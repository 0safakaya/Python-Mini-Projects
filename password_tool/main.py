import random
import string


def sifre_uret(uzunluk=12, buyuk_harf=True, kucuk_harf=True, rakam=True, sembol=True):
    """
    Verilen parametrelere göre rastgele şifre üretir.
    """

    karakter_havuzu = ""

    if buyuk_harf:
        karakter_havuzu += string.ascii_uppercase
    if kucuk_harf:
        karakter_havuzu += string.ascii_lowercase
    if rakam:
        karakter_havuzu += string.digits
    if sembol:
        karakter_havuzu += string.punctuation

    if not karakter_havuzu:
        return None

    sifre = "".join(random.choice(karakter_havuzu) for _ in range(uzunluk))
    return sifre


def sifre_gucluluk_analiz(sifre):
    """
    Girilen şifrenin gücünü analiz eder.
    Puan ve seviye döndürür.
    """

    puan = 0

    if len(sifre) >= 8:
        puan += 1
    if len(sifre) >= 12:
        puan += 1
    if any(harf.islower() for harf in sifre):
        puan += 1
    if any(harf.isupper() for harf in sifre):
        puan += 1
    if any(harf.isdigit() for harf in sifre):
        puan += 1
    if any(harf in string.punctuation for harf in sifre):
        puan += 1

    if puan <= 2:
        seviye = "Zayıf"
    elif 3 <= puan <= 4:
        seviye = "Orta"
    else:
        seviye = "Güçlü"

    return puan, seviye


def menu():
    while True:
        print("\n===== ŞİFRE ARACI =====")
        print("1 - Şifre Üret")
        print("2 - Şifre Güç Analizi Yap")
        print("3 - Çıkış")

        secim = input("Bir seçenek giriniz: ")

        if secim == "1":
            try:
                uzunluk = int(input("Şifre uzunluğu: "))
            except ValueError:
                print("Geçersiz uzunluk girdiniz!")
                continue

            buyuk_harf = input("Büyük harf eklensin mi? (e/h): ").lower() == "e"
            kucuk_harf = input("Küçük harf eklensin mi? (e/h): ").lower() == "e"
            rakam = input("Rakam eklensin mi? (e/h): ").lower() == "e"
            sembol = input("Sembol eklensin mi? (e/h): ").lower() == "e"

            sifre = sifre_uret(uzunluk, buyuk_harf, kucuk_harf, rakam, sembol)

            if sifre:
                print(f"\nOluşturulan Şifre: {sifre}")
                puan, seviye = sifre_gucluluk_analiz(sifre)
                print(f"Güç Seviyesi: {seviye} (Puan: {puan}/6)")
            else:
                print("En az bir karakter türü seçmelisiniz!")

        elif secim == "2":
            sifre = input("Analiz edilecek şifreyi giriniz: ")
            puan, seviye = sifre_gucluluk_analiz(sifre)
            print(f"Güç Seviyesi: {seviye} (Puan: {puan}/6)")

        elif secim == "3":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim yaptınız!")


if __name__ == "__main__":
    menu()