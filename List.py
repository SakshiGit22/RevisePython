# list
my_list = ["Jan", "Feb", "Mar"]
print(my_list[0])
my_list.append("Apr")
print(my_list)

"""for multiline comment"""

# set does not allow duplicate values

my_set = {"January", "February", "March"}
# items in set can not be referred by index
# items does not have defined order
# items can not be changed

for element in my_set:
    print(element)

my_set.add("April")
# it will get added to any unknown index
print(my_set)
my_set.remove("January")
print(my_set)

my_list.remove("Jan")
print(my_list)

