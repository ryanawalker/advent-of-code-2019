masses = """
""" # input goes here as a multiline string bc i always get too lazy to set up reading from file

total = 0

for mass in masses.split("\n"):
  total += int(mass) // 3 - 2

print(f"part 1: {total}")

total = 0

for mass in masses.split("\n"):
  fuel = int(mass)
  while fuel > 0:
    fuel = fuel // 3 - 2
    if fuel > 0:
      total += fuel

print(f"part 2: {total}")
