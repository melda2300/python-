""" Python Yerleşik Fonksiyonları

 1. Veri Tipi Dönüştürme Fonksiyonları
 int(): Bir değeri tamsayıya çevirir.
 float(): Bir değeri ondalıklı sayıya çevirir.
 str(): Bir değeri string (metin) hale getirir.
 bool(): Bir değeri True veya False olarak döndürür.
 complex(): Karmaşık sayı oluşturur.
 list(): Bir liste oluşturur.
 tuple(): Bir tuple oluşturur.
 set(): Bir set oluşturur.
 dict(): Bir sözlük (dictionary) oluşturur.
 frozenset(): Değiştirilemez bir set oluşturur.
 bytes(): Byte dizisi oluşturur.
 bytearray(): Değiştirilebilir byte dizisi oluşturur.
 memoryview(): Byte'lara erişim sağlar.
 
 # 2. Matematiksel Fonksiyonlar
 abs(): Bir sayının mutlak değerini döndürür.
 pow(): Bir sayının kuvvetini alır (ör. pow(2, 3) = 8).
 round(): Ondalıklı bir sayıyı en yakın tam sayıya yuvarlar.
 min(): Bir listedeki en küçük değeri döndürür.
 max(): Bir listedeki en büyük değeri döndürür.
 sum(): Bir iterable'ın (örneğin liste) elemanlarının toplamını döndürür.
 divmod(): Bölme ve kalan işlemini bir arada döndürür.
 bin(): Bir sayıyı ikili (binary) hale çevirir.
 oct(): Bir sayıyı sekizli (octal) hale çevirir.
 hex(): Bir sayıyı onaltılı (hexadecimal) hale çevirir.
 
 # 3. Diziler ve Iterable'lar İçin Fonksiyonlar
 len(): Bir dizinin uzunluğunu döndürür.
 sorted(): Bir diziyi sıralar.
 reversed(): Bir diziyi tersine çevirir.
 enumerate(): Bir iterable'ı numaralandırır.
 zip(): Birden fazla iterable'ı birleştirir.
 map(): Bir fonksiyonu iterable'ın her elemanına uygular.
 filter(): Belirli bir koşulu sağlayan elemanları seçer.
 all(): Tüm elemanlar True ise True döner.
 any(): Elemanlardan biri bile True ise True döner.
 range(): Belirli bir aralıkta sayı üretir.
 iter(): Bir iterable'ın iterator'ını döndürür.
 next(): Bir iterator'ın bir sonraki elemanını döndürür.
 
 # 4. Girdi ve Çıktı Fonksiyonları
 print(): Konsola veri yazdırır.
 input(): Kullanıcıdan veri alır.
 open(): Bir dosya açar.
 
 # 5. Nesne ve Tip Kontrolü
 type(): Bir nesnenin türünü döndürür.
 isinstance(): Bir nesnenin belirli bir türde olup olmadığını kontrol eder.
 id(): Bir nesnenin benzersiz kimliğini döndürür.
 hash(): Bir nesnenin hash değerini döndürür.
 dir(): Bir nesnenin özelliklerini ve metodlarını listeler.
 help(): Yardım ve belgeleri görüntüler.
 callable(): Bir nesnenin çağrılabilir olup olmadığını kontrol eder.
 
 # 6. Karakter ve String İşlemleri
 ord(): Bir karakterin Unicode kodunu döndürür.
 chr(): Bir Unicode kodunun karakterini döndürür.
 ascii(): Bir string'in ASCII temsiline döner.
 repr(): Bir nesnenin okunabilir temsilini döndürür.
 
 # 7. Global ve Yerel Değişkenler
 globals(): Tüm global değişkenleri döndürür.
 locals(): Yerel değişkenleri döndürür.
 eval(): Bir string ifadesini çalıştırır.
 exec(): Python kodunu çalıştırır.
 compile(): Python kodunu derler.
 
 # 8. Hatalar ve İstisnalar
 abs(): Mutlak değer.
 raise: Hata fırlatır.
"""""