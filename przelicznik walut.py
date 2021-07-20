# 1euro=4,26pln
# 1dolar=3,89pln

def podaj(x):
    return x

print("1 EURO = 4,26 ZŁOTY")
print("1 DOLAR = 3,89 ZŁOTY")

print("Wybierz co chcesz przeliczyć: ")
print("1. PLN / EURO")
print("2. PLN / DOLAR")
print("3. EURO / PLN")
print("4. DOLAR / PLN")

choice = input("Którą operację chcesz wykonać? Wybierz 1/2/3/4: ")
num1=float(input("Podaj ilość pierwszej waluty "))
# num2=int(input("Podaj drugą liczbę ")) #float - liczby rzeczywiste , int - liczby całkowite

if choice == '1':
    print("Twój wynik to około: ", int(podaj(num1/4.26)), "E")
elif choice == '2':
    print("Twój wynik to około: ", int(podaj(num1/3.89)), "$")
elif choice =='3':
    print("Twój wynik to około: ", int(podaj(num1*4.26)), "zł")
elif choice == '4':
    print("Twój wynik to około: ", int(podaj(num1*3.89)), "zł")
else:
    print("Niepoprawna wartość")

