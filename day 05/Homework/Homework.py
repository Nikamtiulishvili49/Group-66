1 #  გააკეთეთ პირველი ორი სექცია და დამატებით მესამე სექციაში ორი გაკვეთილი გაიარეთ თქვენით


2 #  ცვლადში შეინახეთ პაროლი, შემდეგ კი მომხმარებელს შემოატანინეთ პაროლი. იმ შემთხვევაში, თუ 
# მომხმარებლის მიერ შემოტანილი პაროლი სწორია, დაბეჭდეთ "accsess grantedess ". წინააღმდეგ შემთხვევაში - "access denied".


my_password = "nika2009"

user_password = input("enter your password: ")
if my_password == user_password:
    print("accsess grantedess")
else:
    print("access denied")



2 # მომხმარებელს შემოატანინეთ რიცხვი და დაწერეთ ისეთი პროგრამა, რომელიც განსაზღვრავს ეს რიცხვი ლუწია თუ კენტი.


num1 = int(input("enter your number: "))

if num1 % 2 == 0:
    print("number is odd")
else:
    print("number is even")



3 # მომხმარებელს შემოატანინეთ 5 რიცხვი. დაწერეთ პროგრამა, რომელიც გამოთვლის და დაბეჭდავს ამ რიცხვების საშუალო არითმეტიკულს.


num1 = int(input("enter  your number"))
num2 = int(input("enter  your number"))
num3 = int(input("enter  your number"))
num4 = int(input("enter  your number"))
num5 = int(input("enter  your number"))

total = num1 + num2 + num3 + num4 + num5

avarge = total / 5

print("The arithmetic mean of these 5 numbers is: ", avarge)


4 #  მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოტანილ ტემპერატურას გადაიყვანს 
# ფარენგეიტში და დაბეჭდეთ საბოლოო შედეგი. (მოიძიეთ ფორმულა ინტერნეტში)


celcius = float(input("enter the temperature in celcius "))

farenheit = (9/5) * celcius + 32

print(f"temperature in farenheit:{farenheit} ")



5 # მეხუთე დავალების მსგავსად, შემოატანინეთ მომხმარებელს ტემპერატურა, თუმცა ამჯერად ფარენგეიტში.
# შემდეგ კი დაწერეთ პროგრამა, რომელიც შემოტანილ ტემპერატურას ცელსიუსში გადაიყვანს და საბოლოოდ დაბეჭდეთ შედეგი.


arenheit = float(input("enter the temperature in farenheit: "))

celcius = (5/9) * (farenheit - 32)

print(f"temperature in celcius:{celcius} ")











