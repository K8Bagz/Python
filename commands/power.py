def power(base, exponent):
    if exponent < 0:
        raise ValueError("The exponent must be greater than or equal to zero.")

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)
    # or return pow(base, exponent) 
    # or return base ** exponent

def run():
    base = int(input("Base: "))
    exponent = int(input("Exponent: "))

    print(power(base, exponent))