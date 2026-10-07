# Section 1: Variables and Types

name = "Student"
age = 40
height = "5.7"
is_student = True

name = "Alex"
age = 27
height = 5.9
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2: User Input and Math

name = input("Please enter your name: ")
Year_of_birth = input("Please enter the year you were born: ")
conv_age = int(Year_of_birth)
year_current = 2026
age = year_current - conv_age
print(f"Hello, {name}! You are approximately {age} years old.")

# Section 3: Type Conversion and f-strings

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

product = number1 * number2

print(f"{number1} × {number2} = {product}")

# Section 4: Formatted Receipt

item = "Guitar strings"
price = 12.99
quantity = 3

total = price * quantity

print("===========================")
print("        RECEIPT")
print("===========================")
print(f"Item:      {item}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")


# Section 5: Mini-Project - Profile Card

profile_name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("Tell me one fun fact about yourself: ")
profile_birth_year = int(input("What year were you born? "))
current_year = 2026

profile_age = current_year - profile_birth_year

print()
print("╔══════════════════════════════╗")
print(f"      PROFILE: {profile_name}")
print("╚══════════════════════════════╝")
print(f"{'Hometown:':12} {hometown}")
print(f"{'Hobby:':12} {hobby}")
print(f"{'Fun fact:':12} {fun_fact}")
print(f"{'Age:':12} {profile_age}")
