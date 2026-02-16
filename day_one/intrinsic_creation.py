import numpy as np

# 从一个范围的元素创建数组
# np.arange(start, stop, step) - 类似于 Python 的 range()
# 用例：为循环创建序列，生成索引
arr_range = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
print("Array from arange:")
print(arr_range)

# 在两个点之间创建具有特定数量元素的数组
# np.linspace(start, stop, num_elements) - 等间距的点
# 用例：为绘图创建点，采样数据
arr_linspace = np.linspace(0, 10, 5)  # 5 个从 0 到 10 的点
print("\nArray from linspace:")
print(arr_linspace)

# 创建一个全为零的数组
# np.zeros((rows, columns)) - 为计算预分配数组
# 用例：在填充计算值之前预先分配数组
arr_zeros = np.zeros((2, 3))  # 2x3 的零数组
print("\nArray of zeros:")
print(arr_zeros)

# 创建一个全为一的数组
# np.ones((rows, columns)) - 用一初始化
# 用例：创建掩码、缩放因子或算法的起始点
arr_ones = np.ones((3, 2))  # 3x2 的一数组
print("\nArray of ones:")
print(arr_ones)

# 创建一个单位矩阵
# np.eye(size) - 对角线上为 1，其余为 0 的方阵
# 用例：线性代数、重置变换、矩阵乘法
identity_matrix = np.eye(3)  # 3x3 单位矩阵
print("\nIdentity matrix:")
print(identity_matrix)