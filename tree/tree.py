from random import seed
from random import randint
from datetime import datetime

class Tree:
  def __init__(self, root):
    self.root = root

  def __str__(self):
    return f"[TREE:{self.root}]"

  def add(self, value):
    return self.root.add(value)

  def find(self, value):
    return self.root.find(value)

  def add_from_list(self, l):
    for i in l:
      self.root.add(i)

  def get_tall_by(self, direction=0):
    tall_left = self.root
    tall_right = self.root
    left, right = self.root.get_height()
    next = self.root.left if direction == 0 else self.root.right
    while not next is None:
      n_left, n_right = next.get_height()
      if n_left > left:
        tall_left = next
        left = n_left
      
      if n_right > right:
        tall_right = next
        right = n_right

      next = next.left if direction == 0 else next.right
    
    return (tall_left, left, tall_right, right)

  def get_tallest(self):
    tl1, l1, tr1, r1 = self.get_tall_by()
    tl2, l2, tr2, r2 = self.get_tall_by(1)

    left = (tl1.value, l1) if l1 > l2 else (tl2.value, l2)
    right = (tr1.value, r1) if r1 > r2 else (tr2.value, r2)

    return {left, right}

class Node:
  def __init__(self, value, right=None, left=None):
    self.value = value
    self.right = right
    self.left = left
  
  def __str__(self):
    return f"\n value ->{self.value} \n${self.value}right: {self.right} \n${self.value}left: {self.left}"

  def add(self, value):
    if self.value == value:
      return self

    if self.value > value and self.left is None:
      self.left = Node(value)
    elif self.value < value and self.right is None:
      self.right = Node(value)
    else:
      if self.value < value:
        self.right.add(value)
      else:
        self.left.add(value)
    
  def find(self, value):
    if self.value == value:
      return self

    if value > self.value:
      if self.right is None:
        return None

      return self.right.find(value)
    else:
      if self.left is None:
        return None

      return self.left.find(value)
  
  def get_height(self, direction=0, right=0, left=0):
    left_height = left
    right_height = right
    if not self.left is None and direction in (0, 1):
      count = left + 1
      left_height, _ = self.left.get_height(1, 0, count)

    if not self.right is None and direction in (0, 2):
      count = right + 1
      _, right_height = self.right.get_height(2, count, 0)

    return (left_height, right_height)

if __name__ == '__main__':
  t = Tree(Node(10))
  # l = [9, 8, 100, 99, 98, 97, 101, 110, 112, 7, -20, -19, -18, -17, -16, -15, -30, -25, -14, 90, 88, 86]
  # t.add_from_list(l)
  seed(1)
  for l in range(0, 10000):
     t.add(randint(-l, l))
  print(f"{datetime.now()}")
  print(f"{t.get_tallest()}")
  print(f"{datetime.now()}")

