def outer_func():
    msg = 'Hello'

    def inner_func():
        msg = 'Hi'
        return msg

    inner_func()
    return msg

print(outer_func()) 