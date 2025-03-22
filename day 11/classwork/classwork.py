1 # შექმენით პროგრამა, რომელშიც 10 ჯერ შემოატანინებთ მომხმარებელს მთელ რიცხვს, 
# შემდეგ კი უნდა გამოთვალოთ ამ რიცხვების ჯამი და გაიგოთ საშუალო არითმეტიკული

# საშუალო არითმეტიკული:
# რიცხვების ჯამი უნდა გაყოთ მაგ რიცხვების რაოდენობაზე

# მაგ:
# 3 + 2 + 5 / 3

total = 0  
count = 0  
while count < 10:
    num = int(input("enter number: ")) 
    total += num  
    count += 1  
average = total / 10  

print("total:", total)
print("avarge arithmeic:", average)
