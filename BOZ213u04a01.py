def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

yil = int(input("Bir yıl giriniz: "))
sonuc = is_year_leap(yil)
print(sonuc)
