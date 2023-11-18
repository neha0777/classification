import random
random_integers = [random.randint(1, 100) for _ in range(10)]
odd_list = []
even_list = []

for num in random_integers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Random Integers List:", random_integers)
print("Odd List:", odd_list)
print("Even List:", even_list)
