def hesap_makinesi():
    print("1. Toplama ")
    print("2. Çıkarma ")
    print("3. Çarpma ")
    print("4. Bölme ")

    secim = int(input("Seciminizi yapınız(1/2/3/4): "))
    num = float(input("Birinci sayıyı giriniz : "))
    nums = float(input("ikinci sayıyı giriniz : "))
    if secim == 1:
        print(f"sonuc : {num + nums} ")
    elif secim == 2:
        print(f"sonucç:{num - nums} ")
    elif secim == 3:
        print(f"sonuc: {num * nums}")
    elif secim == 4:
        if nums != 0:
            print(f"sonuc: {num / nums}")
        else:
            print("HATA : sıfıra bölme yapılamaz")
    else:
        print("Gecersiz secim.")

hesap_makinesi()