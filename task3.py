import random

def generate_array(N):
    return [random.randint(1, 50) for _ in range(N)]

def calculate_and_print(array):
    odd_elements = [x for x in array if x % 2 != 0]

    if odd_elements:
        average = sum(odd_elements) / len(odd_elements)
        print(f"Середнє арифметичне непарних елементів: {average:.2f}")
    else:
        print("У масиві немає непарних елементів.")

    negative_elements = [x for x in array if x < 0]
    if negative_elements:
        print("Від'ємні елементи масиву:")
        for element in negative_elements:
            print(element)

N = 100

array = generate_array(N)
calculate_and_print(array)
