#  Merhaba Dünya
print("hello wold")

print("--------------------------")

# 2. Değişken Tanımlama
yas=12
isim = "ahmet"
boy= 1.40
print(f"isim: {isim}, yaş {yas}, boy {boy}")

print("--------------------------")

# 3. Kullanıcıdan Veri Alma
isim1=input("Adınız nedir: ")
print(f"merhaba , {isim1} ")

print("--------------------------")

# 4. Koşul İfadeleri (if-else)
sayi=int(input("bir sayı giriniz"))
if sayi>0:
    print("pozitif bir sayı girdiniz")
elif sayi==0:
    print("sıfır girdiniz")
else:
    print("negatif bir sayı girdiniz")


print("--------------------------")

#5. Döngüler

# For Döngüsü
for i in range(7):
    print(f"Sayı : {i}")

# While Döngüsü

sayi=2
while sayi<=5:
    print(sayi)
    sayi+=1

# 6. Liste Kullanımı

meyveler=["elma","armut","muz","portakal"]
for meyveler in meyveler:
    print(meyveler)