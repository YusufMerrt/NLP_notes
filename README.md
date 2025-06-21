# 🎓 DOĞAL DİL İŞLEME - DETAYLI KONU ANLATIMI

## 🎯 1. MARKOV MODELİ - DETAYLI ANALİZ

### 📖 **Teorik Temeller**

#### **Tarihsel Gelişim:**
Markov modelleri, **Andrey Markov** tarafından 1906'da geliştirildi. İlk olarak Rus şiirindeki sesli harf dizilerini analiz etmek için kullanıldı.

#### **Matematiksel Temel:**
Markov özelliği, bir **stokastik süreç**'in gelecekteki durumunun **yalnızca mevcut duruma** bağlı olduğunu, geçmiş durumların etkisinin olmadığını belirtir.

**Formal Tanım:**
```
P(Xₙ₊₁ = x | X₁ = x₁, X₂ = x₂, ..., Xₙ = xₙ) = P(Xₙ₊₁ = x | Xₙ = xₙ)
```

### 🔢 **Dil Modellemede Markov Zinciri**

#### **N-Gram Modelleri:**
- **Unigram:** P(w₁, w₂, ..., wₙ) = P(w₁) × P(w₂) × ... × P(wₙ)
- **Bigram:** P(w₁, w₂, ..., wₙ) = P(w₁) × P(w₂|w₁) × P(w₃|w₂) × ... × P(wₙ|wₙ₋₁)
- **Trigram:** P(w₁, w₂, ..., wₙ) = P(w₁) × P(w₂|w₁) × P(w₃|w₁,w₂) × ... × P(wₙ|wₙ₋₂,wₙ₋₁)

#### **Detaylı Örnek - Bigram Model:**

**İngilizce Örnek:**

**Verilen Kelime Geçiş Olasılıkları:**
```
P(BAŞLANGIÇ|savaş) = 0.1
P(savaş|tazminatı) = 0.3
P(tazminatı|aldılar) = 0.2
P(aldılar|.) = 0.8
P(.|SON) = 0.9
```

**Cümle:** "Savaş tazminatı aldılar."

**Adım Adım Hesaplama:**
```
P(cümle) = P(savaş|BAŞLANGIÇ) × P(tazminatı|savaş) × P(aldılar|tazminatı) × P(.|aldılar) × P(SON|.)

P(cümle) = 0.1 × 0.3 × 0.2 × 0.8 × 0.9
P(cümle) = 0.00432
```

**Türkçe Örnek:**

**Verilen Kelime Geçiş Olasılıkları:**
```
P(BAŞLANGIÇ|bugün) = 0.15
P(bugün|hava) = 0.4
P(hava|çok) = 0.3
P(çok|güzel) = 0.6
P(güzel|.) = 0.7
P(.|SON) = 0.9
```

**Cümle:** "Bugün hava çok güzel."

**Adım Adım Hesaplama:**
```
P(cümle) = P(bugün|BAŞLANGIÇ) × P(hava|bugün) × P(çok|hava) × P(güzel|çok) × P(.|güzel) × P(SON|.)

P(cümle) = 0.15 × 0.4 × 0.3 × 0.6 × 0.7 × 0.9
P(cümle) = 0.006804
```

**Karşılaştırmalı Analiz:**

| Özellik | İngilizce | Türkçe |
|---------|-----------|--------|
| **Cümle** | "Savaş tazminatı aldılar." | "Bugün hava çok güzel." |
| **Uzunluk** | 4 kelime | 5 kelime |
| **Olasılık** | 0.00432 | 0.006804 |
| **Konu** | Tarihsel | Günlük |
| **Karmaşıklık** | Orta | Düşük |

### 📊 **Markov Modelinin Avantajları ve Dezavantajları**

#### ✅ **Avantajlar:**
- **Hesaplama Kolaylığı:** Sadece mevcut duruma bakılır
- **Bellek Verimliliği:** Geçmiş bilgiler saklanmaz
- **Hızlı Eğitim:** Az parametre ile eğitilir

#### ❌ **Dezavantajlar:**
- **Kısa Hafıza:** Uzun bağımlılıkları yakalayamaz
- **Sıfır Olasılık:** Eğitim verisinde görülmeyen geçişler
- **Bağlam Eksikliği:** Uzun mesafeli bağlamları unutur

### 🔧 **Smoothing Teknikleri**

#### **Laplace Smoothing (Add-1):**
```
P(wᵢ|wᵢ₋₁) = (count(wᵢ₋₁, wᵢ) + 1) / (count(wᵢ₋₁) + V)
```
V = kelime dağarcığı boyutu

#### **Interpolasyon:**
```
P(wᵢ|wᵢ₋₂, wᵢ₋₁) = λ₁P(wᵢ) + λ₂P(wᵢ|wᵢ₋₁) + λ₃P(wᵢ|wᵢ₋₂, wᵢ₋₁)
```

---

## 🎯 2. SHIFT-REDUCE ALGORİTMASI - DETAYLI ANALİZ

### 📖 **Teorik Temeller**

#### **Tarihsel Gelişim:**
Shift-Reduce algoritması, **Donald Knuth** tarafından 1965'te geliştirilen **LR parsing** algoritmasının temelidir. **Bottom-up parsing** yaklaşımını kullanır.

#### **Matematiksel Temel:**
Shift-Reduce, **yığın (stack)** tabanlı bir algoritmadır. Cümleyi **soldan sağa** işler ve **en sağdan türetme (rightmost derivation)** yapar.

**Temel İşlemler:**
1. **Shift:** Girdi kelimesini yığına ekle
2. **Reduce:** Yığındaki öğeleri gramer kuralına göre birleştir
3. **Accept:** Cümle başarıyla parse edildi
4. **Error:** Gramer hatası tespit edildi

### 🔢 **Algoritma Adımları - Detaylı Açıklama**

#### **Adım 1: Yığın ve Girdi Hazırlama**
```
Yığın: [] (boş)
Girdi: [w₁, w₂, w₃, ..., wₙ]
```

#### **Adım 2: İşlem Döngüsü**
Her adımda şu kararlardan biri alınır:
- **Shift:** Girdiden kelime al, yığına ekle
- **Reduce:** Yığındaki öğeleri gramer kuralına göre birleştir
- **Accept:** Cümle tamamlandı
- **Error:** Gramer hatası

### 📝 **Detaylı Örnek - Adım Adım**

#### **İngilizce Örnek:**

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

**Adım Adım İşlem:**

| Adım | Yığın | Girdi | İşlem | Açıklama |
|------|-------|-------|-------|----------|
| 1 | [] | [the, cat, chased, the, dog] | Shift | "the" yığına ekle |
| 2 | [the] | [cat, chased, the, dog] | Shift | "cat" yığına ekle |
| 3 | [the, cat] | [chased, the, dog] | Reduce | Det + N → NP |
| 4 | [NP] | [chased, the, dog] | Shift | "chased" yığına ekle |
| 5 | [NP, chased] | [the, dog] | Shift | "the" yığına ekle |
| 6 | [NP, chased, the] | [dog] | Shift | "dog" yığına ekle |
| 7 | [NP, chased, the, dog] | [] | Reduce | Det + N → NP |
| 8 | [NP, chased, NP] | [] | Reduce | V + NP → VP |
| 9 | [NP, VP] | [] | Reduce | NP + VP → S |
| 10 | [S] | [] | Accept | Cümle tamamlandı |

#### **Türkçe Örnek:**

**Gramer:**
```
S → NP VP
NP → Det N
VP → V NP
Det → bu, şu, o
N → kedi, köpek, kuş
V → kovaladı, gördü
```

**Cümle:** "bu kedi köpeği kovaladı"

**Adım Adım İşlem:**

| Adım | Yığın | Girdi | İşlem | Açıklama |
|------|-------|-------|-------|----------|
| 1 | [] | [bu, kedi, köpeği, kovaladı] | Shift | "bu" yığına ekle |
| 2 | [bu] | [kedi, köpeği, kovaladı] | Shift | "kedi" yığına ekle |
| 3 | [bu, kedi] | [köpeği, kovaladı] | Reduce | Det + N → NP |
| 4 | [NP] | [köpeği, kovaladı] | Shift | "köpeği" yığına ekle |
| 5 | [NP, köpeği] | [kovaladı] | Shift | "kovaladı" yığına ekle |
| 6 | [NP, köpeği, kovaladı] | [] | Reduce | N + V → VP |
| 7 | [NP, VP] | [] | Reduce | NP + VP → S |
| 8 | [S] | [] | Accept | Cümle tamamlandı |

#### **Karşılaştırmalı Analiz:**

| Özellik | İngilizce | Türkçe |
|---------|-----------|--------|
| **Cümle** | "the cat chased the dog" | "bu kedi köpeği kovaladı" |
| **Uzunluk** | 5 kelime | 4 kelime |
| **Adım Sayısı** | 10 adım | 8 adım |
| **Yapı** | Det N V Det N | Det N N V |
| **Karmaşıklık** | Orta | Düşük |
| **Reduce İşlemleri** | 3 adet | 2 adet |

### 📊 **Shift-Reduce Algoritmasının Avantajları ve Dezavantajları**

#### ✅ **Avantajlar:**
- **Hızlı İşlem:** O(n) zaman karmaşıklığı
- **Bellek Verimli:** Sadece yığın boyutu kadar bellek
- **Gerçek Zamanlı:** Kelime kelime işleyebilir
- **Hata Tespiti:** İlk hatada durur
- **Esnek:** Herhangi bir gramer türü ile çalışır

#### ❌ **Dezavantajlar:**
- **Karmaşık Karar:** Shift mi Reduce mu yapılacağına karar vermek zor
- **Ambiguity:** Birden fazla parse ağacı olabilir
- **Gramer Bağımlılığı:** Gramer kalitesi önemli
- **Hata Kurtarma:** Hata sonrası devam etmek zor

### 🔧 **Karar Mekanizması**

#### **Shift-Reduce Kararı:**
Algoritma her adımda şu kriterlere bakar:
1. **Yığındaki son öğeler** gramer kuralına uyuyor mu?
2. **Girdideki sonraki kelime** hangi kuralı bekliyor?
3. **Lookahead:** Bir sonraki kelimeye bakarak karar ver

#### **Örnek Karar Süreci:**
```
Yığın: [NP, chased]
Girdi: [the, dog]
Durum: chased (V) var, NP bekliyor
Karar: Shift (çünkü NP oluşturmak için daha fazla kelime gerekli)
```

### ⚡ **Algoritma Karmaşıklığı**

#### **Zaman Karmaşıklığı:**
- **O(n)** - Her kelime bir kez işlenir
- **En kötü durum:** O(n²) - Her adımda reduce

#### **Uzay Karmaşıklığı:**
- **O(n)** - Yığın boyutu cümle uzunluğu kadar

#### **Pratik Performans:**
```
n = 20 kelimelik cümle için:
- Zaman: ~20-40 işlem
- Uzay: ~20 kelime
```

---

## 🎯 3. CYK ALGORİTMASI - DETAYLI ANALİZ

### 📖 **Teorik Temeller**

#### **Tarihsel Gelişim:**
CYK (Cocke-Younger-Kasami) algoritması, **John Cocke**, **Daniel Younger** ve **Tadao Kasami** tarafından 1960'larda bağımsız olarak geliştirildi.

#### **Matematiksel Temel:**
CYK, **Chomsky Normal Form** (CNF) gramerlerle çalışan **dinamik programlama** algoritmasıdır.

**CNF Kuralları:**
1. A → BC (iki terminal olmayan)
2. A → a (tek terminal)
3. S → ε (sadece başlangıç sembolü için)

### 🔢 **Algoritma Adımları - Detaylı Açıklama**

#### **Adım 1: Grameri CNF'ye Dönüştür**
```
Orijinal Gramer:
S → NP VP
NP → Det N | N
VP → V NP
Det → the
N → cat, dog, mouse
V → chased, saw

CNF Dönüşümü:
S → NP VP
NP → Det N
NP → N
VP → V NP
Det → the
N → cat
N → dog  
N → mouse
V → chased
V → saw
```

#### **Adım 2: Tablo Oluştur**
n×n matris oluştur (n = cümle uzunluğu)

#### **Adım 3: Köşegen Doldur (Tek Kelimeler)**
```
Cümle: "the cat chased the dog"
Uzunluk: 5

    1     2     3     4     5
1  Det   -     -     -     -
2   -    N     -     -     -
3   -    -     V     -     -
4   -    -     -    Det    -
5   -    -     -     -     N
```

#### **Adım 4: Üst Köşegenleri Doldur**

**2'li Gruplar (Uzunluk 2):**
```
[1,2]: Det + N = NP
[2,3]: N + V = (geçersiz)
[3,4]: V + Det = (geçersiz)
[4,5]: Det + N = NP

    1     2     3     4     5
1  Det   NP    -     -     -
2   -    N     -     -     -
3   -    -     V     -     -
4   -    -     -    Det    NP
5   -    -     -     -     N
```

**3'lü Gruplar (Uzunluk 3):**
```
[1,3]: Det + N + V = (geçersiz)
[2,4]: N + V + Det = (geçersiz)
[3,5]: V + Det + N = VP

    1     2     3     4     5
1  Det   NP    -     -     -
2   -    N     -     -     -
3   -    -     V     -     -
4   -    -     -    Det    NP
5   -    -     -     -     N
```

**4'lü Gruplar (Uzunluk 4):**
```
[1,4]: Det + N + V + Det = (geçersiz)
[2,5]: N + V + Det + N = (geçersiz)
```

**5'li Gruplar (Uzunluk 5):**
```
[1,5]: Det + N + V + Det + N = S

    1     2     3     4     5
1  Det   NP    -     -     S
2   -    N     -     -     -
3   -    -     V     -     -
4   -    -     -    Det    NP
5   -    -     -     -     N
```

### 📝 **Detaylı Örnek - Adım Adım**

#### **İngilizce Örnek:**

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

**Tablo Doldurma Süreci:**

1. **Köşegen (Tek Kelimeler):**
   - [1,1]: "the" → Det
   - [2,2]: "cat" → N
   - [3,3]: "chased" → V
   - [4,4]: "the" → Det
   - [5,5]: "dog" → N

2. **2'li Gruplar:**
   - [1,2]: Det + N → NP
   - [4,5]: Det + N → NP

3. **3'lü Gruplar:**
   - [3,5]: V + NP → VP

4. **5'li Grup:**
   - [1,5]: NP + VP → S

**Sonuç:** S köşesinde S varsa cümle gramer tarafından üretilir.

#### **Türkçe Örnek:**

**Gramer:**
```
S → NP VP
NP → Det N
VP → V NP
Det → bu, şu, o
N → kedi, köpek, kuş
V → kovaladı, gördü
```

**Cümle:** "bu kedi köpeği kovaladı"

**Tablo Doldurma Süreci:**

1. **Köşegen (Tek Kelimeler):**
   - [1,1]: "bu" → Det
   - [2,2]: "kedi" → N
   - [3,3]: "köpeği" → N
   - [4,4]: "kovaladı" → V

2. **2'li Gruplar:**
   - [1,2]: Det + N → NP
   - [3,4]: N + V → VP

3. **4'lü Grup:**
   - [1,4]: NP + VP → S

**Sonuç:** S köşesinde S varsa cümle gramer tarafından üretilir.

#### **Karşılaştırmalı Tablo:**

| Özellik | İngilizce | Türkçe |
|---------|-----------|--------|
| **Cümle** | "the cat chased the dog" | "bu kedi köpeği kovaladı" |
| **Uzunluk** | 5 kelime | 4 kelime |
| **Yapı** | Det N V Det N | Det N N V |
| **Karmaşıklık** | 5×5 tablo | 4×4 tablo |
| **İşlem Sayısı** | 10 adım | 8 adım |

### ⚡ **Algoritma Karmaşıklığı**

#### **Zaman Karmaşıklığı:**
- **O(n³)** - Üç iç içe döngü
- **Uzay Karmaşıklığı:** O(n²) - n×n tablo

#### **Pratik Uygulamalar:**
```
n = 10 kelimelik cümle için:
- Zaman: 10³ = 1000 işlem
- Uzay: 10² = 100 hücre
```

---

## 🎯 4. SHIFT-REDUCE vs CYK - DETAYLI KARŞILAŞTIRMA

### 📊 **Temel Karşılaştırma Tablosu**

| Özellik | Shift-Reduce | CYK |
|---------|--------------|-----|
| **Yöntem** | Yığın tabanlı | Tablo doldurma |
| **Parsing Türü** | Bottom-up | Bottom-up |
| **Gramer Türü** | Herhangi | CNF |
| **Zaman Karmaşıklığı** | O(n) | O(n³) |
| **Uzay Karmaşıklığı** | O(n) | O(n²) |
| **Gerçek Zamanlı** | ✅ Evet | ❌ Hayır |
| **Hata Tespiti** | Hızlı | Yavaş |
| **Ambiguity** | İlk bulduğunu alır | Tüm parse ağaçlarını bulur |
| **Uygulama** | Pratik | Teorik |
| **Bellek Kullanımı** | Düşük | Yüksek |

### 🔄 **Detaylı Karşılaştırma**

#### **1. Çalışma Prensibi:**

**Shift-Reduce:**
```
- Soldan sağa işler
- Yığın kullanır
- Her adımda karar verir
- İlk hatada durur
```

**CYK:**
```
- Tüm cümleyi görür
- Tablo doldurur
- Sonunda karar verir
- Tüm olasılıkları hesaplar
```

#### **2. Gramer Gereksinimleri:**

**Shift-Reduce:**
```
- Herhangi bir gramer türü
- Dönüştürme gerekmez
- Esnek yapı
```

**CYK:**
```
- Sadece CNF gramerler
- Dönüştürme zorunlu
- Kısıtlı yapı
```

#### **3. Hata Yönetimi:**

**Shift-Reduce:**
```
- İlk hatada durur
- Hızlı hata tespiti
- Hata kurtarma zor
```

**CYK:**
```
- Tüm tabloyu doldurur
- Yavaş hata tespiti
- Hata analizi kolay
```

### 📝 **Pratik Örneklerle Karşılaştırma**

#### **Örnek 1: "the cat chased the dog"**

**Shift-Reduce Süreci:**
```
Adım 1: [the] ← Shift
Adım 2: [the, cat] ← Shift  
Adım 3: [NP] ← Reduce (Det + N → NP)
Adım 4: [NP, chased] ← Shift
Adım 5: [NP, chased, the] ← Shift
Adım 6: [NP, chased, the, dog] ← Shift
Adım 7: [NP, chased, NP] ← Reduce (Det + N → NP)
Adım 8: [NP, VP] ← Reduce (V + NP → VP)
Adım 9: [S] ← Reduce (NP + VP → S)
Adım 10: Accept
```

**CYK Süreci:**
```
1. Tablo oluştur (5×5)
2. Köşegen doldur: [Det, N, V, Det, N]
3. 2'li gruplar: [NP, -, -, NP]
4. 3'lü gruplar: [-, -, VP, -]
5. 5'li grup: [S]
6. Sonuç: S köşesinde S var → Kabul
```

#### **Örnek 2: Ambiguous Cümle**

**Cümle:** "I saw the man with the telescope"

**Shift-Reduce:**
```
- İlk bulduğu parse ağacını kabul eder
- Hızlı karar verir
- Diğer olasılıkları görmez
```

**CYK:**
```
- Tüm olası parse ağaçlarını bulur
- Ambiguity'yi tespit eder
- Hangi yapının daha olası olduğunu hesaplar
```

### ⚡ **Performans Karşılaştırması**

#### **Zaman Karşılaştırması:**
```
Cümle Uzunluğu | Shift-Reduce | CYK
10 kelime      | ~10-20 işlem | ~1000 işlem
20 kelime      | ~20-40 işlem | ~8000 işlem
50 kelime      | ~50-100 işlem| ~125000 işlem
```

#### **Bellek Karşılaştırması:**
```
Cümle Uzunluğu | Shift-Reduce | CYK
10 kelime      | ~10 kelime   | ~100 hücre
20 kelime      | ~20 kelime   | ~400 hücre
50 kelime      | ~50 kelime   | ~2500 hücre
```

### 🎯 **Hangi Durumda Hangi Algoritma?**

#### **Shift-Reduce Kullan:**
- **Gerçek zamanlı** uygulamalar
- **Hızlı** parsing gerektiğinde
- **Bellek** kısıtlı olduğunda
- **Pratik** uygulamalar
- **Hata tespiti** önemli olduğunda

#### **CYK Kullan:**
- **Teorik** analiz
- **Ambiguity** tespiti
- **Tüm olasılıkları** görmek istediğinde
- **Gramer doğrulama**
- **Akademik** çalışmalar

### 📊 **Gramer Dönüştürme Örneği**

#### **Normal Gramer → CNF:**

**Orijinal Gramer:**
```
S → NP VP
NP → Det N | N
VP → V NP | V NP PP
PP → P NP
Det → the, a
N → cat, dog, telescope
V → saw, chased
P → with
```

**CNF Dönüşümü:**
```
S → NP VP
NP → Det N
NP → N
VP → V NP
VP → V NP_PP
NP_PP → NP PP
PP → P NP
Det → the
Det → a
N → cat
N → dog
N → telescope
V → saw
V → chased
P → with
```

**Dönüştürme Kuralları:**
1. **A → BCD** → **A → BE, E → CD**
2. **A → a|b** → **A → a, A → b**
3. **Terminal olmayanlar** sadece 2 terminal olmayan üretebilir

---

## 🎯 5. EXPECTATION (BEKLENTİ) - DETAYLI ANALİZ

### 📖 **Teorik Temeller**

#### **Matematiksel Tanım:**
Beklenti, bir rastgele değişkenin **ortalama değeri**'dir.

**Formal Tanım:**
```
E[X] = ∑ xᵢ × P(xᵢ)
```

#### **Sürekli Değişkenler İçin:**
```
E[X] = ∫ x × f(x) dx
```

### 🔢 **Markov Modelinde Beklenti**

#### **Durum Geçiş Beklentisi:**
Bir durumdan diğerine geçişin beklenen sayısı.

**Formül:**
```
E[Geçiş] = ∑ P(geçişᵢ) × değerᵢ
```

#### **Detaylı Örnek - Hava Durumu Modeli:**

**Geçiş Olasılıkları:**
```
Güneşli → Yağmurlu: 0.3
Güneşli → Bulutlu: 0.5
Güneşli → Güneşli: 0.2
```

**Beklenti Hesaplama:**
```
E[Geçiş] = 0.3 × 1 + 0.5 × 1 + 0.2 × 1 = 1
```

**Açıklama:** Her geçiş 1 adım sayıldığı için toplam beklenti 1'dir.

### 📊 **Dil Modellemede Beklenti**

#### **Kelime Beklentisi:**
Bir kelimenin bir cümlede kaç kez geçeceğinin beklenen değeri.

**Örnek:**
```
P("the") = 0.05
Cümle uzunluğu = 20

E["the"] = 20 × 0.05 = 1
```

#### **Cümle Uzunluğu Beklentisi:**
Bir dil modelinin üreteceği cümlelerin ortalama uzunluğu.

**Formül:**
```
E[Uzunluk] = ∑ i × P(Uzunluk = i)
```

### 🔧 **Koşullu Beklenti**

#### **Tanım:**
Bir olayın gerçekleşmesi koşuluyla başka bir olayın beklenen değeri.

**Formül:**
```
E[X|Y] = ∑ x × P(X=x|Y)
```

#### **Markov Modelinde:**
```
E[SonrakiKelime|MevcutKelime] = ∑ kelime × P(SonrakiKelime=kelime|MevcutKelime)
```

### 📝 **Pratik Uygulamalar**

#### **1. Metin Üretimi:**
```
Verilen: "Bugün hava"
Beklenti: E[SonrakiKelime] = 0.3×"güzel" + 0.4×"kötü" + 0.3×"yağmurlu"
Sonuç: "kötü" (en yüksek olasılık)
```

#### **2. Model Değerlendirmesi:**
```
Test cümlesi: "the cat sat on the mat"
Model tahminleri:
- P("cat"|"the") = 0.1
- P("sat"|"cat") = 0.05
- P("on"|"sat") = 0.2
- P("the"|"on") = 0.3
- P("mat"|"the") = 0.15

Beklenti: E[Olasılık] = 0.1 × 0.05 × 0.2 × 0.3 × 0.15 = 0.000045
```

### ⚡ **Beklenti Hesaplama Teknikleri**

#### **1. Monte Carlo Simülasyonu:**
```
1. Çok sayıda rastgele örnek üret
2. Her örneğin değerini hesapla
3. Ortalamasını al
```

#### **2. Dinamik Programlama:**
```
1. Alt problemleri çöz
2. Sonuçları tabloda sakla
3. Büyük problemi küçük parçalardan oluştur
```

### 📊 **Beklenti vs Varyans**

#### **Beklenti (E[X]):**
- Ortalama değer
- Merkezi eğilim

#### **Varyans (Var[X]):**
```
Var[X] = E[(X - E[X])²] = E[X²] - (E[X])²
```
- Değişkenlik ölçüsü
- Dağılımın genişliği

### 🔄 **Markov Modelinde Varyans**

#### **Durum Geçiş Varyansı:**
```
Var[Geçiş] = E[Geçiş²] - (E[Geçiş])²
```

**Örnek:**
```
Geçiş değerleri: [1, 1, 1] (her geçiş 1 adım)
Olasılıklar: [0.3, 0.5, 0.2]

E[Geçiş] = 1
E[Geçiş²] = 0.3×1² + 0.5×1² + 0.2×1² = 1
Var[Geçiş] = 1 - 1² = 0
```

---

## 🎯 SINAVDA ÇIKABİLECEK SORU TİPLERİ

### 📝 **Markov Modeli Soruları:**

#### **Soru Tipi 1: Cümle Olasılığı Hesaplama**
```
Verilen: Geçiş olasılıkları ve bir cümle
İstenen: Cümlenin olasılığını hesapla

Çözüm: P(w₁...wₙ) = P(w₁) × ∏P(wᵢ|wᵢ₋₁)
```

#### **Soru Tipi 2: Beklenti Hesaplama**
```
Verilen: Durum geçiş olasılıkları
İstenen: Beklenen geçiş sayısını hesapla

Çözüm: E[X] = ∑xᵢ × P(xᵢ)
```

### 📝 **CYK Algoritması Soruları:**

#### **Soru Tipi 1: Tablo Doldurma**
```
Verilen: CNF gramer ve cümle
İstenen: CYK tablosunu doldur

Çözüm: Köşegenden başla, üst köşegenleri doldur
```

#### **Soru Tipi 2: Gramer Dönüştürme**
```
Verilen: Normal gramer
İstenen: CNF'ye dönüştür

Çözüm: A → BCD → A → BE, E → CD
```

### 📝 **Shift-Reduce Soruları:**

#### **Soru Tipi 1: Adım Adım Parsing**
```
Verilen: Gramer ve cümle
İstenen: Shift-Reduce adımlarını göster

Çözüm: Yığın ve girdi durumlarını takip et
```

#### **Soru Tipi 2: Karar Mekanizması**
```
Verilen: Yığın ve girdi durumu
İstenen: Shift mi Reduce mu yapılacağına karar ver

Çözüm: Gramer kurallarına ve lookahead'e bak
```

### 📝 **Expectation Soruları:**

#### **Soru Tipi 1: Koşullu Beklenti**
```
Verilen: Koşullu olasılıklar
İstenen: E[X|Y] hesapla

Çözüm: E[X|Y] = ∑x × P(X=x|Y)
```

#### **Soru Tipi 2: Model Değerlendirmesi**
```
Verilen: Test verisi ve model tahminleri
İstenen: Beklenen performansı hesapla

Çözüm: E[Performans] = ∑P(tahmin) × değer
```

---

## 🎓 BAŞARI TAVSİYELERİ

### ✅ **Son Gün Çalışma Planı:**

1. **Markov Modeli (2 saat):**
   - Formülleri ezberle
   - Örnek problemler çöz
   - Beklenti hesaplamaları yap

2. **CYK Algoritması (2 saat):**
   - Tablo doldurma pratiği
   - CNF dönüşümleri
   - Shift-Reduce karşılaştırması

3. **Shift-Reduce (1 saat):**
   - Adım adım parsing
   - Karar mekanizması
   - Pratik örnekler

4. **Expectation (1 saat):**
   - Koşullu beklenti hesaplamaları
   - Varyans formülleri
   - Pratik uygulamalar

### 🎯 **Sınav İpuçları:**

- **Zaman yönetimi:** CYK en çok zaman alır
- **Hesaplama kontrolü:** Sonuçları mantık kontrolünden geçir
- **Birim kontrolü:** Olasılıklar 0-1 arasında olmalı
- **Grafik çiz:** CYK için tablo çiz
- **Adım takibi:** Shift-Reduce için yığın durumunu takip et

### 📝 **Formül Kartı:**
```
Markov: P(w₁...wₙ) = P(w₁) × ∏P(wᵢ|wᵢ₋₁)
CYK: O(n³) zaman, O(n²) uzay
Shift-Reduce: O(n) zaman, O(n) uzay
Expectation: E[X] = ∑xᵢ × P(xᵢ)
Koşullu: E[X|Y] = ∑x × P(X=x|Y)
Varyans: Var[X] = E[X²] - (E[X])²
```

---

**🎓 BAŞARILAR! Final sınavında başarılar dilerim! 🎓**

*Bu döküman, CYK, Markov, Shift-Reduce ve Expectation konularına özel olarak detaylandırılmıştır.*

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

### 📝 **Türkçe Örnek - Duygu Analizi**

**Verilen:**
- 500 yorum test edildi
- 300 pozitif, 200 negatif
- Sonuçlar:
  - 250 pozitif doğru tespit edildi
  - 50 pozitif yanlış tespit edildi (negatif sanıldı)
  - 30 negatif yanlış tespit edildi (pozitif sanıldı)
  - 170 negatif doğru tespit edildi

**Karmaşıklık Matrisi:**
```
                Tahmin
Gerçek    Pozitif    Negatif
Pozitif   250        50
Negatif   30         170
```

**Hesaplamalar:**
- TP = 250 (Pozitif doğru tespit)
- FP = 30 (Negatif yanlış pozitif)
- TN = 170 (Negatif doğru tespit)
- FN = 50 (Pozitif yanlış negatif)

---

### 📝 **İngilizce Örnek - Email Classification**

**Given:**
- 1200 emails tested
- 400 work, 800 personal
- Results:
  - 350 work emails correctly classified
  - 50 work emails misclassified as personal
  - 80 personal emails misclassified as work
  - 720 personal emails correctly classified

**Confusion Matrix:**
```
                Prediction
Actual      Work    Personal
Work        350     50
Personal    80      720
```

**Calculations:**
- TP = 350 (Work correctly classified)
- FP = 80 (Personal misclassified as work)
- TN = 720 (Personal correctly classified)
- FN = 50 (Work misclassified as personal)

### 📖 **Öklid Mesafesi (Euclidean Distance)**

**Formül:**
```
d(x⃗, y⃗) = √(∑ᵢ₌₁ⁿ (xᵢ - yᵢ)²)
```

**İngilizce Pratik Örnek:**
```
Doküman A: [1, 2, 3, 0, 1] (the, cat, sat, on, mat)
Doküman B: [2, 1, 3, 1, 0] (the, dog, sat, on, floor)

d(A,B) = √((1-2)² + (2-1)² + (3-3)² + (0-1)² + (1-0)²)
d(A,B) = √(1 + 1 + 0 + 1 + 1) = √4 = 2
```

**Türkçe Pratik Örnek:**
```
Doküman A: [2, 1, 0, 1, 1] (kedi, evde, uyuyor, çok, mutlu)
Doküman B: [1, 2, 1, 0, 1] (kedi, bahçede, oynuyor, çok, mutlu)

d(A,B) = √((2-1)² + (1-2)² + (0-1)² + (1-0)² + (1-1)²)
d(A,B) = √(1 + 1 + 1 + 1 + 0) = √4 = 2
```

### 📖 **Kosinüs Benzerliği (Cosine Similarity)**

**Formül:**
```
cos(θ) = (x⃗ · y⃗) / (||x⃗|| × ||y⃗||)
```

**İngilizce Pratik Örnek:**
```
Doküman A: [1, 2, 3, 0, 1] (the, cat, sat, on, mat)
Doküman B: [2, 1, 3, 1, 0] (the, dog, sat, on, floor)

A · B = 1×2 + 2×1 + 3×3 + 0×1 + 1×0 = 2 + 2 + 9 + 0 + 0 = 13
||A|| = √(1² + 2² + 3² + 0² + 1²) = √15
||B|| = √(2² + 1² + 3² + 1² + 0²) = √15

cos(θ) = 13 / (√15 × √15) = 13/15 ≈ 0.867
```

**Türkçe Pratik Örnek:**
```
Doküman A: [2, 1, 0, 1, 1] (kedi, evde, uyuyor, çok, mutlu)
Doküman B: [1, 2, 1, 0, 1] (kedi, bahçede, oynuyor, çok, mutlu)

A · B = 2×1 + 1×2 + 0×1 + 1×0 + 1×1 = 2 + 2 + 0 + 0 + 1 = 5
||A|| = √(2² + 1² + 0² + 1² + 1²) = √7
||B|| = √(1² + 2² + 1² + 0² + 1²) = √7

cos(θ) = 5 / (√7 × √7) = 5/7 ≈ 0.714
```

### ⚠️ **Farklar**
- **Öklid:** Mutlak mesafe, küçük değer = benzer
- **Kosinüs:** Açı benzerliği, büyük değer = benzer
- **Kosinüs:** Doküman uzunluğundan etkilenmez

### 📊 **Karşılaştırmalı Analiz:**

| Özellik | İngilizce | Türkçe |
|---------|-----------|--------|
| **Öklid Mesafesi** | 2.0 | 2.0 |
| **Kosinüs Benzerliği** | 0.867 | 0.714 |
| **Doküman Uzunluğu** | 5 kelime | 5 kelime |
| **Ortak Kelimeler** | 3 (the, sat, on) | 3 (kedi, çok, mutlu) |
| **Benzerlik Seviyesi** | Yüksek | Orta | 