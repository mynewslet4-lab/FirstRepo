import argparse
from calc_actions import add, subtract, multiply, divide, power, modulo

def main():
    parser = argparse.ArgumentParser(description="A simple command-line calculator.")
    subparsers = parser.add_subparsers(dest="operation", help="The operation to perform.")

    # Add operation
    parser_add = subparsers.add_parser("add", help="Add two numbers.")
    parser_add.add_argument("a", type=float, help="The first number.")
    parser_add.add_argument("b", type=float, help="The second number.")

    # Subtract operation
    parser_subtract = subparsers.add_parser("subtract", help="Subtract two numbers.")
    parser_subtract.add_argument("a", type=float, help="The first number.")
    parser_subtract.add_argument("b", type=float, help="The second number.")

    # Multiply operation
    parser_multiply = subparsers.add_parser("multiply", help="Multiply two numbers.")
    parser_multiply.add_argument("a", type=float, help="The first number.")
    parser_multiply.add_argument("b", type=float, help="The second number.")

    # Divide operation
    parser_divide = subparsers.add_parser("divide", help="Divide two numbers.")
    parser_divide.add_argument("a", type=float, help="The first number.")
    parser_divide.add_argument("b", type=float, help="The second number.")

    # Power operation
    parser_power = subparsers.add_parser("power", help="Raise a number to a power.")
    parser_power.add_argument("a", type=float, help="The base.")
    parser_power.add_argument("b", type=float, help="The exponent.")

    # Modulo operation
    parser_modulo = subparsers.add_parser("modulo", help="Calculate the modulo of two numbers.")
    parser_modulo.add_argument("a", type=float, help="The dividend.")
    parser_modulo.add_argument("b", type=float, help="The divisor.")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.a, args.b)
    elif args.operation == "subtract":
        result = subtract(args.a, args.b)
    elif args.operation == "multiply":
        result = multiply(args.a, args.b)
    elif args.operation == "divide":
        result = divide(args.a, args.b)
    elif args.operation == "power":
        result = power(args.a, args.b)
    elif args.operation == "modulo":
        result = modulo(args.a, args.b)
    else:
        parser.print_help()
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
