from functools import wraps
def log(log_file):
    def dec(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            with open(log_file, 'a') as f:
                f.write(f"Calling function {func.__name__}, with args: {args} and kwargs: {kwargs}") 
            try:
                result = func(*args,**kwargs)
                with open(log_file, 'a') as f:
                    f.write(f"Function {func.__name__} returned {result}")
                return result
            except Exception as e:
                with open(log_file, 'a') as f:
                    f.write(f" Error in function {func.__name__}: {e}")
                raise
        return wrapper
    return dec

@log('log.txt')
def test():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    try:
        a//b
    except Exception as ex:
        print(ex.__class__.__name__)
    
test()