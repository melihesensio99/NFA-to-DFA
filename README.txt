=================================================
Ders: Python Programlamaya Giriş
Öğrenci: Melih Esen
Numara: 2210656013
Ödev No: 3
Tarih: 23.05.2026
=================================================

PYTHON SÜRÜMÜ:
  Python 3.8 veya üzeri (Önerilen: Python 3.10+)

GEREKLİ KÜTÜPHANELER:
  Standart kütüphane dışında bir bağımlılığa gerek yoktur. Üçüncü parti kütüphane (pip install gerektiren) kullanılmamıştır. Sadece Python kurulumu yeterlidir.

ÇALIŞTIRMA KOMUTU:
  Terminal veya komut satırını README.txt dosyasının bulunduğu dizinde açarak şu komutu çalıştırınız:
  python src/main.py

ÖRNEK KULLANIM:
  1. Terminali açın ve projenin kök klasörüne gidin.
  2. "python src/main.py" yazın.
  3. Ekranda Otomata Teorisindeki Subset Construction mantığına göre NFA'nın DFA'ya dönüştürüldüğünü, oluşan geçiş tablosunu (transition table) göreceksiniz.
  4. Alt kısımda istenen 5 farklı test senaryosunun (Normal, Boundary, Error) otomata üzerindeki "KABUL" veya "RED" sonuçları listelenecektir.

BİLİNEN SORUNLAR (varsa):
  - Kod tamamen doğru çalışmaktadır ve PEP 8 kurallarına (snake_case değişkenler vb.) uygun yazılmıştır.
  - Sadece Ölü Durumlara (Dead States) geçişler gereksiz bellek kaplamaması için bilerek geçiş tablosuna eklenmemiş, fonksiyonda "yoksa direkt Reddet" olarak kodlanmıştır. Bu bilinen bir tercih kararıdır.
