# 导入numpy和matplotlib库
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义二维序列
data = np.array([[1,2],[3,2],[5,6],[3,3],[4,6],[5,9],[6,5],[5,7],[8,5],[8,8],[9,10],[11,12]])

# 定义卷积核函数
kernel = np.array([0.3, 0.4 , 0.3])

# 使用卷积对二维序列进行平滑
smoothed_data = np.convolve(data[:,0], kernel , mode='same'),np.convolve(data[:,1], kernel , mode='same')
smoothed_data = np.array(smoothed_data).T

# 创建三维图形对象
fig = plt.figure()
ax = fig.add_subplot(111 , projection='3d')

# 绘制原始序列和平滑后的序列
ax.plot(data[:,0], data[:,1], range(len(data)), label='original')
ax.plot(smoothed_data[:,0], smoothed_data[:,1], range(len(smoothed_data)), label='smoothed')

# 设置图形标题和坐标轴标签
ax.set_title('Smoothing a 2D sequence using convolution')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图例
plt.legend()

# 显示图形
plt.show()