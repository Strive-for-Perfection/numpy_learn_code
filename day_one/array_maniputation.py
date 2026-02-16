import numpy as np

# --- Part 1: Views vs. Copies ---
a = np.arange(1, 5)
print("Original array 'a':", a)

# 创建一个包含前两个元素的视图
b = a[:2]
b[0] = 99 # 修改视图
print("Modified view 'b':", b)
print("Array 'a' after modifying the view:", a) # 'a' 也被改变了

# 创建一个副本
c = a[:2].copy()
c[0] = 0 # 修改副本
print("\nModified copy 'c':", c)
print("Array 'a' after modifying the copy:", a) # 'a' 未改变

# --- Part 2: Joining Arrays ---
A = np.ones((2, 2))
B = np.eye(2) * 2
C = np.zeros((2, 2))
D = np.diag((-3, -4))

# 将数组组合成一个块矩阵
block_matrix = np.block([
    [A, B],
    [C, D]
])
print("\nBlock matrix:")
print(block_matrix)