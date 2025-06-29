import fitz  # PyMuPDF
import os
import sys
from PIL import Image
import io
import base64

class GelismisextractorPDF:
    def __init__(self):
        self.output_dir = "ders_notlari"
        self.images_dir = "gorseller"
        
    def setup_directories(self):
        """Gerekli klasörleri oluşturur"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        images_path = os.path.join(self.output_dir, self.images_dir)
        if not os.path.exists(images_path):
            os.makedirs(images_path)
            
    def extract_images_from_page(self, page, pdf_name, page_num):
        """Sayfadaki görselleri çıkarır"""
        image_list = page.get_images()
        images_info = []
        
        for img_index, img in enumerate(image_list):
            try:
                xref = img[0]
                pix = fitz.Pixmap(page.parent, xref)
                
                # RGB formatına çevir
                if pix.n - pix.alpha < 4:
                    img_data = pix.tobytes("png")
                    
                    # Dosya adı oluştur
                    img_filename = f"{pdf_name}_sayfa{page_num}_gorsel{img_index + 1}.png"
                    img_path = os.path.join(self.output_dir, self.images_dir, img_filename)
                    
                    # Görüntüyü kaydet
                    with open(img_path, "wb") as img_file:
                        img_file.write(img_data)
                    
                    images_info.append({
                        'filename': img_filename,
                        'path': img_path,
                        'index': img_index + 1
                    })
                    
                pix = None
                
            except Exception as e:
                print(f"Görsel çıkarma hatası: {e}")
                continue
                
        return images_info
    
    def extract_pdf_content(self, pdf_path):
        """PDF'den tüm içeriği çıkarır"""
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        content = {
            'filename': pdf_name,
            'pages': [],
            'total_pages': 0,
            'total_images': 0
        }
        
        try:
            doc = fitz.open(pdf_path)
            content['total_pages'] = len(doc)
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                
                # Metni çıkar
                text = page.get_text()
                
                # Görselleri çıkar
                images = self.extract_images_from_page(page, pdf_name, page_num + 1)
                content['total_images'] += len(images)
                
                # Sayfa bilgilerini kaydet
                page_info = {
                    'page_number': page_num + 1,
                    'text': text,
                    'images': images,
                    'image_count': len(images)
                }
                
                content['pages'].append(page_info)
                
            doc.close()
            
        except Exception as e:
            print(f"PDF işleme hatası ({pdf_path}): {e}")
            return None
            
        return content
    
    def create_markdown_notes(self, pdf_content):
        """Markdown formatında ders notları oluşturur"""
        md_content = f"# {pdf_content['filename']}\n\n"
        md_content += f"**Toplam Sayfa:** {pdf_content['total_pages']}\n"
        md_content += f"**Toplam Görsel:** {pdf_content['total_images']}\n\n"
        md_content += "---\n\n"
        
        for page in pdf_content['pages']:
            md_content += f"## Sayfa {page['page_number']}\n\n"
            
            # Görseller varsa önce onları ekle
            if page['images']:
                md_content += "### Görseller\n\n"
                for img in page['images']:
                    img_path = os.path.join(self.images_dir, img['filename'])
                    md_content += f"![Görsel {img['index']}]({img_path})\n\n"
                    md_content += f"*Görsel {img['index']}: {img['filename']}*\n\n"
            
            # Metin içeriği
            if page['text'].strip():
                md_content += "### İçerik\n\n"
                md_content += page['text']
                md_content += "\n\n"
            
            md_content += "---\n\n"
        
        return md_content
    
    def process_all_pdfs(self):
        """Dizindeki tüm PDF'leri işler"""
        self.setup_directories()
        
        pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
        all_content = []
        
        print(f"Toplam {len(pdf_files)} PDF dosyası bulundu.\n")
        
        for i, pdf_file in enumerate(pdf_files, 1):
            print(f"[{i}/{len(pdf_files)}] İşleniyor: {pdf_file}")
            
            content = self.extract_pdf_content(pdf_file)
            if content:
                all_content.append(content)
                
                # Her PDF için ayrı markdown dosyası oluştur
                md_content = self.create_markdown_notes(content)
                md_filename = f"{content['filename']}.md"
                md_path = os.path.join(self.output_dir, md_filename)
                
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                print(f"   ✓ {content['total_pages']} sayfa işlendi")
                print(f"   ✓ {content['total_images']} görsel çıkarıldı")
                print(f"   ✓ Ders notu kaydedildi: {md_path}")
            else:
                print(f"   ✗ Hata: {pdf_file} işlenemedi")
            
            print()
        
        # Birleşik ders notu oluştur
        self.create_combined_notes(all_content)
        
        return all_content
    
    def create_combined_notes(self, all_content):
        """Tüm PDF'lerin birleşik ders notunu oluşturur"""
        combined_md = "# Doğal Dil İşleme - Kapsamlı Ders Notları\n\n"
        combined_md += f"**Toplam Dosya:** {len(all_content)}\n"
        
        total_pages = sum(content['total_pages'] for content in all_content)
        total_images = sum(content['total_images'] for content in all_content)
        
        combined_md += f"**Toplam Sayfa:** {total_pages}\n"
        combined_md += f"**Toplam Görsel:** {total_images}\n\n"
        
        # İçindekiler
        combined_md += "## İçindekiler\n\n"
        for i, content in enumerate(all_content, 1):
            combined_md += f"{i}. [{content['filename']}](#{content['filename'].lower().replace(' ', '-').replace('ç', 'c').replace('ğ', 'g').replace('ı', 'i').replace('ö', 'o').replace('ş', 's').replace('ü', 'u')})\n"
        combined_md += "\n---\n\n"
        
        # Her PDF'in içeriğini ekle
        for content in all_content:
            combined_md += f"# {content['filename']}\n\n"
            
            for page in content['pages']:
                combined_md += f"## {content['filename']} - Sayfa {page['page_number']}\n\n"
                
                # Görseller
                if page['images']:
                    combined_md += "### Görseller\n\n"
                    for img in page['images']:
                        img_path = os.path.join(self.images_dir, img['filename'])
                        combined_md += f"![Görsel]({img_path})\n\n"
                
                # Metin
                if page['text'].strip():
                    combined_md += "### İçerik\n\n"
                    combined_md += page['text']
                    combined_md += "\n\n"
                
                combined_md += "---\n\n"
        
        # Birleşik dosyayı kaydet
        combined_path = os.path.join(self.output_dir, "Kapsamli_Ders_Notlari.md")
        with open(combined_path, 'w', encoding='utf-8') as f:
            f.write(combined_md)
        
        print(f"✓ Kapsamlı ders notları oluşturuldu: {combined_path}")

def main():
    print("Gelişmiş PDF Çıkarıcı")
    print("=" * 50)
    
    # Gerekli kütüphaneleri kontrol et
    try:
        import fitz
        print("✓ PyMuPDF (fitz) kütüphanesi mevcut")
    except ImportError:
        print("✗ PyMuPDF kütüphanesi bulunamadı")
        print("Yüklemek için: pip install PyMuPDF")
        return
    
    try:
        from PIL import Image
        print("✓ Pillow kütüphanesi mevcut")
    except ImportError:
        print("✗ Pillow kütüphanesi bulunamadı")
        print("Yüklemek için: pip install Pillow")
        return
    
    print("\nİşlem başlatılıyor...\n")
    
    extractor = GelismisextractorPDF()
    extractor.process_all_pdfs()
    
    print("\n" + "=" * 50)
    print("Tüm PDF'ler başarıyla işlendi!")
    print("Ders notları 'ders_notlari' klasöründe oluşturuldu.")

if __name__ == "__main__":
    main() 