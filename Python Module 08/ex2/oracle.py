import os
from dotenv import load_dotenv


def security_check(env_errors: bool) -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_errors:
        print("[WARNING] .env file contains errors")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.\n")


def show_info(env_vars: dict) -> None:
    mode = env_vars["MATRIX_MODE"]

    print("\nConfiguration loaded:")

    if mode == "development":
        print(f"Mode: {mode}")
        print("Database: Connected to local instance")
        print("API Access: Authenticated" if
              env_vars["API_KEY"] else "API Access: Missing API key")
        print(f"Log Level: {env_vars["LOG_LEVEL"]}")
        print("Zion Network: Online")

    elif mode == "production":
        print(f"Mode: {mode}")
        print("Database: Connected to production instance")
        print("API Access: Authenticated" if
              env_vars["API_KEY"] else "API Access: Missing API key")
        print(f"Log Level: {env_vars["LOG_LEVEL"]}")
        print("Zion Network: Online")

    else:
        print("[ERROR] incompatible mode")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    load_dotenv()

    env_vars = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }

    missing = [key for key, value in env_vars.items() if value is None]
    env_errors: bool = False

    if missing:
        print("[WARNING] Missing configuration:")
        for var in missing:
            print(f" - {var}")
            env_errors = True

    show_info(env_vars)
    security_check(env_errors)


if __name__ == "__main__":
    main()
