class Kullanici:
    def __init__(self, ad, hesap_numarasi, bakiye=0):
        self.ad = ad
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz miktar!")

    def para_cek(self, miktar):
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye veya geçersiz miktar!")

    def bakiye_goster(self):
        print(f"Hesap Bakiyesi: {self.bakiye} TL")


class Banka:
    def __init__(self):
        self.kullanicilar = {}

    def hesap_olustur(self, ad, hesap_numarasi, baslangic_bakiyesi=0):
        if hesap_numarasi in self.kullanicilar:
            print("Bu hesap numarası zaten kullanılıyor!")
        else:
            yeni_kullanici = Kullanici(ad, hesap_numarasi, baslangic_bakiyesi)
            self.kullanicilar[hesap_numarasi] = yeni_kullanici
            print(f"Hesap oluşturuldu: {ad}, Hesap No: {hesap_numarasi}, Başlangıç Bakiyesi: {baslangic_bakiyesi} TL")

    def kullanici_giris(self, hesap_numarasi):
        return self.kullanicilar.get(hesap_numarasi, None)


def main():
    banka = Banka()

    while True:
        print("\n1. Hesap Oluştur")
        print("2. Giriş Yap ve İşlem Yap")
        print("3. Çıkış")
        
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ad = input("Adınızı girin: ")
            hesap_numarasi = input("Hesap numarası oluşturun: ")
            try:
                baslangic_bakiyesi = float(input("Başlangıç bakiyesini girin: "))
                banka.hesap_olustur(ad, hesap_numarasi, baslangic_bakiyesi)
            except ValueError:
                print("Lütfen geçerli bir miktar girin!")
        elif secim == "2":
            hesap_numarasi = input("Hesap numaranızı girin: ")
            kullanici = banka.kullanici_giris(hesap_numarasi)
            
            if kullanici:
                while True:
                    print("\n1. Para Yatır")
                    print("2. Para Çek")
                    print("3. Bakiye Sorgula")
                    print("4. Ana Menüye Dön")

                    alt_secim = input("Seçiminizi yapın: ")

                    if alt_secim == "1":
                        try:
                            miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
                            kullanici.para_yatir(miktar)
                        except ValueError:
                            print("Lütfen geçerli bir miktar girin!")
                    elif alt_secim == "2":
                        try:
                            miktar = float(input("Çekmek istediğiniz miktarı girin: "))
                            kullanici.para_cek(miktar)
                        except ValueError:
                            print("Lütfen geçerli bir miktar girin!")
                    elif alt_secim == "3":
                        kullanici.bakiye_goster()
                    elif alt_secim == "4":
                        break
                    else:
                        print("Geçersiz seçim!")
            else:
                print("Hesap bulunamadı!")
        elif secim == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()