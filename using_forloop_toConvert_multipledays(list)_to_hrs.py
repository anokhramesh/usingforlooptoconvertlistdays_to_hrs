# In this program we will convert a list of days to hours using for loop and split function in python.
calculation_to_units =24
name_of_unit = "Hours"

def days_to_units(num_of_days):# created a function name -days_to_units with an argument of num_of_days.
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
def validate_and_execute():#function for validation if user input is int data type,then only calculate conversion.
    try:
        user_input_number =int(num_of_days_elements)#type casting the usre input to int data type.
        if user_input_number >0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You Entered  0,Please enter a valid positive number")
        else:
            print("You Entered a negative number,Not Possible conversion")
    except ValueError:
        print("Your input is not a valid number")

user_input =""
while user_input != "exit":
    user_input =input("Enter number of Days for convert to Hours\n")
    for num_of_days_elements in user_input.split(","):#using split function to split the user input lits with comas.
        validate_and_execute()
