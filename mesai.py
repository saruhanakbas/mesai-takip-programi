print("Kaç Saat Çalıştın? Lütfen bir sayı değeri giriniz.")

try:
    time = int(input())

    if time == 1 or time == 2 or time == 4 or time == 5 or time == 6 or time == 7 or time == 8:
        print("Mesai devam ediyor.")
    elif time == 3:
        print("Öğle Arası.")
    elif time == 9:
        print("Mesai Bitti.")
    else:
        print("Lütfen doğru bir time değeri giriniz (1-9).")
except ValueError:
    print("Lütfen bir sayı değeri giriniz.")
