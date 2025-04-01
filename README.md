# Room Expense Splitter

## Overview
This Python script helps roommates or hostel dwellers split their monthly expenses evenly. It takes inputs for rent, food costs, and electricity bills, calculates the total cost, and determines how much each person should pay.

## Features
- Calculates total electricity bill based on unit charge.
- Splits expenses evenly among all residents.
- Provides a simple way to manage shared expenses.

## How It Works
1. The user inputs the rent amount.
2. The user enters the total cost of food ordered.
3. The user provides the total electricity consumption and charge per unit.
4. The user specifies the number of residents sharing the expenses.
5. The script calculates and displays each person's share.

## Code
```python
rent = int(input("Enter flat/hostel rent = "))

food_Ordered = int(input("Enter the amount of food ordered = "))

electricity_bill = int(input("Enter the total electricity bill = "))

charge_per_unit = int(input("Enter the charge per unit = "))

person = int(input("Enter total room person living = "))


total_electricity_bill = electricity_bill * charge_per_unit

total_pay = (rent + food_Ordered + total_electricity_bill) // person

print("Each person will pay ", total_pay)
```

## Usage
1. Copy and paste the script into a Python environment.
2. Run the script and input the required values.
3. The script will output the amount each person should pay.

## Example Input/Output
### Input:
```
Enter flat/hostel rent = 10000
Enter the amount of food ordered = 5000
Enter the total electricity bill = 300
Enter the charge per unit = 10
Enter total room person living = 3
```

### Output:
```
Each person will pay 6000
```

## License
This project is open-source and free to use.

