from classuser import User
from postclass import Post

app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "James Bond", "supersecret", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()

# this is the example of OOPS
# class is a blueprint from which objects are created
# object is a real-world entity , class is a group of similar objects
# python is object oriented programming language