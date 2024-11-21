#  Merhaba Dünya
print("hello wold")

print("--------------------------")

# 2. Değişken Tanımlama
yas = 12
isim = "ahmet"
boy = 1.40
print(f"isim: {isim}, yaş {yas}, boy {boy}")

print("--------------------------")

# 3. Kullanıcıdan Veri Alma
isim1 = input("Adınız nedir: ")
print(f"merhaba , {isim1} ")

print("--------------------------")

# 4. Koşul İfadeleri (if-else)
sayi = int(input("Bir sayı girin: "))
if sayi > 0:
    print("Pozitif bir sayı girdiniz.")
elif sayi == 0:
    print("Sıfır girdiniz.")
else:
    print("Negatif bir sayı girdiniz.")

print("--------------------------")

# 5. Döngüler

# For Döngüsü
for i in range(7):
    print(f"Sayı : {i}")

# While Döngüsü

sayi = 2
while sayi <= 5:
    print(sayi)
    sayi += 1

print("--------------------------")

# 6. Liste Kullanımı

meyveler = ["elma", "armut", "muz", "portakal"]
for meyveler in meyveler:
    print(meyveler)

print("--------------------------")

print("BASIT MATAMATİK İŞLEMLERİ-")

print("--------------------------")



# Toplama işlemi
num1 = 30
nums2 = 25
toplama = num1 + nums2
print(f"Toplama :{num1}+{nums2}={toplama}")

print("--------------------------")

# Cıkarma işlemi
num = 30
nums = 25
fark = num - nums
print(f"Cıkarma :{num} - {nums}={fark}")

# Carpma işlemi
num = 30
nums = 25
carpma = num - nums
print(f"Cıkarma :{num}*{nums}={carpma}")

print("--------------------------")

# bölme işlemi
num = 30
nums = 25
bolme = num - nums
print(f"Cıkarma :{num}*{nums}={bolme}")

print("--------------------------")

# 7. Dosya Okuma ve Yazma

print("dosya yazma")
with open("deneme.txt","w") as dosya:
    dosya.write("merhabalar ben melda pyton'u daha yeni öğreniyorum ")

print("dosya okuma")
with open("deneme.txt","r") as dosya:
    icerk=dosya.read()
    print(icerk )


print("--------------------------")
