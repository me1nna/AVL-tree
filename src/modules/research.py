import time, random
from main import *

'''Исследование'''
avl_tree1 = AVLTree()
avl_tree2 = AVLTree()
avl_tree3 = AVLTree()
avl_tree4 = AVLTree()
avl_tree5 = AVLTree()

for _ in range(10 ** 1):
    avl_tree1.insert_val(random.randint(-1000, 1000))

for _ in range(10 ** 2):
    avl_tree2.insert_val(random.randint(-1000, 1000))

for _ in range(10 ** 3):
    avl_tree3.insert_val(random.randint(-1000, 1000))

for _ in range(10 ** 4):
    avl_tree4.insert_val(random.randint(-1000, 1000))

for _ in range(10 ** 5):
    avl_tree5.insert_val(random.randint(-1000, 1000))

start = time.time()
avl_tree1.insert_val(random.randint(-1000, 1000))
end = time.time()
print(f"Вставка в дерево 10^1 {end - start}")

start = time.time()
avl_tree2.insert_val(random.randint(-1000, 1000))
end = time.time()
print(f"Вставка в дерево 10^2 {end - start}")

start = time.time()
avl_tree3.insert_val(random.randint(-1000, 1000))
end = time.time()
print(f"Вставка в дерево 10^3 {end - start}")

start = time.time()
avl_tree4.insert_val(random.randint(-1000, 1000))
end = time.time()
print(f"Вставка в дерево 10^4 {end - start}")

start = time.time()
avl_tree5.insert_val(random.randint(-1000, 1000))
end = time.time()
print(f"Вставка в дерево 10^5 {end - start}")

start = time.time()
avl_tree1.deleteMin()
end = time.time()
print(f"Удаление минимального в дереве 10^1 {end - start}")

start = time.time()
avl_tree2.deleteMin()
end = time.time()
print(f"Удаление минимального в дереве 10^2 {end - start}")

start = time.time()
avl_tree3.deleteMin()
end = time.time()
print(f"Удаление минимального в дереве 10^3 {end - start}")

start = time.time()
avl_tree4.deleteMin()
end = time.time()
print(f"Удаление минимального в дереве 10^4 {end - start}")

start = time.time()
avl_tree5.deleteMin()
end = time.time()
print(f"Удаление минимального в дереве 10^4 {end - start}")