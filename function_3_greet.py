def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

#print(compose_greet_func())
greet = compose_greet_func()
print(greet())