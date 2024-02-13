# tip_calculator.py

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = calculate_tip(dollars, percent)
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove the leading $ and convert to float
    return float(d[1:])

def percent_to_float(p):
    # Remove the trailing % and convert to float
    return float(p[:-1]) / 100

def calculate_tip(dollars, percent):
    # Calculate and return the tip amount
    return dollars * percent

if __name__ == "__main__":
    main()
