def init_memory():
  return list(map(int, "".split(","))) # input goes into the string

def run_program(noun, verb):
  array = init_memory()

  array[1] = noun
  array[2] = verb

  idx = 0

  while True:
    op = array[idx]

    if op == 99:
      break

    loc1 = array[idx + 1]
    loc2 = array[idx + 2]
    target = array[idx + 3]
    
    if op == 1:
      array[target] = array[loc1] + array[loc2]
    elif op == 2:
      array[target] = array[loc1] * array[loc2]
    
    idx += 4

  return array[0]

target = 19690720

for i in range(0, 100):
  for j in range(0, 100):
    if run_program(i, j) == target:
      print(100 * i + j)
      break
  else:
    continue
  break
