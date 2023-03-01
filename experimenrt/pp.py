import numpy as np
import matplotlib.pyplot as plt
import queue

#卡尔曼滤波参数
A = np.array([[1, 0], [0, 1]])  # 状态转移矩阵
H = np.array([[1, 0], [0, 1]])  # 观测矩阵
Q = np.array([[0.001, 0], [0, 0.001]])  # 系统噪声协方差矩阵
R = np.array([[1, 0], [0, 1]])  # 观测噪声协方差矩阵

# 初始化状态和误差协方差
x = np.array([0, 0])  # 初始状态
P = np.array([[1000, 0], [0, 1000]])  # 初始误差协方差


# 定义卡尔曼滤波函数
def kalman_filter(now):
    global x, P
    # 进行卡尔曼滤波
    for i in range(len(now)):
        # 预测步骤
        x_pred = A.dot(x)
        P_pred = A.dot(P).dot(A.T) + Q

        # 更新步骤
        K = P_pred.dot(H.T).dot(np.linalg.inv(H.dot(P_pred).dot(H.T) + R))
        x = x_pred + K.dot(now[i] - H.dot(x_pred))
        P = (np.eye(2) - K.dot(H)).dot(P_pred)
    return x
while True:
    # 输入当前观测值
    now = input("请输入当前观测值：")
    now = now.split(',')
    now = [int(i) for i in now]
    now = np.array(now)
    # 进行卡尔曼滤波
    result = kalman_filter(now)
    print(f"当前预测值为：{result}")






