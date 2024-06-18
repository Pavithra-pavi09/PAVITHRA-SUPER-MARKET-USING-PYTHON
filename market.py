import datetime
import smtplib
import random
x = datetime.datetime.now()
current = x.strftime("%H:%M:%S %p")
f=open("bill.txt","a")
f.write("\n***SUPER MARKET**\n")
f.write(f"\nTime of Purchase is {current}\n")

cost = []
def calculate():
    total=sum(cost)
    f=open("bill.txt","a")
    f.write(f"\nThe grand total is {total}")
    print(f"The grand total is {total}")
    email_sending(total)

def email_sending(total):
    try:
        receiver_mails=["durpavadhaarani@gmail.com"]
        for i in receiver_mails:
            otp_number=random.randint(0000,9999)
            print(i,otp_number)
            s=smtplib.SMTP('SMTP.gmail.com',587)
            s.starttls()
            s.login("adipavi2005@gmail.com","aryn vqxl iupq oxet")
            message=f" your otp number is {otp_number}"
            message=f"your grand total is {total} "
            s.sendmail("adipavi2005@gmail.com",i,message)
            s.quit()
            print("mail sent successfully")
    except:
        print("mail not sent")  
        


def main():
    Available = ["Biscuit", "Shop", "Shampoo", "Chocolate", "Samayal Powders", "Ice Creams", "Fruits", "Vegitables", "Make_Up Items"]
    prizes = {
        "Biscuit": 20,
        "Shop": 50,
        "Shampoo": 3,
        "Chocolate": 50,
        "Samayal Powders": 30,
        "Ice Creams": 30,
        "Fruits": 100,
        "Vegitables": 150,
        "Make_Up Items": 300
    }
    
    
    your_order = input("Enter your order: ")

    if your_order in Available:
        print(f"YES, {your_order} is available")
        try:
            how_many = int(input(f"How many {your_order} you want: "))
            total = prizes[your_order]* how_many
            cost.append(total)

            f=open("bill.txt","a")
            f.write(f"\n {your_order} total bill is {total}")

            print(f"Your total bill for {your_order} is {total}")
            print("Bill generated successfully")

            var = input("Do you want to continue (yes/no): ")
            if var == "yes":
                main()
            else:
                calculate()
                print("Thank You for coming. WELCOME Again")           
         
        except :
            print("Please type a number only")
    else:
        print(f"Sorry, {your_order} is not available")

main()