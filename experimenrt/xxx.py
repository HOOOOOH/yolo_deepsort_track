import numpy as np

# 定义系统模型
A = np.array([[1, 0], [0, 1]])  # 状态转移矩阵
H = np.array([[1, 0], [0, 1]])  # 观测矩阵
Q = np.array([[0.01, 0], [0, 0.01]])  # 系统噪声协方差矩阵
R = np.array([[1, 0], [0, 1]])  # 观测噪声协方差矩阵

# 初始化状态和误差协方差
x = np.array([0, 0])  # 初始状态
P = np.array([[10000, 0], [0, 10000]])  # 初始误差协方差

# 定义观测序列
z = np.array([[1, 2], [3, 2], [5, 6], [3, 3], [4, 6], [5, 9], [6, 5], [5, 7], [8, 5], [8, 8], [9,10],[9,10],[9,10],[19,20]])

# 进行卡尔曼滤波
for i in range(len(z)):
    # 预测步骤
    x_pred = A.dot(x)  # 预测状态
    P_pred = A.dot(P).dot(A.T) + Q  # 预测误差协方差

    # 更新步骤
    K = P_pred.dot(H.T).dot(np.linalg.inv(H.dot(P_pred).dot(H.T) + R))  # 计算卡尔曼增益
    x = x_pred + K.dot(z[i] - H.dot(x_pred))  # 更新状态估计
    P = (np.eye(2) - K.dot(H)).dot(P_pred)  # 更新误差协方差

    print(f"第{i + 1}次观测后的状态估计为：{x}")