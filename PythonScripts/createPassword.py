import random
import os

os.system("cls")
os.system("clear")

upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = upper_letters.lower()
symbols = "|!@#$%&/()={}[]',.-;:_"
numbers = "0123456789"
final_string =""

print("Welcome to Password Creator version 1.0")
print("Made by Diogo Vilaça - 2022")
print("Contact me: realplayerzero@gmail.com")

entity = input("Identify your password - ex: facebook, email, etc: ")

try:
    password_size = int(input("Enter the password's lenght: "))
    if password_size < 0 :
	    print("Value must be > 0")
except ValueError as e:
        print("Invalid input")
        
### IF YOU WANT MORE THAN 1 PASSWORD GENERATED AT THE SAME TIME, UNCOMMENT THE CODE BELLOW ###
#try:
    #passwords_amount = int(input("Enter the number of passwords. Max of 20 (1 is the default): "))
    #if passwords_amount < 0 or passwords_amount > 20:
        #passwords_amount = 1
        #print("Value must be > 0 or < 20. Default value assumed.")
#except ValueError as e:
        #print("Invalid input")
###

u = input("Use upper letters?(y/n): ")
if u == "y":
    final_string+= upper_letters
    
u = input("Use lower letters?(y/n): ")
if u == "y":
    final_string+= lower_letters
    
u = input("Use symbols?(y/n): ") 
if u == "y":
    final_string+= symbols

### UNCOMMENT AND IDENT FOR MORE THAN 1 PASSWORD ###
#for x in range(passwords_amount):
### 


final_string+= numbers
password = "".join(random.sample(final_string, password_size))       
print(entity + " password: " + password)
    
with open('passwords.csv', 'a') as f:
    f.write("\n" + entity + " password: " + password)