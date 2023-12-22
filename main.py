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

def bubble_sort(nums):  
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
random_list_of_nums = gen()  
bubble_sort(random_list_of_nums)  


 

