
def hello():
    print("hello!")
    
greet = hello

del hello   
# here the function is not deleted, just the keyword, because greet is still pointing to the function memory
# and python has not deleted it
#(hello()  # this will give error, because it has been deleted
print(greet)
greet()
