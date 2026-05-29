def garden_operations() -> None:
    """Function that  demonstrates these common errors"""

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        5 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        plants = {"rose": 1, "tulip": 2}
        print(plants["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    garden_operations()

    print("Testing multiple errors together...")

    # Check: mostrar cómo capturar varios errores a la vez
    try:
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
