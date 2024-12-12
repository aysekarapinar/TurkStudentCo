class Urun:
    def __init__(self, ad, fiyat, miktar):
        self.ad = ad
        self.fiyat = fiyat
        self.miktar = miktar

    def __str__(self):
        return f"{self.ad} - Fiyat: {self.fiyat} TL, Miktar: {self.miktar}"

class Sepet:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, urun):
        if urun.ad in self.urunler:
            self.urunler[urun.ad].miktar += urun.miktar
            print(f"{urun.ad} sepetinize güncellendi. Yeni miktar: {self.urunler[urun.ad].miktar}")
        else:
            self.urunler[urun.ad] = urun
            print(f"{urun.ad} sepetinize eklendi.")

    def sepeti_listele(self):
        if not self.urunler:
            print("Sepetinizde hiç ürün yok.")
        else:
            print("Sepetinizdeki ürünler:")
            for urun in self.urunler.values():
                print(urun)

    def urun_cikar(self, urun_adi, miktar):
        if urun_adi in self.urunler:
            urun = self.urunler[urun_adi]
            if urun.miktar > miktar:
                urun.miktar -= miktar
                print(f"{urun_adi} sepetinizden çıkarıldı. Kalan miktar: {urun.miktar}")
            elif urun.miktar == miktar:
                del self.urunler[urun_adi]
                print(f"{urun_adi} tamamen sepetinizden çıkarıldı.")
            else:
                print(f"{urun_adi} için sepetinizde yeterli miktar yok.")
        else:
            print(f"{urun_adi} sepetinizde bulunmuyor.")

    def toplam_tutar(self):
        toplam = sum(urun.fiyat * urun.miktar for urun in self.urunler.values())
        print(f"Toplam tutar: {toplam} TL")
        return toplam

# Program Örneği
sepet = Sepet()

urun1 = Urun("Elma", 10, 3)
urun2 = Urun("Portakal", 12, 2)
urun3 = Urun("Muz", 15, 5)

sepet.urun_ekle(urun1)
sepet.urun_ekle(urun2)
sepet.urun_ekle(urun3)

sepet.sepeti_listele()
sepet.toplam_tutar()

sepet.urun_cikar("Elma", 2)
sepet.sepeti_listele()
sepet.toplam_tutar()

sepet.urun_cikar("Portakal", 2)
sepet.sepeti_listele()
sepet.toplam_tutar()
