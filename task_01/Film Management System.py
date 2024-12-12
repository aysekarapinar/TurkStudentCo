class Film:
    def __init__(self, ad, yonetmen, yil, tur):
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil
        self.tur = tur

    def __str__(self):
        return f"{self.ad} ({self.yil}) - Yönetmen: {self.yonetmen}, Tür: {self.tur}"

class FilmYoneticisi:
    def __init__(self):
        self.filmler = []

    def film_ekle(self, film):
        self.filmler.append(film)
        print(f"{film.ad} filmi başarıyla eklendi.")

    def film_sil(self, film_adi):
        for film in self.filmler:
            if film.ad == film_adi:
                self.filmler.remove(film)
                print(f"{film_adi} filmi başarıyla silindi.")
                return
        print(f"{film_adi} isimli film bulunamadı.")

    def filmleri_listele(self, filtre=None):
        if not self.filmler:
            print("Henüz hiçbir film eklenmedi.")
            return

        if filtre is None:
            print("Tüm Filmler:")
            for film in self.filmler:
                print(film)
        elif isinstance(filtre, str):  # Tür bazlı filtreleme
            print(f"Tür: {filtre} olan filmler:")
            for film in self.filmler:
                if film.tur.lower() == filtre.lower():
                    print(film)
        elif isinstance(filtre, int):  # Yıl bazlı filtreleme
            print(f"Yıl: {filtre} olan filmler:")
            for film in self.filmler:
                if film.yil == filtre:
                    print(film)

# Program Örneği
film_yoneticisi = FilmYoneticisi()

film1 = Film("Inception", "Christopher Nolan", 2010, "Bilim Kurgu")
film2 = Film("The Godfather", "Francis Ford Coppola", 1972, "Dram")
film3 = Film("Interstellar", "Christopher Nolan", 2014, "Bilim Kurgu")

film_yoneticisi.film_ekle(film1)
film_yoneticisi.film_ekle(film2)
film_yoneticisi.film_ekle(film3)

film_yoneticisi.filmleri_listele()
film_yoneticisi.filmleri_listele(filtre="Bilim Kurgu")
film_yoneticisi.filmleri_listele(filtre=2010)

film_yoneticisi.film_sil("The Godfather")
film_yoneticisi.filmleri_listele()