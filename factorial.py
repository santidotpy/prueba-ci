def factorial(num:int):
    if num in (0, 1):
        return 1
    else:
        return (num * factorial(num-1))