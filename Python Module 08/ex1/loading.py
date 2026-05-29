try:
    import numpy as np
    import pandas as pd
    import requests
    import matplotlib as mtl
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print(f"ERROR: '{e.name}' module is not installed\n\n"
          "You can fulfill all the required dependencies with:\n"
          " - PIP: 'pip install -r requirements.txt'\n"
          " - Poetry: 'poetry install' and 'poetry run python loading.py'")
    exit(1)


def check_dependencies() -> None:
    print("Checking dependencies:\n"
          f"[OK] pandas ({pd.__version__}) - Data manipulation ready\n"
          f"[OK] numpy ({np.__version__}) - Numerical computation ready\n"
          f"[OK] requests ({requests.__version__}) - Network access ready\n"
          f"[OK] matplotlib ({mtl.__version__}) - Visualization ready\n")


def use_packages() -> None:
    # Numpy: random sales in a week
    print("Analyzing Matrix data...")
    daily_sales = np.random.randint(0, 101, 7)

    # Pandas: table (Data Frame) and column
    print(f"Processing {len(daily_sales)} data points...")
    df = pd.DataFrame({
        "day": range(1, 8),
        "sales": daily_sales})

    # Matplotlib: visualization
    print("Generating visualization...")
    plt.plot(df["day"], df["sales"])
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!\n"
          "Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    check_dependencies()
    use_packages()
