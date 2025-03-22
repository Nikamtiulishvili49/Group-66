1 #  მოიყვანეთ while loop-ის მაგალითი და კომენტარის სახით ახსენით, თუ როგორ მუშაობს while ციკლი;

n = 3 # ვიწყებთ 1 იდან 
while n < 5: # აქ while ციკლი მუშაობს სანამ n ნაკლები იქნება 5 ზე
    print(n) # დავბეჭდოთ n ცვლადი



2 #  კომენტარის სახით ახსენით თუ რა განსხვავებაა for loop-სა და while loop-ს შორის;

# for loop ში დეველოპერები განვსაზღვრავთ თუ რამდენჯერ გამოვიტანთ კონკრეტულ სიტყვას,
# ხოლო while loop ში არ გვაქ განსაზღვრული ინტერაციების რაოდენობა.


3 #  ცვლადში შეინახეთ პაროლი. შემდეგ მომხმარებელს შემოატანინეთ პაროლი, სანამ მომხმარებლის მიერ შემოტანილი 
# პაროლი არ დაემთხვევა თქვენს პაროლს, გამოუტანეთ Incorrect password. Try again".
#  იმ შემთხვევაში თუ ეს პაროლები ერთმანეთს დაემთხვევა გამოიტანეთ 
# "Correct password. You have successfully logged in." (გააკეთეთ While ციკლით, არ გამოიყენოთ if else statement-ები.);


password = "nika123"  
user_password = input("Enter a password: ")
while password != user_password:
    print("Incorrect password. Try again")  
    user_password = input("Enter a password: ")  

print("Correct password. You have successfully logged in") 




4 #  ტერმინალში დაბეჭდეთ რიცხვები 1-დან 20-ის ჩათვლით ორ-ორის გამოტოვებით.

i = 1  

while i <= 20:  
    print(i)  
    i += 2  



5 # Sololearn-ში გაიარეთ While loops სექცია:



