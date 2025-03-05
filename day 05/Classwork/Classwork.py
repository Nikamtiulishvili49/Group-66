1 # შექმენით პროგრამა, სადაც მომხმარებელს შემოატანინებთ # სახელს, გვარს და ასაკს,
# შემოტანილი მნიშვნელობები შეინახეთ ცვლადებში, ცვლადებსა # დაარქვით ისეთი სახელები რომელიც შეესაბამება მნიშვნელობებს,
#  აგრეთვე კომენტარებით ახსენით რა არის ფუნქცია + ყველა ხაზი დააკომენტარეთ და ახსენით თითოეულ ხაზზე რას აკეთებთ

firstname = input ("please enter your name: ") # აქ ვეუბნებით მომხმარებელს რომ შემოიტანოთ მისი სახელი

surname = input ("please enter your surname: ") # აქ ვეუბნებით მომხმარებელს რომ შემოიტანოთ მისი გვარი

age = input ("please enter your age") # აქ ვეუბნებით მომხმარებელს რომ შემოიტანოთ მისი ასაკი

print(firstname,surname,age)

# ფუნქცია არის მოქმედება რომელიც ასრულებს თავის მოვალეობას,რასაც ჩვენ ვანიჭებთ 




2 #  bonus: შექმენით პროგრამა სადაც მომხმარებელს შემოატანინებთ სახელს და ასაკს,
# შემდეგ შეამოწმეთ ასაკი, თუ ასაკი >= 18 დაუბეჭდეთ რომ მას შეუძლია შევიდეს კლუბში, სხვა შემთხვევაში დაუბეჭდეთ რომ არ შეუძლია.
  # test case 1
# input: Luka 24
# output: "Luka you can enter in the club"

# test case 2
# input: Luka 16
# output: "Luka you can't enter club"


firstname = input  ("enter your firstname:")
age = input("enter your age")

print(firstname,age)

if age >=18:
    print("you can enter in the club ")
else:
    print("you can't enter in the club")


