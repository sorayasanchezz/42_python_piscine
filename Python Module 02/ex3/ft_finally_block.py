def water_plants(plant_list: list) -> None:
    """Program that protects invalid args (None and Numbers)"""

    print("Opening watering system")

    try:
        for plant in plant_list:
            if not isinstance(plant, str) or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    try:
        print("\nTesting normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfully!")
    except Exception:
        pass
    finally:
        print()

    try:
        print("Testing with error...")
        water_plants(["tomato", None, "lettuce", "carrots"])
    except Exception:
        pass
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
