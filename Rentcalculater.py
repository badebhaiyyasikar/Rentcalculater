##input we need from the user
#total food ordered for snacking 
#total rent 
#electricity units spend 
#per unit charge
#persons living in room

##output
#total amount you to pay
rent=int(input("Enter your rent = "))
food=int(input("Enter your amount of food orderd = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit= int(input("Enter the charge per unit = "))
persons = int(input("Enter the of persons living in room = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent +total_bill) //persons

print ("Each persons will pay = ",output)


print("made by sandeep kumawt"  "," "bade bhaiyya sikar ")
