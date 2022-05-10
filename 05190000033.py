ASGARI_UCRET = 2324.70  # Asgari ücret o ay  2324.70 TL olarak verilmiştir
ON = 10
YIRMI_BES_BIN = 25000
YUZDE_DORT = 0.04
YUZDE_ON = 0.1
IKI = 2
top_satilan_konut, top_kiralanan_konut = 0, 0   # Satılan ve kiralanan toplam konut sayıları
top_is_yeri_satilan, top_is_yeri_kiralanan = 0, 0  # Satılan ve kiralanan toplam iş yeri sayıları
top_arsa_satilan, top_arsa_kiralanan = 0, 0  # Satılan ve kiralanan toplam arsa sayıları
konut_bedel = 0  # Satılan konutların satış bedellerinin ortalaması
is_yeri_bedel = 0  # Satılan işyerlerinin satış bedellerinin ortalaması
arsa_bedel = 0  # Satılan arsaların satış bedellerinin ortalaması
max_satilan_bedel = 0  # O ay en yüksek bedelle satılan emlak satış bedeli
max_satilan_emlak_tipi = 0  # O ay en yüksek bedelle satılan emlak tipi
max_satis_yapan_ad = 0  # O ay en yüksek bedelle emlak satan danışmanın adı
max_konut_kira_bedel = 0  # O ay en yüksek bedelle kiralanan konutun kira bedeli
max_konut_kira_ad = 0  # O ay en yüksek bedelle konut kiralayan danışmanın adı
asgari_ucretten_fazla_sayi = 0  # O ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı
top_satis_yapamayan = 0  # O ay hiç satış yapamayan danışmanların sayısı
max_satis_adedi = 0  # Bir eleman tarafından yapılan max satış adedi
max_satis_bedeli_top = 0  # O ay satış bedeli olarak en çok satış yapan danışmanın satış bedeli toplamı
max_aded_satan_bedel = 0  # O ay satış adedi olarak en çok satış yapan danışmanın satış bedeli toplamı
max_aded_satan_ad = 0  # O ay satış adedi olarak en çok satış yapan danışman adı
max_aded_satan_topl = 0  # O ay satış adedi olarak en çok satış yapan danışmanın satış adedi
kotasini_dolduran_sayisi = 0
max_satis_bedel_ad = 0  # O ay satış bedeli olarak en çok satış yapan danışmanın adı
max_satis_bedel_aded = 0  # O ay satış bedeli olarak en çok satış yapan danışmanın satış adedi
primi_maasindan_yuksek_olanlar = 0
on_yirmi_bes = 0  # O ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı
danisman_prim = 0
max_prim = danisman_prim
min_prim = danisman_prim
max_prim_alan_ad = 0  # O ay en yüksek prim alan danışmanın adı
max_prim_alan_maas = 0  # O ay en yüksek prim alan danışmanın maaşı
max_prim_alan_ucret = 0  # O ay en yüksek prim alan danışmanın ücreti
min_prim_alan_ad = 0  # O ay en düşük primi alan danışmanın adı
min_prim_alan_maas = 0  # O ay en düşük primi alan danışmanın maaşı
min_prim_alan_ucret = 0  # O ay en düşük primi alan danışmanın ücreti
butun_ucret_toplam = 0  # O ay tüm emlak danışmanlarına ödenecek toplam ücretlerin toplamı
toplam_komisyon = 0  # O ay acentenin kazandığı toplam komisyon

# Emlak danışmanı sayısı alınır. Tam sayı girilmelidir
emlak_danismani_sayisi = int(input("Emlak acentesinde çalışan emlak çalışanı sayısını giriniz: "))
while emlak_danismani_sayisi <= 0:  # Emlak danışmanı sayısı sıfır veya sıfırdan küçük olamaz
    emlak_danismani_sayisi = int(input("Hatalı veri girişi, lütfen tekrar giriniz: "))
for danisman in range(0, emlak_danismani_sayisi):  # Döngü emlak danışmanı sayısı kadar döner

    danisman_satilan_aded = 0  # O ay sattığı emlak adedi
    danisman_kiralanan_aded = 0  # O ay kiralığı emlak adedi
    danisman_konut_satilan_bedel = 0  # Satılan konut toplam bedeli
    danisman_is_yeri_satilan_bedel = 0  # Satılan iş yeri toplam bedeli
    danisman_arsa_satilan_bedel = 0  # Satılan arsa toplam bedeli
    danisman_top_kira_bedel = 0  # Danışmanın aldığı toplam kira bedeli
    konut_kira_bed_top = 0  # Konutlar için aldığı toplam kira bedeli
    konut_kira_aded = 0  # Kiraladığı konutların adedi
    danisman_max_konut_kira_bedel = 0  # Max bedele kiraladığı konutun bedeli
    ikramiye = 0  # İkramiyesi
    satis_yapma_durumu = 0  # Satış yapıp yapamadığı
    top_arsa_satilan_bedel = 0  # Sattığı arsa bedellerinin toplamı
    top_is_yeri_satilan_bedel = 0  # Sattığı iş yeri bedellerinin toplamı
    top_konut_satilan_bedel = 0  # Sattiığı konutların bedellerinin toplamı
    danisman_komisyon = 0  # Danışmanın aldığı komisyon

    ad_soyad = input("Emlak danışmanının adını ve soyadını giriniz: ")


    maas = float(input("Emlak danışmanın aldığı maaşı giriniz (TL): "))
    while maas < ASGARI_UCRET:  # Maaş asgari ücretten düşük olamaz. Reel sayılar girilir
        maas = float(input("Hatalı veri girişi, lütfen tekrar giriniz: "))

    kota = float(input("Emlak danışmanın bir ayda kazandırması beklenen komisyon tutarı (TL): "))
    while kota < maas * ON:  # Kota maaşın on katından düşük olamaz. Reel sayılar girilir
        kota = float(input("Hatalı veri girişi, lütfen tekrar giriniz: "))  # İstenilen değer aralığında girilmezse hata mesajı döner

    devam = "e"
    while devam in ["e", "E"]:  # Devam etmek istenilen kadar döngü döner

        emlak_tipi = input("Kiralan ya da satılan yerin emlak tipini giriniz (K/k/İ/i/A/a karakterleri): ")
        while emlak_tipi not in ["k", "K", "i", "İ", "a", "A"]:  # Bu karakterler dışında girilirse hata mesajı döner
            emlak_tipi = input("Hatalı veri girişi, lütfen tekrar giriniz: ")

        islem_turu = input("Emlak tipine yapılan işlem türünü giriniz (S/s/K/k karakterleri): ")
        while islem_turu not in ["s", "S", "k", "K"]:  # Bu karakterler dışında girilirse hata mesajı döner
            islem_turu = input("Hatalı veri girişi, lütfen tekrar giriniz: ")

        satis_kira_bedeli = float(input("Satılan ya da kiralanan yerin bedelini giriniz (TL): "))
        while satis_kira_bedeli <= 0:  # Emlak bedeli sıfırdan küçük girilemez
            satis_kira_bedeli = float(input("Hatalı veri girişi, lütfen tekrar giriniz: "))  # İstenilen değer aralığında girilmezse hata mesajı döner

        if islem_turu in ["s", "S"]:  # Satış yapılan emlaklar için koşul ifadesi
            satis_yapma_durumu = True
            danisman_satilan_aded += 1
        else:  # Kiralanan emlaklar için koşul ifadesi
            danisman_kiralanan_aded += 1
            danisman_top_kira_bedel += satis_kira_bedeli

        if (emlak_tipi == "k" or emlak_tipi == "K") and (islem_turu == "s" or islem_turu == "S"):  # Satılan konutlar
            top_satilan_konut += 1
            danisman_konut_satilan_bedel += satis_kira_bedeli
            top_konut_satilan_bedel += satis_kira_bedeli
            konut_bedel += satis_kira_bedeli
        elif (emlak_tipi == "k" or emlak_tipi == "K") and (islem_turu == "k" or islem_turu == "K"):  # Kiralanan konutlar
            konut_kira_aded += 1
            top_kiralanan_konut += 1
            konut_kira_bed_top += satis_kira_bedeli
            if danisman_max_konut_kira_bedel < satis_kira_bedeli:  # Max bedele kiraladığı konutun bedeli bulmak için koşul
                danisman_max_konut_kira_bedel = satis_kira_bedeli
            if max_konut_kira_bedel < satis_kira_bedeli:  # O ay en yüksek bedelle kiralanan konutun kira bedeli bulmak için koşul
                max_konut_kira_bedel = satis_kira_bedeli
                max_konut_kira_ad = ad_soyad
            if satis_kira_bedeli > ASGARI_UCRET:  # # O ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı bulunur
                asgari_ucretten_fazla_sayi += 1

        elif (emlak_tipi == "i" or emlak_tipi == "İ") and (islem_turu == "s" or islem_turu == "S"):  # Satılan iş yeri
            top_is_yeri_satilan += 1
            danisman_is_yeri_satilan_bedel += satis_kira_bedeli
            top_is_yeri_satilan_bedel += satis_kira_bedeli
            is_yeri_bedel += satis_kira_bedeli
        elif (emlak_tipi == "i" or emlak_tipi == "İ") and (islem_turu == "k" or islem_turu == "K"):  # Kiralanan iş yeri
            top_is_yeri_kiralanan += 1

        elif (emlak_tipi == "a" or emlak_tipi == "A") and (islem_turu == "s" or islem_turu == "S"):  # Satılan arsa
            top_arsa_satilan += 1
            danisman_arsa_satilan_bedel += satis_kira_bedeli
            top_arsa_satilan_bedel += satis_kira_bedeli
            arsa_bedel += satis_kira_bedeli
        else:  # Kiralanan arsa
            top_arsa_kiralanan += 1

        if islem_turu in ["s", "S"] and max_satilan_bedel < satis_kira_bedeli:  # Satılanlar arasında max bedelle satılan bulunur
            max_satilan_bedel = satis_kira_bedeli
            max_satis_yapan_ad = ad_soyad
            if emlak_tipi in ["k", "K"]:
                max_satilan_emlak_tipi = "konuttur."
            elif emlak_tipi in ["i", "İ"]:
                max_satilan_emlak_tipi = "iş yeridir."
            else:
                max_satilan_emlak_tipi = "arsadır."

        devam = input("Girilecek başka emlak olup olmadığını giriniz (E/e/H/h karakterleri): ")
        while devam not in ["e", "E", "h", "H"]:  # Bu karakterler dışında girilirse hata mesajı döner
            devam = input("Hatalı veri girişi, lütfen tekrar giriniz: ")

    if not satis_yapma_durumu:  # Satış yapamayan danışman sayısı bulunur
        top_satis_yapamayan += 1

    toplam_satilan_bedel = top_arsa_satilan_bedel+top_is_yeri_satilan_bedel+top_konut_satilan_bedel

    if max_satis_adedi < danisman_satilan_aded:  # # O ay satış adedi olarak en çok satış yapan danışman için girilecek koşul
        max_satis_adedi = danisman_satilan_aded
        max_aded_satan_ad = ad_soyad
        max_aded_satan_topl = danisman_satilan_aded
        max_aded_satan_bedel = toplam_satilan_bedel

    if max_satis_bedeli_top < toplam_satilan_bedel:  # O ay satış bedeli olarak en çok satış yapan danışman için girilecek koşul
        max_satis_bedeli_top = toplam_satilan_bedel
        max_satis_bedel_ad = ad_soyad
        max_satis_bedel_aded = danisman_satilan_aded

    if danisman_kiralanan_aded >= ON or danisman_top_kira_bedel >= YIRMI_BES_BIN:
        on_yirmi_bes += 1


    # Bir danışman için hesaplanacak oranlar, ortalamalar, komisyon ve prim
    danisman_satilan_oran = (danisman_satilan_aded / (danisman_kiralanan_aded + danisman_satilan_aded)) * 100
    danisman_kiralanan_oran = (danisman_kiralanan_aded / (danisman_satilan_aded + danisman_kiralanan_aded)) * 100
    danisman_konut_kira_bedel_ort = konut_kira_bed_top / konut_kira_aded
    danisman_komisyon = (danisman_konut_satilan_bedel+danisman_is_yeri_satilan_bedel+danisman_arsa_satilan_bedel) * YUZDE_DORT + danisman_top_kira_bedel
    danisman_prim = danisman_komisyon * YUZDE_ON

    if danisman_prim > maas:
        primi_maasindan_yuksek_olanlar += 1



    # Bir danışmandan sonra yazılacaklar
    print("Danişmanın adı soyadı: {}".format(ad_soyad))
    print("O ay sattığı emlak adedi: {} ve oranı: %{:.2f}".format(danisman_satilan_aded, danisman_satilan_oran))
    print("O ay kiralığı emlak adedi: {} ve oranı: %{:.2f}".format(danisman_kiralanan_aded, danisman_kiralanan_oran))
    print("Satılan konut toplam bedeli: {:,.2f}TL".format(danisman_konut_satilan_bedel))
    print("Satılan iş yeri toplam bedeli: {:,.2f}TL".format(danisman_is_yeri_satilan_bedel))
    print("Satılan arsa toplam bedeli: {:,.2f}TL".format(danisman_arsa_satilan_bedel))
    print("O ay kiraladığı konutların ortalama kira bedeli: {:,.2f}TL".format(danisman_konut_kira_bedel_ort))
    print("O ay en yüksek bedelle kiraladığı konutun kira bedeli: {:,.2f}TL".format(danisman_max_konut_kira_bedel))
    print("O ay maaşı: {:,.2f}TL".format(maas))
    print("O ay primi: {:,.2f}TL".format(danisman_prim))
    print("O ay kotası: {:,.2f}TL".format(kota))
    print("O ay acenteye kazandırdığı toplam komisyon tutarı: {:,.2f}TL".format(danisman_komisyon))

    if kota <= danisman_komisyon:
        kotasini_dolduran_sayisi += 1
        print("Kotasını doldurmuştur.")
        ikramiye = ASGARI_UCRET/IKI
        print("Kotayı doldurduğu için o ay alacağı ikramiye: {:,.2f}TL".format(ikramiye))
    else:
        print("Kotasını dolduramamıştır. İkramiye almayacaktır.")

    toplam_ucret = maas+danisman_prim+ikramiye
    print("O ay toplam ücreti: {:,.2f}TL".format(toplam_ucret))
    butun_ucret_toplam += toplam_ucret
    toplam_komisyon += danisman_komisyon

    if max_prim < danisman_prim:
        max_prim = danisman_prim
        max_prim_alan_ad = ad_soyad
        max_prim_alan_maas = maas
        max_prim_alan_ucret = toplam_ucret

    if min_prim == 0:
        min_prim = danisman_prim+1
    if min_prim > danisman_prim:
        min_prim = danisman_prim
        min_prim_alan_ad = ad_soyad
        min_prim_alan_maas = maas
        min_prim_alan_ucret = toplam_ucret

# Bütün istastistiksel bilgilerin hesaplanması
# Oranlar, ortalamalar
konut_satilan_oran = (top_satilan_konut/(top_satilan_konut+top_kiralanan_konut))*100
is_yeri_satilan_oran = (top_is_yeri_satilan/(top_is_yeri_kiralanan + top_is_yeri_satilan))*100
arsa_satilan_oran = (top_arsa_satilan/(top_arsa_kiralanan+top_arsa_satilan))*100
konut_satilan_bedel_ort = konut_bedel/top_satilan_konut
is_yeri_satilan_bedel_ort = is_yeri_bedel/top_is_yeri_satilan
arsa_satilan_bedel_ort = arsa_bedel/top_arsa_satilan
asgari_ucret_fazla_oran = (asgari_ucretten_fazla_sayi/top_kiralanan_konut)*100
satis_yapamayan_oran = (top_satis_yapamayan/emlak_danismani_sayisi)*100
kotasini_dolduran_oran = (kotasini_dolduran_sayisi/emlak_danismani_sayisi)*100
primi_yuksek_oran = (primi_maasindan_yuksek_olanlar/emlak_danismani_sayisi)*100
butun_ucret_ort = butun_ucret_toplam/emlak_danismani_sayisi

# Bütün danışmanlardan sonra gelecek çıktılar
print("Satılan konut sayısı: {}, kiralanan konut sayısı: {} ve  konut sayısının satılma oranı: %{:.2f}".format(top_satilan_konut, top_kiralanan_konut, konut_satilan_oran))
print("Satılan işyeri sayısı: {}, kiralanan işyeri sayısı: {} ve iş yeri sayısının satılma oranı: %{:.2f}".format(top_is_yeri_satilan, top_is_yeri_kiralanan, is_yeri_satilan_oran))
print("Satılan arsa sayısı: {}, kiralanan arsa sayısı: {} ve arsa sayısının satılma oranı: %{:.2f}".format(top_arsa_satilan, top_arsa_kiralanan, arsa_satilan_oran))
print("Satılan konutların satış bedellerinin toplamı: {:,.2f}TL, ortalaması: {:,.2f}TL".format(konut_bedel, konut_satilan_bedel_ort))
print("Satılan işyerlerinin satış bedellerinin toplamı: {:,.2f}TL, ortalaması: {:,.2f}TL".format(is_yeri_bedel, is_yeri_satilan_bedel_ort))
print("Satılan arsaların satış bedellerinin toplamı: {:,.2f}TL, ortalaması: {:,.2f}TL".format(arsa_bedel, arsa_satilan_bedel_ort))
print("O ay en yüksek bedelle satılan emlak tipi {}, satış bedeli: {:,.2f}TL, satışı yapan danışman adı soyadı: {} ".format(max_satilan_emlak_tipi, max_satilan_bedel, max_satis_yapan_ad))
print("O ay en yüksek bedelle kiralanan konutun kira bedeli: {:,.2f}TL, kiralayan danışmanın adı soyadı: {}".format(max_konut_kira_bedel, max_konut_kira_ad))
print("O ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı: {}, kiralanan konutlar içindeki oranı: %{:.2f}".format(asgari_ucretten_fazla_sayi, asgari_ucret_fazla_oran))
print("O ay hiç satış yapamayan danışmanların sayısı: {}, tüm danışmanlar içindeki oranı: %{:.2f}".format(top_satis_yapamayan, satis_yapamayan_oran))
print("O ay satış adedi olarak en çok satış yapan danışman adı: {}, sattığı emlak sayısı: {} toplam satış bedeli: {:,.2f}TL".format(max_aded_satan_ad, max_aded_satan_topl, max_aded_satan_bedel))
print("O ay satış bedeli olarak en çok satış yapan danışman adı: {}  sattığı emlak sayısı: {} toplam satış bedeli: {:,.2f}TL".format(max_satis_bedel_ad, max_satis_bedel_aded, max_satis_bedeli_top))
print("O ay kotasını dolduran danışmanların sayısı: {}, tüm danışmanlar içindeki oranı: %{:.2f}".format(kotasini_dolduran_sayisi, kotasini_dolduran_oran))
print("O ay primi maaşından yüksek olan danışmanların sayısı: {}, tüm danışmanlar içindeki oranı: %{:.2f}".format(primi_maasindan_yuksek_olanlar, primi_yuksek_oran))
print("O ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı: {}".format(on_yirmi_bes))
print("O ay en yüksek prim alan danışmanın adı: {},  maaşı: {:,.2f}TL, primi: {:,.2f}TL, aylık toplam ücreti: {:,.2f}TL".format(max_prim_alan_ad, max_prim_alan_maas, max_prim, max_prim_alan_ucret))
print("O ay en düşük prim alan danışmanın adı: {}, maaşı: {:,.2f}TL, primi: {:,.2f}TL, aylık toplam ücreti: {:,.2f}TL".format(min_prim_alan_ad, min_prim_alan_maas, min_prim, min_prim_alan_ucret))
print("O ay tüm emlak danışmanlarına ödenecek toplam ücretlerin toplamı: {:,.2f}TL, ortalaması: {:,.2f}TL".format(butun_ucret_toplam, butun_ucret_ort))
print("O ay acentenin kazandığı toplam komisyon: {:,.2f}TL".format(toplam_komisyon))
