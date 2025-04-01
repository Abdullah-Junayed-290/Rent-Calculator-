rent = int(input("Enter flat/hostel rent = "))

food_Ordered = int(input("Enter the amount of food ordered = "))

electricity_bill = int(input("Enter the total electricity bill = "))

charge_per_unit = int(input("Enter the charge per unit = "))

person = int(input("Enter total room person ar living = "))



total_electricity_bill = electricity_bill * charge_per_unit

total_pay = (rent + food_Ordered + total_electricity_bill) // person 


print("Each person will pay ", total_pay)