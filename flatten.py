from typing import List

def flatten(items: list, values: list) -> List[int]:
  for item in items:
    if not isinstance(item, list):
      values.append(item)
    else:
      flatten(item, values)
  return values

# print(flatten([1, [2, [3, [4, 5]]]], []))