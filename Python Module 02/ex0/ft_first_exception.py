def check_temperature(temp_str: str) -> int | None:
    """
    Validate a temperature string.

    Returns the temperature if it is within the plant-safe range (0–40°C),
    otherwise (if it is not a number) returns None.
    """

    try:
        temp_nbr = int(temp_str)

        if temp_nbr > 40:
            print(f"Error: {temp_nbr}°C is too hot for plants (max 40°C)")
            return None

        if temp_nbr < 0:
            print(f"Error: {temp_nbr}°C is too cold for plants (min 0°C)")
            return None

        print(f"Temperature {temp_nbr}°C is perfect for plants!")
        return temp_nbr

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    """Tester, (all tests are written in the test list)"""

    print("=== Garden Temperature Checker ===\n")

    tests = ["25", "abc", "100", "-50"]

    for temp in tests:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
