def safe_add_three_numbers():
    """Add three numbers with error handling"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        
        result = num1 + num2 + num3
        print(f"The sum of {num1}, {num2}, and {num3} is: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the function
safe_add_three_numbers()