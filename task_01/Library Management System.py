class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar
        self.odunc_alindi = False

    def __str__(self):
        durum = "Ödünçte" if self.odunc_alindi else "Mevcut"
        return f"Kitap: {self.ad}, Yazar: {self.yazar}, Durum: {durum}"

class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.odunc_alinan_kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap.ad} kütüphaneye eklendi.")

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("Kütüphanede hiç kitap yok.")
        else:
            print("Kütüphanedeki kitaplar:")
            for kitap in self.kitaplar:
                print(kitap)

    def kitap_odunc_ver(self, kitap_adi):
        for kitap in self.kitaplar:
            if kitap.ad == kitap_adi:
                if not kitap.odunc_alindi:
                    kitap.odunc_alindi = True
                    self.odunc_alinan_kitaplar.append(kitap)
                    print(f"{kitap.ad} kitabı ödünç verildi.")
                    return
                else:
                    print(f"{kitap.ad} kitabı zaten ödünçte.")
                    return
        print(f"{kitap_adi} adında bir kitap bulunamadı.")

    def kitap_geri_al(self, kitap_adi):
        for kitap in self.odunc_alinan_kitaplar:
            if kitap.ad == kitap_adi:
                kitap.odunc_alindi = False
                self.odunc_alinan_kitaplar.remove(kitap)
                print(f"{kitap.ad} kitabı geri alındı.")
                return
        print(f"{kitap_adi} adında ödünçte olan bir kitap bulunamadı.")

    def odunc_alinan_kitaplari_listele(self):
        if not self.odunc_alinan_kitaplar:
            print("Ödünçte olan hiç kitap yok.")
        else:
            print("Ödünçte olan kitaplar:")
            for kitap in self.odunc_alinan_kitaplar:
                print(kitap)

# Program Örneği
kutuphane = Kutuphane()

kitap1 = Kitap("Sırfın Simyacısı", "Paulo Coelho")
kitap2 = Kitap("1984", "George Orwell")
kitap3 = Kitap("Dönüşüm", "Franz Kafka")

kutuphane.kitap_ekle(kitap1)
kutuphane.kitap_ekle(kitap2)
kutuphane.kitap_ekle(kitap3)

kutuphane.kitaplari_listele()
kutuphane.kitap_odunc_ver("1984")
kutuphane.kitap_odunc_ver("Sırfın Simyacısı")

kutuphane.odunc_alinan_kitaplari_listele()

kutuphane.kitap_geri_al("1984")
kutuphane.odunc_alinan_kitaplari_listele()
kutuphane.kitaplari_listele()
