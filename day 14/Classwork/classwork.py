1 # 1) მომხმარებელს შემოატანინეთ 10 მნიშვნელობა სიაში (For loop-ის მეშვეობით. ) შემდეგ გამოიყენეთ კიდევ ერთი for loop, 
# გადაუარეთ თითოეულ სიის ელემენტს და შამოწმეთ ეს რიცხვები ლუწია თუ კენტი


numbers = []
for i in range(10):
    number = int(input("Please enter a number: "))
    numbers.append(number)

for num in numbers:
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")



2 #  მომხმარებელს შემოატანინეთ 5 სახეთი, შემდეგ კი კიდევ ერთი for loop გამოიყენეთ რათა გაიგოთ ამ სახელებში სიმბოლოების რაოდენობა 
# აღემატება თუ არა 5-ს. თუ აღემატება დაუბეჭდეთ "the name consists of more than five letters)


names = []
for i in range(5):
    name = input("Please enter a name: ")  
    names.append(name)

for name in names:
    if len(name) > 5:
       print("The name", name, "consists of more than five letters.")




3 # შექმენით სია, რომელშიც დაამატებთ ჯანსაღ საკვებ პროდუქტებს. (იყოს მინიმუმ 5 პროდუქტი). ამოშალეთ სიის პირველი და ბოლო 
# ელემენტები და ტერმინალში დაბეჭდეთ სიის განახლებული ვერსია

healthy_foods = ["apple", "banana", "carrot", "cherry", "blueberries"]

del healthy_foods[0]  
del healthy_foods[-1]  

print(healthy_foods)






4 # შექმენით რიცხვების სია, რომელშიც მინიმუმ გექნებათ 5 ელემენტი. ამ 5 ელემენტიდან 1 განსხვავებული ელემენტი იქნება.
# ეს ელემენტი უნდა იყოს მოთავსებული დაახლოების სიის შუაში. (არ უნდა იყოს სიის დასაწყისში ან დასასრულში). 
# თქვენი დავალებაა დაწეროთ პროგრამა და იპოვოთ ეს განსხვავებული ელემენტი მოცემულ სიაში. (მინიშნება: სიის დალაგება)




def find_unique(numbers):
    if numbers[2] != numbers[1]:  
        return numbers[0] 
    
    elif numbers[-1] != numbers[-4]:
        return numbers[-1]  
    else:
        for i in range(1, len(numbers) - 4): 
            if numbers[i] != numbers[i - 4] and numbers[i] != numbers[i + 1]:
                return numbers[i]  

numbers = [1, 1, 2, 1, 1]
result = find_unique(numbers)
print(result)  

