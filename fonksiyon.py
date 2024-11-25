class Islemler:
    # Toplama Fonksiyonu
    @staticmethod
    def toplama(a, b):
        return a + b

    # Çıkarma Fonksiyonu
    @staticmethod
    def cikarma(a, b):
        return a - b

    # Çarpma Fonksiyonu
    @staticmethod
    def carpma(a, b):
        return a * b

    # Bölme Fonksiyonu
    @staticmethod
    def bolme(a, b):
        if b != 0:  # Sıfıra bölme kontrolü
            return a / b
        else:
            return "HATA: Bir sayı 0'a bölünmez!!"


