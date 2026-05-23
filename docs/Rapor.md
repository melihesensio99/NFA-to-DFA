# NFA'dan DFA'ya Dönüşüm (Subset Construction) Raporu

**Ders:** Python Programlamaya Giriş / Otomata Teorisi
**Öğrenci:** Melih Esen
**Öğrenci No:** 2210656013

Bu raporda, NFA'dan DFA'ya geçişi sağlayan "Subset Construction" (Alt Küme İnşası) algoritmasının Python ile nasıl implemente edildiği anlatılmaktadır. Kurallara uygun olarak kod içi yorumlar haricinde, genel tasarım kararlarını buraya da ekliyorum.

## 1. Veri Yapıları ve Ders Kavramları

Algoritmanın temelinde Python'un dahili veri yapılarını otomata kuramındaki matematiksel karşılıklarına eşleştirdim:
- **Kümeler (Sets):** DFA'daki bir durum, NFA'daki birden fazla durumun alt kümesinden oluştuğu için `set` veri tipini kullandım. İçindeki verilerin tekrar etmemesi büyük avantaj sağladı.
- **Dondurulmuş Kümeler (Frozenset):** Python'da standart `set`'ler değiştirilebilir (mutable) oldukları için Sözlük (Dictionary) anahtarı yapılamazlar. Bu yüzden her alt kümeyi tabloya kaydederken Hash'lenebilen bir yapı olan `frozenset` kullandım.
- **Sözlükler (Dictionaries):** Geçiş tablosunu (Transition Table) modellemek için iç içe dictionary yapıları kullandım. Örn: `gecis_tablosu['q0']['1']`

## 2. Tasarım Kararları ve Algoritma

1. **Epsilon Kapanışı (Epsilon Closure):** NFA'da sadece ε (epsilon) ile gidilebilen her yeri bulan bir "DFS" (Derinlik Öncelikli Arama) yazarak işe başladım. Döngü sırasında kuyruktan eleman çekip kapanış tablosuna ekliyorum.
2. **Alt Küme İnşası:** Sıfırdan oluşturduğum islem kuyruğu (Breadth First Search - BFS mantığı) ile keşfettiğim yepyeni DFA düğümlerini geziyorum. Döngü bittiğinde yeni NFA alt kümeleri bulunamaz hale geliyor ve DFA tablom tamamlanıyor.
3. **Dead States (Ölü Durumlar):** Eğer otomata, o harf için hiçbir yere gidemiyorsa kod içerisinde boş kümeye düşüyor. Bunu tabloda saklayıp RAM israfı yapmak yerine test fonksiyonunda "eğer gidilecek yer yoksa direkt False (Reject) döndür" şeklinde sadeleştirdim.

## 3. Test Senaryoları ve Analizi

Kod içinde bulunan `tests_senaryolari` dizisi 5 farklı senaryo içerir. Otomatamız **sonu 11 ile bitenleri** kabul edecek şekilde tasarlandığı için test sonuçları şu şekilde oluşmuştur:

- **0011 (Normal):** KABUL (Accept). Doğru bir şekilde sonlandığı için çalışıyor.
- **01010 (Normal):** RED (Reject). 11 ile bitmediği için doğru olarak reddedildi.
- **11 (Boundary - Sınır):** KABUL. Alabileceği en kısa doğru metin. Başarıyla testten geçti.
- **"" (Boundary - Sınır):** RED. Boş metin girilmesi halinde sistem çökmedi, normal olarak reddedip devam etti.
- **0000a (Error - Hata):** RED. Normalde 'a' harfi alfabede yok. Program çökmek yerine bunu ölü duruma atıp reddetti (Dead State) ve hata güvenliği sağlandı.

Tüm kodlar PEP 8 kurallarına (snake_case, 120 satır uzunluğu, 4 boşluk girintisi) uygun olarak geliştirilmiştir.
