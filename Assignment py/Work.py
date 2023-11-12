# %%
def get_basic_price():
    basic_price = input("Enter the basic price of the vehicle: ")
    while not basic_price.isnumeric():
        print("Invalid basic price. Please enter a number.")
        basic_price = input("Enter the basic price of the vehicle: ")
    return int(basic_price)

# %%
def get_trade_in_allowance():
    trade_in = input("Enter the trade-in allowance: ")
    while not trade_in.isnumeric():
        print("Invalid trade-in allowance. Please enter a number.")
        trade_in = input("Enter the trade-in allowance: ")
    return int(trade_in)

# %%
def get_accessories():
    accessories = input("Enter the accessories: ")
    while accessories != "Stereo System" and accessories != "Leather Interior" and accessories != "GPS":
        print("Invalid accessories. Please enter Stereo System, Leather Interior, or GPS.")
        accessories = input("Enter the accessories: ")
    return accessories

# %%
def get_exterior_finish():
    exterior_finish = input("Enter the exterior finish: ")
    while exterior_finish != "Standard" and exterior_finish != "Modified" and exterior_finish != "Customized":
        print("Invalid exterior finish. Please enter Standard, Modified, or Customized.")
        exterior_finish = input("Enter the exterior finish: ")
    return exterior_finish

# %%
# write a function to calculate the total price of additional accessories based on the user's selection and use prices written above
def get_total_accessories_price(accessories):
    total_accessories_price = 0
    if accessories == "Stereo System":
        total_accessories_price = 30.50
    elif accessories == "Leather Interior":
        total_accessories_price = 530.99
    elif accessories == "GPS":
        total_accessories_price = 301.90
    return float(total_accessories_price)


def get_exterior_finish_price(exterior_finish):
    if exterior_finish == "Standard":
        exterior_finish_price = 0
    elif exterior_finish == "Modified":
        exterior_finish_price = 370.50
    elif exterior_finish == "Customized":
        exterior_finish_price = 1257.99
    return float(exterior_finish_price)


def get_subtotal(basic_price, total_accessories_price, exterior_finish_price):
    subtotal = basic_price + total_accessories_price + exterior_finish_price
    return float(subtotal)



def get_sales_tax(subtotal, sales_tax_rate):
    sales_tax = subtotal * sales_tax_rate
    return float(sales_tax)
def get_amount_due(sales_tax, subtotal, trade_in_allowance):
    if trade_in_allowance is None:
        trade_in_allowance = 0
    amount_due = sales_tax + subtotal - float(trade_in_allowance)
    return amount_due


def display_results(subtotal, sales_tax, amount_due):
    print("Subtotal: ", subtotal)
    print("Sales Tax: ", sales_tax)
    print("Amount Due: ", amount_due)


# %%
import sys

def reset():
    clear_screen()
    main()

def clear_screen():
    basic_price = 0
    trade_in_allowance = 0
    accessories = ""
    total_accessories_price = 0
    exterior_finish = ""
    exterior_finish_price = 0
    subtotal = 0
    sales_tax = 0
    amount_due = 0
    
def main():
    sales_tax_rate = 0.08
    basic_price = get_basic_price()
    trade_in_allowance = get_trade_in_allowance()
    accessories = get_accessories()
    total_accessories_price = get_total_accessories_price(accessories)
    exterior_finish = get_exterior_finish()
    exterior_finish_price = get_exterior_finish_price(exterior_finish)
    subtotal = get_subtotal(basic_price, total_accessories_price, exterior_finish_price)
    sales_tax = get_sales_tax(subtotal, sales_tax_rate)
    amount_due = get_amount_due(sales_tax, subtotal, trade_in_allowance)
    display_results(subtotal, sales_tax, amount_due)

    
    while True:
        key = input("Press 'c' to clear, 'r' to reset, 'x' to exit, or any other key to continue: ")
        if key.lower() == 'c':
            clear_screen()
        elif key.lower() == 'r':
            main()
        elif key.lower() == 'x':
            sys.exit()
        elif key == chr(27):
            sys.exit()
        else:
            break



main()