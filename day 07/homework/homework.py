1 #  კომენტარის სახით ჩამოწერეთ and და or ლოგიკური ოპერატორების ყველა 
# შესაძლო გამოსახულება. ამასთანავე, მიუწერეთ თუ რა იქნება თითოეული ოპერაციის შედეგი.

print(True and False) # false
print(True and False and True) # false
print(True and False and True and True) # false
print(False and True and True and True and False) # false
print(False and Falsee and False and False) # False


print(True or False)#True
print(True or False or False) # True
print(False or False or False or True) # True
print(True or True or False) # True
print(True or True or True or True or False) # True



2 # ტერმინალში გაშვების გარეშე დაადგინეთ თუ რას გამოიტანს მოცემული კოდი:
True and False or True or True and False
# ბოლოს კი გაუშვით ეს კოდი და შეამოწმეთ თქვენი ვარაუდი გამართლდა თუ არა.

# ეს გამოიტანს True, დიახ გამართლდა



3 #  მომხმარებელს შემოატანინე ორი რიცხვი, შეამოწმე არის თუ არა ეს რიცხვები ერთმანეთის ტოლი
# და შედეგი გამოიტანე ტერმინალში. (შედეგი Boolean მნიშვნელობის უნდა იყოს.)


first_num = float(input("enter your first number: "))
second_num = float(input("enter your second number: "))

if first_num == second_num:
    print("True")
else:
    print("False")




4 # მომხმარებელს შემოატანინე მისი შემაფასებელი ქულა (0-დან 100-ის ჩათვლით).

# • იმ შემთხვევაში თუ შემოტანილი ქულა მეტია ან ტოლია 90-ის, ტერმინალში გამოიტანე "Grade A".
# • თუ მისი ქულა მეტია ან ტოლია 70-ზე გამოიტანე "Grade B". 
# • თუ მომხმარებლის ქულა მეტია ან ტოლია 50-ზე ტერმინალში დაბეჭდე "Grade C"
# • ყველა დანარჩენ შემთხვევაში გამოიტანე  "Grade F"


point = int(input("enter your  point (0-100):  "))

if point >= 90:
    print("Grade A")
elif point:
    print("Grade B")
elif point:
    print("Grade C")
else:
    print("Grade F")




5 #  მომხმარებელს შემოატანინე მთელი რიცხვი. იმ შემთხვევაში, თუ ეს რიცხვი არის ლუწი
# და ამავდროულად არის 10-ზე მეტი, დაბეჭდე True. ყველა სხვა შემთხვევაში False. 


num = int(input("enter an integer: "))

if num % 2 == 0 > 10:
    print("True")
else:
    print("False")

