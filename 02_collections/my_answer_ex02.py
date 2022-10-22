# -*- coding: utf-8 -*-

# def number():
#   x = [1,2,3]
#   print(len(x))
#   for i, x in enumerate(x):
#       print(i, x)
  
# if __name__ == "__main__":
#   number()

# def name():
#   names = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
#   for i, x in enumerate(name):
#     if(x == 'Angy'):
#       print("{0} My name is {1}" .format(i+1, x))
#     else:
#       print("{0}.{1} is my classmate" .format(i+1, x))

# if __name__ == "__main__":
#   name()

def name(names):
  def get_format(is_angy):
    return "{0}.My name is {1}" if is_angy else "{0}.{1} is my classmate"

  for i, n in enumerate(names):
    print(get_format(n == "Angy").format(i+1, n))

if __name__ == "__main__":
  names = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
  name(names)


