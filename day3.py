lines = """
""".split("\n") # input goes here

line_1 = lines[0].split(",")
line_2 = lines[1].split(",")

line_locations = [{}, {}]

steps, step_2 = 0, 0

dir_dict = {"U": (1, 1), "R": (0, 1), "D": (1, -1), "L": (0, -1)}

for idx, line in enumerate([line_1, line_2]):
  steps = 0
  line_location = [0, 0]

  for instruction in line:
    direction = instruction[0]
    distance = int(instruction[1:])
    loc_target, loc_incr = dir_dict[direction]
    for i in range(distance):
      steps += 1
      line_location[loc_target] += loc_incr
      line_locations[idx][tuple(line_location)] = steps

cross_distances = set()
cross_steps = set()

for location in line_locations[0]:
  if location in line_locations[1]:
    cross_distances.add(abs(location[0]) + abs(location[1]))
    cross_steps.add(line_locations[0][location] + line_locations[1][location])

print(min(cross_distances)) # part 1
print(min(cross_steps)) # part 2
