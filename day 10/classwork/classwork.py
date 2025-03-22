1 # დაწერეთ პროგრამა, რომელიც მომხმარებლს მოსთხოვს, რომ შემოიტანოს დადებითი რიცხვი. 
# თუ მომხმარებელი შემოიტანს უარყოფით რიცხვს ან ნულს, პროგრამამ უნდა მოსთხოვოს რიცხვის თავიდან შემოტანა


while True:  
    number = input("enter positive number: ")  
    if int (number) > 0:
        print(f"you enter positive number: {number}") 
    else:
        print("error! please try again: ")  
