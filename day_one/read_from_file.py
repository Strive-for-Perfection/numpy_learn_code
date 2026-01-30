import numpy as np

# 从 CSV 文件加载数据
try:
    # 相对路径会导致验证失败，请在实验中使用绝对路径
    data = np.loadtxt('/home/yiyepianzhou/miniconda3/envs/ml_env/bin/numpy_learn_code/data.csv', delimiter=',', skiprows=1)
    print("Data loaded from data.csv:")
    print(data)
except IOError:
    print("Error: data.csv not found.")