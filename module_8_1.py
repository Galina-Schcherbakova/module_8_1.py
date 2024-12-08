def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return format(a + b, '.3f')
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return format(a, '.3f') + b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return a + str(int(b))
        else:
            raise TypeError("Типы аргументов различаются.")
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
