import random
random_number=random.randint(1,100)
print("1 ile 100 arasında bir sayı giriniz: ")
while True:
    tahmin=int(input("TAHMİNİNİZİ YAZINIZ : "))
    if tahmin < random_number:
        print(" daha büyük sayı girin: ")
    elif tahmin >random_number:
        print("daha kücük sayı girin: ")
    else:
        print("tebrikler doğru tahmin.")
        break