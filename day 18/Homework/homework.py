1 #  ჩამოწერეთ ყველა პითონის ჩაშენებული ფუნქცია, რაც დღს განვიხილეთ.
 
 # print() 

# len() 

# type() 

# input() 

# int() 

# str() 

# float() 

# sum() 

# max() 

# min() 




2 # 

# 1
print("Hello World") # -   ეს დაპრინტავს ტერმინალში  Hello world
# 1
name = "Nika"
print("Hello, " + name) # -  ეს გამოიტანს Hello და ცვლადში შენახულ სახელს ამჯერად Nika


# 2
list = [1, 2, 3, 4, 5]
print(len(list)) # -  len ფუნქცია ითვლის თუ რამდენი ელემენტია სიაში ამჯერად ეს გამოიტანს 5 - ს
# 2
word = "Nikolozi"
print(len(word)) # - აქ კი ითვლის თუ რამდენი სიმბოლოა სიტყვაში


# 3
number = 10
print(type(number)) # - type ფუნქცია გვაძლევს პასუხს თუ რა ტიპისაა ცვლადში მოცემული რიცხვი, ამჯერად ეს გამოიტანს Integer - ს
# 3
word = "Hello"
print(type(word)) # - აქაც იგივეს აკეთებს ეს კი string - ს გამოიტანს


# 4
name = input("Enter your name: ")
print("Hello, " + name)
# 4
my_age = 15
name = input("enter your age")
if my_age != name:
    print("Try again")
else:
    print("That's right.")



# 5 







3 # ეცადეთ, რომ გააკეთოთ ამ ფუნქციების Copy ფუნქციები თქვენი ხელით.

# ვერ გავაკეთე



4 #  შექმენით სია სადაც შეინახავთ 5 რიცხვს, მომხმარებელს აარჩევინეთ ამ სიიდან ერთ-ერთი რიცხვი და დათვალეთ 
# თუ რამდენჯერ მეორდება ეს რიცხვი სიაში.


numbers = [5, 7, 10, 55, 6]

x = int(input("Pick a number: "))
print(numbers.count(x))





5 #  შექმენით სია, სადაც დაამატებთ მინიმუმ 5 ელემენტს. მომხმარებელს ჰკითხე სურს თუ არა სიის გასუფთავება.
# თუ დაგთანხმდება გაასუფთავე სია თუ არა მაშინ ჩვეულებრივად დაბეჭდე ეს სია ტერმინალში.

numbers = [10, 15, 33, 55, 77, 90, 14, 100]

answer = input("do you want clean this list: yes Or No ->")

if answer == "yes":
    numbers.clear
    print("the list is clear")
else:
    print("The list remained the same.")
    print(numbers)





6 #  შექმენით სია სახელად Fruits და ჩაამატეთ მასში ხილი. მომხმარებელს შემოატანინეთ ინდექსი და შემდეგ  ამ ინდექსზე მდგომი
# ელემენტი ამოშალე სიიდან. საბოლოოდ დაბეჭდე სიის საბოლოო ვერსია.


Fruits = ["banana", "apple", "cherry"]

index = int(input("Enter index to remove: "))

if 0 <= index < len(Fruits):
    Fruits.pop(index)
print(Fruits)





7 # გააკეთეთ Codewars-ები: 

# 7) https://www.codewars.com/kata/5a023c426975981341000014/train/python (ამ ამოცანის გასაკეთებლად მათემატიკური ცოდნა დაგჭირდებათ,
#  ამიტომ მოიძიეთ ინფორმაცია თუ როგორ ვიპოვოთ სამკუთხედის მესამე კუთხის გრადუსი,
#  იმ შემთხვევაში თუ დანარჩენი ორი კუთხის გრადუსი ჩვენთვის უკვე ცნობილია).

# 8) https://www.codewars.com/kata/5951d30ce99cf2467e000013/train/python (მესამე ამოცანის მსგავსად, ამ kata-ს ამოსახსნელად
#  დაგჭირდებათ მათემატიკური ცოდნა. კერძოდ პითაგორას თეორემა. მოიძიეთ ინფორმაცია პითაგორას თეორემის
#  შესახებ და ამის მიხედვით ამოხსენით ეს codewars-ი)

# 9) https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

# 10) https://www.codewars.com/kata/5ad0d8356165e63c140014d4

# 11) https://www.codewars.com/kata/5834fec22fb0ba7d080000e8/train/python

# 12)https://www.codewars.com/kata/566dc566f6ea9a14b500007b/train/python

# 13) https://www.codewars.com/kata/559590633066759614000063/train/python











