def say_hello():
    global age
    age += 2
    print('You are', age)

age = 12
say_hello()
print('real age:', age)





