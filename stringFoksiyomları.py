# TEMEL STRİNG FONKSİYONLARI
from typing import overload

#len(s) = Bir string'in uzunluğunu (karakter sayısını) döner.

s="merhaba"
print(len(s))


# str() = Bir değeri string'e dönüştürür.

x = 12345
print(str(x))



#  Büyük/Küçük Harf İşlemleri

# s.upper()= String'in tüm harflerini büyük yapar.
d="Hava Cok Güzel"
print(d.upper())

# s.lower() = String'in tüm harflerini küçük yapar.
print(d.lower())


# s.capitalize() = String'in sadece ilk harfini büyük yapar.
print(s.capitalize())



#s.title() = String'deki her kelimenin ilk harfini büyük yapar.
c="python string fonksiyonları"
print(c.title())


# s.swapcase() = Büyük harfleri küçük, küçük harfleri büyük yapar
print(d.swapcase())




#  Arama ve Kontrol Fonksiyonları

# .find(sub) = Alt string'in (sub) ilk geçtiği indeksin konumunu döner. Bulamazsa -1 döner.
a="mehraba arkadasım"

print(a.find("arkadasım"))  # Çıktı: 0
print(a.find("Python"))  # Çıktı: -1

# s.index(sub) = find() gibidir ama alt string bulunamazsa hata (ValueError) verir.

s = "Merhaba Dünya"
print(s.index("Dünya"))  # Çıktı: 8
# print(s.index("python")) # Çıktı: ValueError




