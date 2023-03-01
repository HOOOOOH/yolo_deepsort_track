import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox, QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class MultiPersonDetection(QWidget):
    def __init__(self, num_people, person_names, x, y):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle('多人检测')

        # 设置窗口大小
        self.setFixedSize(1000, 800)

        # 创建按键
        self.button = QPushButton(self)
        self.button.setText('开始检测')
        self.button.setGeometry(200, 150, 300, 100)
        self.button.clicked.connect(self.toggle_detection)

        # 创建图片显示区域
        self.image_label = QLabel(self)
        self.image_label.setGeometry(400, 50, 400, 500)
        self.image_label.setAlignment(Qt.AlignCenter)

        # 创建文字注释
        self.text_label = QLabel('检测结果', self)
        self.text_label.setGeometry(400, 10, 100, 30)

        # 创建下拉菜单
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(690, 10, 100, 30)
        self.combo_box.addItem('请开始检测')
        for i in range(num_people):
            self.combo_box.addItem(person_names[i])

        # 创建文本框
        self.text_box = QLineEdit(self)
        self.text_box.setGeometry(690, 550, 100, 30)
        self.text_box.setStyleSheet('border: 1px solid gray')
        self.text_box.setText(f'X: {x} Y: {y}')

        # 初始化检测状态
        self.detecting = False

    def toggle_detection(self):
        self.detecting = not self.detecting
        if self.detecting:
            self.button.setText('停止检测')
        else:
            self.button.setText('开始检测')

    def show_image(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.resize(image, (600, 800))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QPixmap.fromImage(QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888))
        self.image_label.setPixmap(q_image)
        self.image_label.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 定义菜单栏选项
    num_people = 3
    person_names = ['Person 1', 'Person 2', 'Person 3']

    # 定义文本框参数
    x = 100
    y = 200

    # 创建窗口
    window = MultiPersonDetection(num_people, person_names, x, y)
    window.show()

    sys.exit(app.exec_())