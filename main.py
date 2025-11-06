import calc_actions

def main():
    """A simple calculator program."""
    print("Welcome to the simple calculator!")
    print("Let's demonstrate the available functions.")

    a = 10
    b = 5

    print(f"{a} + {b} = {calc_actions.add(a, b)}")
    print(f"{a} - {b} = {calc_actions.subtract(a, b)}")
    print(f"{a} * {b} = {calc_actions.multiply(a, b)}")
    print(f"{a} / {b} = {calc_actions.divide(a, b)}")
    print(f"{a} ** {b} = {calc_actions.power(a, b)}")
    print(f"{a} % {b} = {calc_actions.modulo(a, b)}")

if __name__ == "__main__":
    main()
