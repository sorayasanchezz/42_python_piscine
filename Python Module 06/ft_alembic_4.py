import alchemy

print("=== Alembic 4 ===\n"
      "Accessing the alchemy module using 'import alchemy'\n"
      "Testing create_air:", alchemy.create_air())

print("Now show that not all functions can be reached\n"
      "This will raise an exception!\n"
      "Testing the hidden create_earth: ", end="")

print(alchemy.create_earth())
