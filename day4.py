valid_passwords_1, valid_passwords_2 = [], []

def is_valid_1(password):
  password_str = str(password)
  has_doubles = False
  for idx in range(len(password_str) - 1):
      if password_str[idx] > password_str[idx + 1]:
          return False
      elif password_str[idx] == password_str[idx + 1]:
          has_doubles = True
  return has_doubles


def is_valid_2(password):
  num_seen = 1
  has_doubles = False
  password_str = str(password)

  for idx in range(len(password_str) - 1):
      if password_str[idx] > password_str[idx + 1]:
          return False
      if password_str[idx] == password_str[idx + 1]:
          num_seen += 1
      else:
        if not has_doubles:
          has_doubles = num_seen == 2
        num_seen = 1
  if has_doubles or num_seen == 2:
    return True
  else:
    return False

for password in range(153517, 630396):
  if is_valid_1(password):
     valid_passwords_1.append(password)
  if is_valid_2(password):
     valid_passwords_2.append(password)
  

print(len(valid_passwords_1))
print(len(valid_passwords_2))
