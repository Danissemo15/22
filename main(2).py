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

def insertion_sort(nums):  
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert
random_list_of_nums = gen()  
insertion_sort(random_list_of_nums) 

