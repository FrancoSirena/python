j_array = ["some", 0, 2, 3]
j_dict = {"key": 10, "other_key": "other_value"}
j_tuple = ("some", "value", "other_one")

first_value, second_value, third_value = j_tuple

"""
  reading tuple
"""
print("Tuple")
for j in j_tuple:
  print(j)

"""
  reading array
"""
print("Array")
for i in j_array:
  print(i)

"""
  reading dict
"""
print("Dict")
for k in j_dict:
  print(f"key {k}")
  print(f"value {j_dict[k]}")

for k, v in j_dict.items():
  print(k, v)


"""
  Checking for value in dict
"""
if "key" in j_dict:
  print("fount key")

if not "Key1" in j_dict:
  print("Not found Key1")
