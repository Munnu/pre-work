animals = ["dog", "cat", "kangaroo", "elephant", "kiwi", "rhino"]
k_animals_list = []

def k_animals(animals_list, k_animals_list):
  for animal in animals_list:
    if animal.startswith("k"):
      k_animals_list.append(animal)
  return k_animals_list 

k_animals_list = k_animals(animals, k_animals_list)

print "Here is the list of animals that start with the letter k:",
for animal in k_animals_list:
  print animal,
