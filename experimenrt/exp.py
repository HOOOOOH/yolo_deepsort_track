import cv2

cap = cv2.VideoCapture(0)

# 获取摄像头支持的所有分辨率
supported_resolutions = []
for i in range(100):
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    if width == 0 or height == 0:
        break
    supported_resolutions.append((int(width), int(height)))
    cap.read()

# 选择最大的分辨率
max_resolution = max(supported_resolutions)

# 设置摄像头分辨率
cap.set(cv2.CAP_PROP_FRAME_WIDTH, max_resolution[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, max_resolution[1])