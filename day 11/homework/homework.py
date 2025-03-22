1 #  შექმენით Number guess game, if else statement-ების გამოყენებით.

number = 300

print("Hello! Guess the number I am thinking of (It's 300).")

guess = int(input("Enter your guess: "))

if guess < number:
    print("Your number is low.")
elif guess > number:
    print("Your number is high!")
else:
    print(" You guessed the correct number!")



2 #  შექმენით Number guess game, while ციკლების გამოყენებით.

number = 100

guess = 30 
while guess != number:  
    guess = int(input("Enter your guess: "))  
    
    if guess < number:
        print("Your number is  low!")
    elif guess > number:
        print("Your number is  high!")
    else:
        print("You guessed the correct number!")



3 # გაიხსენეთ გაკვეთილზე გაკეთებული დავალება მომხმარებლის სისტემაში
# შესვლის მცდელობაზე და დამოუკიდებლად გააკეთეთ იგივე while ციკლის საშუალებით.















4 #  გადაუარეთ სტრინგს for loop-ით და სტრინგში მხოლოდ ლუწ ინდექსებზე მდგომი ასოები დაბეჭდეთ .

text = "nikanika"

for i in range(0, len(text), 2):  
    print(text[i])



5 # გამოიყენეთ range და ლუწ ინდექსებზე მდგომი რიცხვები შეკრიბეთ. ჯამი გამოიტანეთ ტერმინალში.

numbers = "16793967"

total = 0

for i in range(0, len(numbers), 2): 
    total += int(numbers[i])  
print("Sum:", total)


