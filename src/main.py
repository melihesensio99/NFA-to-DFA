# =================================================
# Ders: Python Programlamaya Giriş
# Öğrenci: Melih Esen
# Numara: 2210656013
# Ödev No: 3
# Tarih: 23.05.2026
#
# Açıklama: NFA (Non-deterministic Finite Automaton) 
# modelini DFA'ya (Deterministic Finite Automaton) dönüştüren 
# Python aracı.
#
# Hatırlatılan Ders Kavramları:
#  - Otomata Teorisi: Subset Construction algoritması, 
#    epsilon kapanışı (closure) hesaplama ve Ölü Durum (Dead State).
#  - Veri Yapıları: Tabloları modellemek için Dictionary (Sözlük), 
#    tekrarsız durum kümesi için Set (Küme) ve dictionary 
#    anahtarı yapabilmek için 'frozenset' kullanılmıştır.
# =================================================

def epsilon_kapanisi_al(durumlar, gecis_tablosu):
    """
    Verilen durumların Epsilon ('e') geçişleriyle gidebileceği 
    tüm durumların kümesini (closure) döndürür.
    """
    kapanis = set(durumlar)
    yigin = list(durumlar)
    
    # DFS (Depth First Search) mantığıyla tüm epsilon yollarını geziyoruz
    while yigin:
        su_anki_durum = yigin.pop()
        
        # Eğer bu durumdan epsilon ('e') geçişi varsa 
        if su_anki_durum in gecis_tablosu and 'e' in gecis_tablosu[su_anki_durum]:
            gidecegi_yerler = gecis_tablosu[su_anki_durum]['e']
            for d in gidecegi_yerler:
                if d not in kapanis:
                    kapanis.add(d)
                    yigin.append(d)
                    
    return kapanis


def nfa_den_dfaya_cevir(alfabe, gecis_tablosu, baslangic, kabul_durumlari):
    """
    Subset Construction algoritmasını kullanarak NFA'yı DFA'ya çevirir.
    Python 'frozenset' yapısı sayesinde kümeleri sözlük anahtarı (key) 
    olarak kullanabiliyoruz.
    """
    dfa_gecisleri = {}
    dfa_kabul_durumlari = []
    
    # Başlangıç durumu, NFA başlangıcının epsilon kapanışıdır
    dfa_baslangic = frozenset(epsilon_kapanisi_al({baslangic}, gecis_tablosu))
    
    # Henüz işlenmemiş yeni durumları tuttuğumuz kuyruk (BFS - Breadth First Search)
    islem_kuyrugu = [dfa_baslangic]
    islenen_dfa_durumlari = []
    
    while islem_kuyrugu:
        su_anki_dfa_durumu = islem_kuyrugu.pop(0)
        
        if su_anki_dfa_durumu in islenen_dfa_durumlari:
            continue
            
        islenen_dfa_durumlari.append(su_anki_dfa_durumu)
        dfa_gecisleri[su_anki_dfa_durumu] = {}
        
        # Eğer bu yeni DFA durumunun alt kümelerinden biri NFA'nın kabul durumlarından 
        # biriyse, o zaman bu DFA durumu da komple kabul durumu olur.
        for nfa_durumu in su_anki_dfa_durumu:
            if nfa_durumu in kabul_durumlari:
                if su_anki_dfa_durumu not in dfa_kabul_durumlari:
                    dfa_kabul_durumlari.append(su_anki_dfa_durumu)
                break
                
        # Her bir alfabe harfi için (örneğin 0 ve 1) yeni durumlar türetiyoruz
        for harf in alfabe:
            hedef_durumlar = set()
            for nfa_d in su_anki_dfa_durumu:
                # Tabloda böyle bir geçiş var mı diye kontrol et (KeyError almamak için)
                if nfa_d in gecis_tablosu and harf in gecis_tablosu[nfa_d]:
                    for hedef in gecis_tablosu[nfa_d][harf]:
                        hedef_durumlar.add(hedef)
            
            # Gidilecek hedeflerin de epsilon kapanışını alarak tam durumu buluyoruz
            yeni_dfa_durumu = frozenset(epsilon_kapanisi_al(hedef_durumlar, gecis_tablosu))
            
            # Boş küme değilse geçiş tablosuna yazıyoruz (boş kümeler dead-state olur)
            dfa_gecisleri[su_anki_dfa_durumu][harf] = yeni_dfa_durumu
            
            # Yepyeni bir durum keşfettiysek işlem kuyruğuna atalım
            if yeni_dfa_durumu not in islenen_dfa_durumlari and yeni_dfa_durumu not in islem_kuyrugu:
                if len(yeni_dfa_durumu) > 0:
                    islem_kuyrugu.append(yeni_dfa_durumu)
                
    return dfa_baslangic, dfa_gecisleri, dfa_kabul_durumlari


def metin_test_et(metin, dfa_baslangic, dfa_gecisleri, dfa_kabul_durumlari):
    """
    Oluşturulan DFA üzerinde verilen string metnin otomat tarafından
    kabul (Accept) veya red (Reject) edileceğini test eder.
    """
    su_anki_durum = dfa_baslangic
    
    for harf in metin:
        # Eğer harf için gidilecek bir yol yoksa (Ölü Durum / Dead State) reddet.
        if su_anki_durum not in dfa_gecisleri or harf not in dfa_gecisleri[su_anki_durum]:
            return False
        
        yeni_durum = dfa_gecisleri[su_anki_durum][harf]
        
        # Boş kümeye düştüysek yine Dead State içindeyiz demektir.
        if len(yeni_durum) == 0:
            return False
            
        su_anki_durum = yeni_durum
        
    # Tüm harfler bittiğinde ulaştığımız durum kabul durumlarından biri mi?
    return su_anki_durum in dfa_kabul_durumlari


if __name__ == '__main__':
    # ---------------------------------------------------------
    # ÖRNEK NFA: Sonu "11" ile biten tüm ikili (binary) stringleri 
    # tanıyan otomatın tanımı. 
    # ---------------------------------------------------------
    
    alfabe_listesi = ['0', '1']
    baslangic = 'q0'
    kabul_edilenler = {'q2'}
    
    # NFA Geçiş Tablosu (Sözlükler iç içe kullanıldı)
    nfa_tablosu = {
        'q0': {'0': ['q0'], '1': ['q0', 'q1']},
        'q1': {'1': ['q2']},
        'q2': {} # q2'den hiçbir yere gidilmiyor
    }
    
    print("=================================================")
    print(" NFA'dan DFA'ya Alt Küme (Subset) Dönüşümü")
    print("=================================================")
    
    d_baslangic, d_gecisleri, d_kabuller = nfa_den_dfaya_cevir(
        alfabe_listesi, nfa_tablosu, baslangic, kabul_edilenler
    )
    
    print(f"\n[+] DFA Başlangıç Durumu: {set(d_baslangic)}")
    
    print("\n[+] DFA Kabul Durumları:")
    for k in d_kabuller:
        print(f"  --> {set(k)}")
        
    print("\n[+] Üretilen DFA Geçiş Tablosu (Transition Table):")
    for durum, harf_gecisleri in d_gecisleri.items():
        if len(durum) > 0:
            for harf, hedef in harf_gecisleri.items():
                if len(hedef) > 0:
                    print(f"  {set(durum)} --( {harf} )--> {set(hedef)}")
                
    # ---------------------------------------------------------
    # TEST SENARYOLARI (En az 5 adet ve 3 farklı tür)
    # ---------------------------------------------------------
    print("\n=================================================")
    print(" Otomata Test Senaryoları (Sonu 11 ile bitenler)")
    print("=================================================\n")
    
    testler = [
        ("0011", "Normal Durum - Sonu 11 ile biten doğru metin"),
        ("01010", "Normal Durum - Sonu 11 ile bitmeyen metin"),
        ("11", "Sınır Durumu (Boundary) - Kabul edilecek en kısa string"),
        ("", "Sınır Durumu (Boundary) - Tamamen boş string"),
        ("0000a", "Hata Durumu (Error Case) - Alfabede tanımlı olmayan harf (a) içeriyor")
    ]
    
    for i, (girdi_metni, aciklama) in enumerate(testler, 1):
        sonuc = metin_test_et(girdi_metni, d_baslangic, d_gecisleri, d_kabuller)
        durum_yazisi = "KABUL (Accept)" if sonuc else "RED (Reject)  "
        print(f"Test {i}: Metin: '{girdi_metni}'")
        print(f"Sonuç : {durum_yazisi}")
        print(f"Bilgi : {aciklama}")
        print("-" * 50)
