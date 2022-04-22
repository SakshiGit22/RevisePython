print(10)
print("200 is great")
print('200 is great')
print(-10)
print(20.9)

print(f"total price {50} done")
print("total price is " + str(50) + " done1")
print(f"20 days are {20 * 24 * 60} minutes")
print("10 days are " + str(10 * 24 * 60) + " minutes")

no_of_seconds = 15 * 24 * 60
name_minutes = "minutes ok"
print(f"15 days are {no_of_seconds} {name_minutes}")


# functions


def price_calculation(days, msg):
    print(f"{days} days are {days * no_of_seconds} {name_minutes}")
    print(msg)


price_calculation(15, "awesome")
price_calculation(10, "okay")
price_calculation(20, "good")


# global variables can be accessed by all functions
# local variable restricted to only functions

# user input validation
def price(quantity):
    print(quantity > 0)
    print(type(quantity > 0))
    return f"total amt to be paid for {quantity} books is {quantity * 20}"


def validate():
    try:

        user_input_int = int(i)
        if user_input_int > 0:
            total_price = price(user_input_int)
            print(total_price)
        elif user_input_int == 0:
            print("zero input")
        else:
            print("negative number")
    except ValueError:
        print("invalid input")


# split(",") makes "10 20 30" to [10, 20, 30]


user_input = ""
while user_input != "exit":
    user_input = input("number of books required\n")
    list1 = user_input.split(", ")
    print(list1)
    print(set(list1))
    print(type(list1))
    print(type(set(list1)))

    for i in set(list1):
        validate()

# set does not allow duplicate values
# user_input.split(" ,")
# if user_input.isdigit():
# input() takes input as string so convert to number ; do casting int(input1)
