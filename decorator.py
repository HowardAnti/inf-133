from functools import wraps

def my_decorator(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hola, {name}"

greet("Juan")

print(greet.__name__)
print(greet.__doc__)
