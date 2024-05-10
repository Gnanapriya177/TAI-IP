def payment(amount):
    print(f"Processing Your payment of {amount}")
    print("Your Payment is successful!!!")

def main_function():
    try:
        amount = float(input("Enter payment amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a positive number")
        
        payment(amount)
    except ValueError as error:
        print(f"Error: {error}")
        print("Payment failed... Enter a valid amount")

if __name__ == "__main__":
    main_function()

