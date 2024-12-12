import datetime
import os

class Not:
    def __init__(self, icerik, tarih=None):
        self.icerik = icerik
        self.tarih = tarih if tarih else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.tarih}] {self.icerik}"

class NotDefteri:
    def __init__(self):
        self.notlar = []

    def not_ekle(self, not_obj):
        self.notlar.append(not_obj)
        print("Not başarıyla eklendi.")

    def notlari_listele(self):
        if not self.notlar:
            print("Henüz hiç not eklenmedi.")
        else:
            print("Notlar:")
            for i, not_obj in enumerate(self.notlar, start=1):
                print(f"{i}. {not_obj}")

    def not_sil(self, index):
        if 0 <= index < len(self.notlar):
            silinen_not = self.notlar.pop(index)
            print(f"Not silindi: {silinen_not}")
        else:
            print("Geçersiz not numarası.")

    def notlari_kaydet(self, dosya_adi):
        try:
            with open(dosya_adi, 'w', encoding='utf-8') as dosya:
                for not_obj in self.notlar:
                    dosya.write(f"{not_obj}\n")
            print(f"Tüm notlar {dosya_adi} dosyasına kaydedildi.")
        except Exception as e:
            print(f"Hata: {e}")

    def notlari_yukle(self, dosya_adi):
        if not os.path.exists(dosya_adi):
            print(f"{dosya_adi} dosyası bulunamadı.")
            return
        try:
            with open(dosya_adi, 'r', encoding='utf-8') as dosya:
                self.notlar = []
                for satir in dosya:
                    tarih, icerik = satir.strip().split(']', 1)
                    self.notlar.append(Not(icerik=icerik.strip(), tarih=tarih[1:]))
            print(f"Notlar {dosya_adi} dosyasından yüklendi.")
        except Exception as e:
            print(f"Hata: {e}")

# Program Örneği
not_defteri = NotDefteri()

not_defteri.not_ekle(Not("İlk notum."))
not_defteri.not_ekle(Not("Python projeme devam etmeliyim."))
not_defteri.notlari_listele()

not_defteri.not_sil(0)
not_defteri.notlari_listele()

not_defteri.notlari_kaydet("notlar.txt")
not_defteri.notlari_yukle("notlar.txt")
not_defteri.notlari_listele()