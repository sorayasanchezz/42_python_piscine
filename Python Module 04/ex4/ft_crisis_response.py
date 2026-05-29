def crisis_handler(filename: str, accestype: str) -> None:
    print(f"{accestype}: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as f:
            print(f"SUCCESS: Archive recovered - ``{f.read().strip()}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, fallback protocols engaged")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt", "CRISIS ALERT")
    print()
    crisis_handler("classified_vault.txt", "CRISIS ALERT")
    print()
    crisis_handler("standard_archive.txt", "ROUTINE ACCESS")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
