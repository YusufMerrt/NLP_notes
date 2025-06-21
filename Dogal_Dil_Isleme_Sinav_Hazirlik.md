# 🎓 DOĞAL DİL İŞLEME FINAL SINAVI HAZIRLIK NOTLARI

## 📋 SINAV YAPISI (Hocanın Belirttiği)
- **3 Ana Soru** (Büyük puanlı)
- **5 Doğru/Yanlış Sorusu** (TF sorusu)
- **Karmaşıklık Matrisi** oluşturma
- **Benzerlik Ölçütleri** hesaplama

---

## 🎯 1. MARKOV MODELİ (Muhtemelen Sınavda Gelecek)

### 📖 **Temel Tanım**
Markov modeli, bir sistemin gelecekteki durumunun **yalnızca mevcut duruma** bağlı olduğu, geçmişin etkisinin olmadığı olasılıksal bir modeldir.

### 🔢 **Matematiksel Formül**
```
P(w₁, w₂, ..., wₙ) = P(w₁) × P(w₂|w₁) × P(w₃|w₂) × ... × P(wₙ|wₙ₋₁)
```

### 📝 **Pratik Örnek**
**Verilen:** "Savaş tazminatı aldılar." cümlesi

**Çözüm:**
```
P(cümle) = P(savaş|BAŞLANGIÇ) × P(tazminatı|savaş) × P(aldılar|tazminatı) × P(.|aldılar)
```

**Sayısal Örnek:**
- P(savaş|BAŞLANGIÇ) = 0.1
- P(tazminatı|savaş) = 0.3  
- P(aldılar|tazminatı) = 0.7
- P(.|aldılar) = 0.9

**Sonuç:** P(cümle) = 0.1 × 0.3 × 0.7 × 0.9 = **0.0189**

### ⚠️ **Önemli Noktalar**
- **Markov Özelliği:** Gelecek sadece şimdiki duruma bağlı
- **Bağımsızlık:** Geçmiş durumlar etkisiz
- **Toplam Olasılık:** Tüm geçişlerin çarpımı

---

## 🎯 2. NAIVE BAYES (Bilmede Fayda Var)

### 📖 **Temel Tanım**
Özelliklerin birbirinden **bağımsız** olduğu varsayımıyla çalışan olasılıksal sınıflandırıcı.

### 🔢 **Matematiksel Formül**
```
P(Sınıf|Veri) ∝ P(Sınıf) × ∏ᵢ P(Özellikᵢ|Sınıf)
```

### 📝 **Pratik Örnek - Spam Tespiti**

**Verilen:**
- **Spam sınıfı:** P(Spam) = 0.3
- **Normal sınıfı:** P(Normal) = 0.7
- **"Ücretsiz" kelimesi:** P(ücretsiz|Spam) = 0.8, P(ücretsiz|Normal) = 0.1
- **"Toplantı" kelimesi:** P(toplantı|Spam) = 0.1, P(toplantı|Normal) = 0.6

**Soru:** "Ücretsiz toplantı" içeren e-posta hangi sınıfa ait?

**Çözüm:**
```
P(Spam|ücretsiz,toplantı) ∝ P(Spam) × P(ücretsiz|Spam) × P(toplantı|Spam)
P(Spam|ücretsiz,toplantı) ∝ 0.3 × 0.8 × 0.1 = 0.024

P(Normal|ücretsiz,toplantı) ∝ P(Normal) × P(ücretsiz|Normal) × P(toplantı|Normal)
P(Normal|ücretsiz,toplantı) ∝ 0.7 × 0.1 × 0.6 = 0.042

Sonuç: Normal sınıfı (0.042 > 0.024)
```

### ⚠️ **Önemli Noktalar**
- **Bağımsızlık Varsayımı:** Gerçekte yanlış ama hesaplamayı kolaylaştırır
- **Laplace Smoothing:** Sıfır olasılık problemini çözer
- **Logaritma:** Çok küçük sayıları önlemek için kullanılır

---

## 🎯 3. BENZERLİK ÖLÇÜTLERİ (Ufak Soru)

### 📖 **Öklid Mesafesi (Euclidean Distance)**

**Formül:**
```
d(x⃗, y⃗) = √(∑ᵢ₌₁ⁿ (xᵢ - yᵢ)²)
```

**Pratik Örnek:**
```
Doküman A: [1, 2, 3, 0, 1]
Doküman B: [2, 1, 3, 1, 0]

d(A,B) = √((1-2)² + (2-1)² + (3-3)² + (0-1)² + (1-0)²)
d(A,B) = √(1 + 1 + 0 + 1 + 1) = √4 = 2
```

### 📖 **Kosinüs Benzerliği (Cosine Similarity)**

**Formül:**
```
cos(θ) = (x⃗ · y⃗) / (||x⃗|| × ||y⃗||)
```

**Pratik Örnek:**
```
Doküman A: [1, 2, 3, 0, 1]
Doküman B: [2, 1, 3, 1, 0]

A · B = 1×2 + 2×1 + 3×3 + 0×1 + 1×0 = 2 + 2 + 9 + 0 + 0 = 13
||A|| = √(1² + 2² + 3² + 0² + 1²) = √15
||B|| = √(2² + 1² + 3² + 1² + 0²) = √15

cos(θ) = 13 / (√15 × √15) = 13/15 ≈ 0.867
```

### ⚠️ **Farklar**
- **Öklid:** Mutlak mesafe, küçük değer = benzer
- **Kosinüs:** Açı benzerliği, büyük değer = benzer
- **Kosinüs:** Doküman uzunluğundan etkilenmez

---

## 🎯 4. CYK ALGORİTMASI (Zor Konu)

### 📖 **Temel Tanım**
Bağımsız gramerlerle verilen cümlenin gramer tarafından üretilip üretilmediğini **dinamik programlama** ile kontrol eder.

### 🔢 **Algoritma Adımları**
1. **Chomsky Normal Form** grameri kullan
2. **Tablo oluştur** (n×n matris)
3. **Köşegen doldur** (tek kelimeler)
4. **Üst köşegenleri doldur** (2'li, 3'lü gruplar)

### 📝 **Pratik Örnek**

**Gramer:**
```
S → NP VP
NP → Det N
VP → V NP
Det → the
N → cat, dog
V → chased
```

**Cümle:** "the cat chased the dog"

**Tablo Doldurma:**
```
    1     2     3     4     5
1  Det   NP    -     -     -
2   -    N     -     -     -
3   -    -     V     -     -
4   -    -     -    Det    NP
5   -    -     -     -     N
```

**Sonuç:** S köşesinde S varsa cümle gramer tarafından üretilir.

### ⚠️ **Shift-Reduce ile Farkları**

| Özellik | CYK | Shift-Reduce |
|---------|-----|--------------|
| **Yöntem** | Tablo doldurma | Yığın işlemi |
| **Karmaşıklık** | O(n³) | O(n) |
| **Kullanım** | Teorik | Pratik |
| **Gramer** | CNF | Herhangi |

---

## 🎯 5. KARMAŞIKLIK MATRİSİ (Confusion Matrix)

### 📖 **Temel Tanım**
Sınıflandırma problemlerinde modelin tahminlerinin doğruluğunu ölçmek için kullanılan tablo.

### 📊 **Matris Yapısı**

| Gerçek/Tahmin | Pozitif | Negatif |
|---------------|---------|---------|
| **Pozitif** | TP | FN |
| **Negatif** | FP | TN |

### 📝 **Pratik Örnek - Spam Tespiti**

**Verilen:**
- 1000 e-posta test edildi
- 200 spam, 800 normal
- Sonuçlar:
  - 150 spam doğru tespit edildi
  - 50 spam yanlış tespit edildi (normal sanıldı)
  - 100 normal yanlış tespit edildi (spam sanıldı)
  - 700 normal doğru tespit edildi

**Karmaşıklık Matrisi:**
```
                Tahmin
Gerçek    Spam    Normal
Spam      150     50
Normal    100     700
```

**Hesaplamalar:**
- TP = 150 (Spam doğru tespit)
- FP = 100 (Normal yanlış spam)
- TN = 700 (Normal doğru tespit)
- FN = 50 (Spam yanlış normal)

---

## 🎯 6. BAŞARI ÖLÇÜTLERİ

### 🔢 **Temel Formüller**

```
Doğruluk (Accuracy) = (TP + TN) / (TP + TN + FP + FN)
Hassasiyet (Precision) = TP / (TP + FP)
Duyarlılık (Recall) = TP / (TP + FN)
F1 Skoru = 2 × (Precision × Recall) / (Precision + Recall)
```

### 📝 **Pratik Örnek**

**Yukarıdaki spam örneği için:**
```
Accuracy = (150 + 700) / 1000 = 850/1000 = 0.85 = 85%
Precision = 150 / (150 + 100) = 150/250 = 0.60 = 60%
Recall = 150 / (150 + 50) = 150/200 = 0.75 = 75%
F1 = 2 × (0.60 × 0.75) / (0.60 + 0.75) = 0.90 / 1.35 = 0.67 = 67%
```

### ⚠️ **Ortalama Hesaplama**

**Ham Ortalama:**
```
(Spam_başarı + Normal_başarı) / 2 = (75% + 87.5%) / 2 = 81.25%
```

**Ağırlıklı Ortalama:**
```
(200/1000 × 75%) + (800/1000 × 87.5%) = 15% + 70% = 85%
```

---

## 🎯 7. EXPECTATION (Beklenti) Hesaplama

### 📖 **Markov Modelinde Beklenti**
Bir durumdan diğerine geçişin beklenen değeri.

### 📝 **Pratik Örnek**

**Verilen:** Hava durumu geçiş olasılıkları
```
Güneşli → Yağmurlu: 0.3
Güneşli → Bulutlu: 0.5
Güneşli → Güneşli: 0.2
```

**Beklenti Hesaplama:**
```
E[Geçiş] = 0.3 × 1 + 0.5 × 1 + 0.2 × 1 = 1
```

### 🔢 **Genel Formül**
```
E[X] = ∑ xᵢ × P(xᵢ)
```

---

## 📚 SLAYT İÇERİKLERİNDEN ÖNEMLİ KONULAR

### 🎯 **Zipf Yasası**
**Formül:** `Zipf = R × F / N_toplam`

**Örnek:** "ile" kelimesi 2. sırada, frekansı 676
```
Zipf = 2 × 676 / 90800 = 0.015
```

### 🎯 **Entropi**
**Formül:** `H(x) = ∑ P(x) × log(1/P(x))`

**Örnek:** AVM'ye gelen arabalar
```
P(sedan) = 0.5, P(hatchback) = 0.25, P(station) = 0.125, P(sport) = 0.125
H(x) = 0.5×1 + 0.25×2 + 2×0.125×3 = 1.5
```

### 🎯 **Eşdizimlilik**
**Pointwise Mutual Information:**
```
I(x,y) = log₂(P(x,y) / (P(x) × P(y)))
```

**Null Hipotez Testi:**
```
H₀: P(x) × P(y) > P(x,y) → Bağımsız
H₁: P(x,y) > P(x) × P(y) → Eşdizim
```

---

## 🎯 SINAV STRATEJİSİ

### 📋 **Sınav Sırası**
1. **Doğru/Yanlış** (5 soru) - Hızlı geç
2. **Benzerlik Ölçütleri** - Kolay puan
3. **Karmaşıklık Matrisi** - Dikkatli hesapla
4. **Ana Sorular** - Zaman ayır

### ⚠️ **Dikkat Edilecek Noktalar**
- **Gauss gelmez** - Normal dağılım yok
- **Shift-Reduce** - CYK ile karşılaştırma
- **Expectation** - Markov modelinde
- **Interpolasyon** - Seyrek kelimeler için

### 📝 **Formül Kartı**
```
Markov: P(w₁...wₙ) = P(w₁) × ∏P(wᵢ|wᵢ₋₁)
Naive Bayes: P(S|V) ∝ P(S) × ∏P(Fᵢ|S)
Öklid: d = √(∑(xᵢ-yᵢ)²)
Kosinüs: cos = (x·y)/(||x||×||y||)
Precision: TP/(TP+FP)
Recall: TP/(TP+FN)
F1: 2×(P×R)/(P+R)
```

---

## 🎓 BAŞARI TAVSİYELERİ

### ✅ **Son Gün Çalışma Planı**
1. **Formülleri tekrar et** (30 dk)
2. **Örnek problemler çöz** (1 saat)
3. **Karmaşıklık matrisi pratiği** (30 dk)
4. **Kısa tanımları gözden geçir** (30 dk)

### 🎯 **Sınav İpuçları**
- **Zaman yönetimi** - Ana sorulara daha fazla zaman ayır
- **Hesaplama kontrolü** - Sonuçları mantık kontrolünden geçir
- **Birim kontrolü** - Olasılıklar 0-1 arasında olmalı
- **Grafik çiz** - Karmaşıklık matrisi için tablo çiz

---

**🎓 BAŞARILAR! Final sınavında başarılar dilerim! 🎓**

*Bu döküman, hocanın vurguladığı konular ve slayt içerikleri göz önünde bulundurularak final sınavına özel olarak hazırlanmıştır.* 