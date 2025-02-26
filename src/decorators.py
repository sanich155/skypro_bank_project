from functools import wraps


def log(filename=None):
    def wrapped(function):
        @wraps(function)
        def inner(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except Exception as err:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} error: {str(err)}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{function.__name__} error: {str(err)}. Inputs: {args}, {kwargs}")
            else:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} ok\n" f"{result}\n")
                else:
                    print(f"{function.__name__} ok\n" f"{result}")

        return inner

    return wrapped
