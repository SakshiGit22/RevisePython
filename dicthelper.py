# create a module and import a statement

def price(quantity, conversion_unit):
    print(quantity > 0)
    print(type(quantity > 0))
    if conversion_unit == "hours":
        return f"{quantity} days are {quantity * 24} hours"
    elif conversion_unit == "minutes":
        return f"{quantity} days are {quantity * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate(dict1):
    try:
        user_input_int = int(dict1["days"])
        if user_input_int > 0:
            total_price = price(user_input_int, dict1["unit"])
            print(total_price)
        elif user_input_int == 0:
            print("zero input")
        else:
            print("negative number")
    except ValueError:
        print("invalid input")


input_msg = "number of days and conversion unit\n"
