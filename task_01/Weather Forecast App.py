class Sehir:
    def __init__(self, ad, sicaklik):
        self.ad = ad
        self.sicaklik = sicaklik

    def __str__(self):
        return f"{self.ad}: {self.sicaklik}°C"

class HavaDurumu:
    def __init__(self):
        self.sehirler = {}

    def sehir_ekle(self, sehir):
        if sehir.ad in self.sehirler:
            print(f"{sehir.ad} zaten listede mevcut.")
        else:
            self.sehirler[sehir.ad] = sehir
            print(f"{sehir.ad} listeye eklendi.")

    def sicaklik_guncelle(self, sehir_adi, yeni_sicaklik):
        if sehir_adi in self.sehirler:
            self.sehirler[sehir_adi].sicaklik = yeni_sicaklik
            print(f"{sehir_adi} şehrinin sıcaklığı {yeni_sicaklik}°C olarak güncellendi.")
        else:
            print(f"{sehir_adi} listede bulunamadı.")

    def hava_durumu_sorgula(self, sehir_adi):
        if sehir_adi in self.sehirler:
            sehir = self.sehirler[sehir_adi]
            print(f"{sehir.ad} şehrinin sıcaklığı: {sehir.sicaklik}°C")
            self.tavsiye_ver(sehir.sicaklik)
        else:
            print(f"{sehir_adi} listede bulunamadı.")

    def tavsiye_ver(self, sicaklik):
        if sicaklik < 0:
            print("Soğuk, sıkı giyinin.")
        elif 0 <= sicaklik <= 15:
            print("Serin, mont almayı unutmayın.")
        else:
            print("Hava güzel, rahat giyin.")

# Program Örneği
hava_durumu = HavaDurumu()

sehir1 = Sehir("Ankara", 10)
sehir2 = Sehir("Istanbul", 18)
sehir3 = Sehir("Erzurum", -5)

hava_durumu.sehir_ekle(sehir1)
hava_durumu.sehir_ekle(sehir2)
hava_durumu.sehir_ekle(sehir3)

hava_durumu.hava_durumu_sorgula("Ankara")
hava_durumu.hava_durumu_sorgula("Istanbul")
hava_durumu.hava_durumu_sorgula("Erzurum")

hava_durumu.sicaklik_guncelle("Ankara", 5)
hava_durumu.hava_durumu_sorgula("Ankara")