# 导入需要的库
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义二次指数平滑函数，输入为原始序列和平滑参数alpha，输出为平滑后的序列和预测值
def double_exponential_smoothing(series, alpha):
    # 初始化第一个点和第一个趋势
    s1 = series[0]
    b1 = series[1] - series[0]
    # 创建空列表存储平滑后的序列和预测值
    smoothed = []
    forecast = []
    # 遍历原始序列，按照公式更新s和b，并将结果添加到列表中
    for x in series:
        smoothed.append(s1 + b1)
        forecast.append(smoothed[-1] + b1)
        s2 = alpha * x + (1 - alpha) * (s1 + b1)
        b2 = alpha * (s2 - s1) + (1 - alpha) * b1
        s1 = s2
        b1 = b2
    # 返回平滑后的序列和预测值（去掉第一个点）
    return smoothed[1:], forecast[1:]

# 定义原始数据，这里是二维坐标序列
data = np.array([[  1,   2],
       [  3,   2],
       [  5,   6],
       [  3,   3],
       [  4,   6],
       [  5,   9],
       [  6,   5],
       [ 5 ,7 ],
       [8 ,5 ],
       [8 ,8 ],
       [9 ,10 ],
       [11 ,12 ]])

# 将二维坐标分成x和y两个一维数组，并转换为numpy数组方便计算
x_series = np.array(data[:,0])
y_series = np.array(data[:,1])

# 定义平滑参数alpha，这里设为0.6，可以根据需要调节
alpha = 0.6

# 调用二次指数平滑函数对x和y进行平滑，并得到预测值（这里只预测一个点）
x_smoothed, x_forecast = double_exponential_smoothing(x_series, alpha)
y_smoothed, y_forecast = double_exponential_smoothing(y_series, alpha)

# 创建三维图形对象Axes3D，并设置标题、坐标轴标签等信息
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('Original and Smoothed Series')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time')

# 定义时间轴t，从0开始递增到原始数据长度加上预测长度（这里是13）
t_series = np.arange(0,len(data)+len(x_forecast))

# 绘制原始数据点（散点图）和线条（折线图），并设置颜色、标签等信息
ax.scatter(x_series,y_series,t_series[:len(data)],c='r',label='Original Data')
ax.plot(x_series,y_series,t_series[:len(data)],c='r')

# 绘制平滑后的数据点（散点图）和线条（折线图），并设置颜色、标签等信息
ax.scatter(x_smoothed,y_smoothed,t_series[1:len(data)+len(x_forecast)-len(x_forecast)],c='b',label='Smoothed Data')
ax.plot(x_smoothed,y_smoothed,t_series[1:len(data)+len(x_forecast)-len(x_forecast)],c='b')

# 绘制预测值（散点图）和线条（折线图），并设置颜色、标签等信息
ax.scatter(x_forecast,y_forecast,t_series[len(data):],c='g',label='Forecast Data')
ax.plot(x_forecast,y_forecast,t_series[len(data):],c='g')

# 显示图例
ax.legend()

# 显示图形
plt.show()