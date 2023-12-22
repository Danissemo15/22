'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import time
import random
N = 10000
def run():
    i = 0
    while i < 100000000:
        i += 1 
start = time.time()
run()
end = time.time() - start
print(f"Время выполнения: {end}")

def gen():
    a = []
    for i in range (N):
        a.append(random.randint(1,10000))
    return a

def selection_sort(nums):  
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
random_list_of_nums = gen()  
selection_sort(random_list_of_nums)  


