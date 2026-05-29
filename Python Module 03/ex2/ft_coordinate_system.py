import math


def calculate_distance(point1: tuple[float, float, float],
                       point2: tuple[float, float, float]) -> float:
    """Calculate the 3D Euclidean distance between two points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    """Parse a string like '3,4,0' into a tuple of integers."""
    parsed_coord = coord_str.split(",")
    x = int(parsed_coord[0])
    y = int(parsed_coord[1])
    z = int(parsed_coord[2])
    return (x, y, z)


def parse_and_calculate(input_coord: str) -> tuple[int, int, int]:
    """
    Parse a coordinate string (e.g., '3,4,0') into a tuple of integers.
    Raise an error if the input does not contain exactly three numeric values.
    """
    origin = (0, 0, 0)

    try:
        parsed_coord = parse_coordinates(input_coord)
        print('Parsed position:', parsed_coord)
        print(f'Distance between {origin} and {parsed_coord}: '
              f'{calculate_distance(origin, parsed_coord):.1f}')

    except (ValueError, IndexError) as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        raise

    return parsed_coord


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    x, y, z = 0, 0, 0

    # basic case (without parse)
    position = (10, 20, 5)
    print("Position created:", position)
    print(f"Distance between {origin} and {position}: "
          f"{calculate_distance(origin, position):.2f}")

    # parse case
    print('\nParsing coordinates: "3,4,0"')
    try:
        x, y, z = parse_and_calculate("3,4,0")
    except (ValueError, IndexError):
        pass

    # invalid case
    print('\nParsing invalid coordinates: "abc,def,ghi"')
    try:
        x, y, z = parse_and_calculate("abc,def,ghi")
    except (ValueError, IndexError):
        pass

    print("\nUnpacking demonstration:\n"
          f"Player at x={x}, y={y}, z={z}\n"
          f"Coordinates: X={x}, Y={y}, Z={z}")
