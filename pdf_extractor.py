import pdfplumber
import os

def extract_text_from_pdf(pdf_path, output_file=None):
    """
    PDF dosyasından metin çıkarır ve dosyaya kaydeder
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            all_text = ""
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    all_text += f"\n--- SAYFA {i+1} ---\n"
                    all_text += text
                    all_text += "\n" + "="*50 + "\n"
            
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(all_text)
                print(f"Metin {output_file} dosyasına kaydedildi.")
            
            return all_text
            
    except Exception as e:
        print(f"Hata: {e}")
        return None

def extract_all_pdfs_in_directory():
    """
    Dizindeki tüm PDF dosyalarından metin çıkarır
    """
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        print(f"\nİşleniyor: {pdf_file}")
        output_file = pdf_file.replace('.pdf', '_extracted.txt')
        text = extract_text_from_pdf(pdf_file, output_file)
        
        if text:
            print(f"Başarıyla çıkarıldı: {output_file}")
        else:
            print(f"Çıkarılamadı: {pdf_file}")

if __name__ == "__main__":
    print("PDF Metin Çıkarıcı")
    print("=" * 30)
    
    # Önce gerekli kütüphaneyi kontrol et
    try:
        import pdfplumber
        print("pdfplumber kütüphanesi mevcut.")
    except ImportError:
        print("pdfplumber kütüphanesi bulunamadı.")
        print("Yüklemek için: pip install pdfplumber")
        exit(1)
    
    # Tüm PDF'leri işle
    extract_all_pdfs_in_directory() 