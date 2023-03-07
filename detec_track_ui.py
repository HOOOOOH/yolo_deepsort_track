# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\detec_track_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import imutils
import sys
import math
import queue
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtGui import QPixmap, QImage
from AIDetector_pytorch import Detector
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Ui_Dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_fun()
        self.initTimer()
        self.det = Detector()
        self.setWindowState(QtCore.Qt.WindowActive)
        self.raise_()
        self.detecting = False
        self.tracking = 0
        self.cap = None
        self.cap_width = 1920
        self.cap_height = 1080
        self.cameras = 1 #'dance_demo.mp4'  # 'address.txt'
        self.current_id = None
        self.track_id = None
        self.track_id_pos = []
        self.track_id_speed = 0
        self.queue = queue.Queue()
        self.time_cost = 0


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start_button.setText(_translate("Dialog", "开始检测"))
        self.choose_id_button.setText(_translate("Dialog", "初始化"))
        self.onoff_button.setText(_translate("Dialog", "追踪开关"))
        self.pic_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">视频显示区域</p></body></html>"))
        self.id_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">追踪人员选择</p></body></html>"))
        self.pos_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">追踪人员位置</p></body></html>"))
        self.y_lable.setText(_translate("Dialog", "0.00"))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-style:italic;\">x:</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-style:italic;\">y:</span></p></body></html>"))
        self.x_pos.setText(_translate("Dialog", "0.00"))


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle('多人检测追踪系统')
        Dialog.resize(1147, 807)
        self.start_button = QtWidgets.QPushButton(Dialog)
        self.start_button.setGeometry(QtCore.QRect(50, 100, 281, 121))
        self.choose_id_button = QtWidgets.QPushButton(Dialog)
        self.choose_id_button.setGeometry(QtCore.QRect(360, 100, 150, 121))
        self.onoff_button = QtWidgets.QPushButton(Dialog)
        self.onoff_button.setGeometry(QtCore.QRect(540, 100, 170, 121))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet(
            "background-color: rgb(230, 230, 230);border-radius: 15px;border-style: outset;border-radius: 10px; border: 1px groove gray")
        self.start_button.setObjectName("start_button")
        self.choose_id_button.setFont(font)
        self.choose_id_button.setStyleSheet(
            "background-color: rgb(230, 230, 230);border-radius: 15px;border-style: outset;border-radius: 10px; border: 1px groove gray")
        self.choose_id_button.setObjectName("choose_id_button")
        self.onoff_button.setFont(font)
        self.onoff_button.setStyleSheet(
            "background-color: rgb(230, 230, 230);border-radius: 15px;border-style: outset;border-radius: 10px; border: 1px groove gray")
        self.onoff_button.setObjectName("onoff_button")
        self.info_label = QtWidgets.QLabel(Dialog)
        self.info_label.setGeometry(QtCore.QRect(0, 780, 150, 30))
        self.pic_label = QtWidgets.QLabel(Dialog)
        self.pic_label.setGeometry(QtCore.QRect(40, 250, 681, 481))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.pic_label.setFont(font)
        self.pic_label.setStyleSheet("border-color: rgb(130, 130, 130);\n"
                                     "background-color: rgb(230, 230, 230);")
        self.pic_label.setObjectName("pic_label")
        self.id_box = QtWidgets.QComboBox(Dialog)
        self.id_box.setGeometry(QtCore.QRect(740, 160, 361, 41))
        self.id_box.setObjectName("id_box")
        self.id_box.addItem('请先初始化！')
        self.id_label = QtWidgets.QLabel(Dialog)
        self.id_label.setGeometry(QtCore.QRect(810, 100, 211, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.pos_label = QtWidgets.QLabel(Dialog)
        self.pos_label.setGeometry(QtCore.QRect(820, 270, 211, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.pos_label.setFont(font)
        self.pos_label.setObjectName("pos_label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(740, 320, 381, 81))
        self.groupBox.setStyleSheet("border-color: rgb(175, 175, 175);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.y_lable = QtWidgets.QLabel(self.groupBox)
        self.y_lable.setGeometry(QtCore.QRect(260, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.y_lable.setFont(font)
        self.y_lable.setObjectName("y_lable")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(210, 10, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.x_pos = QtWidgets.QLabel(self.groupBox)
        self.x_pos.setGeometry(QtCore.QRect(80, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.x_pos.setFont(font)
        self.x_pos.setObjectName("x_pos")
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.id_box.setFont(font)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Change_ID(self):
        self.track_id = self.id_box.currentText()
        if self.track_id:
            print('track_id:', self.track_id)

    def set_ID_Box(self):
        self.id_box.clear()
        for i in range(len(self.current_id)):
            self.id_box.addItem(str(self.current_id[i][-1]))

    def connect_fun(self):
        self.start_button.clicked.connect(self.toggle_detection)
        self.id_box.currentIndexChanged.connect(self.Change_ID)
        self.choose_id_button.clicked.connect(self.init_id)
        self.onoff_button.clicked.connect(self.on_off_track)

    def toggle_detection(self):
        self.detecting = not self.detecting
        if self.detecting:
            self.start_button.setText('停止检测')
            self.start_button.setStyleSheet(
                "background-color: rgb(150, 150, 150);border-radius: 15px;border-style: outset;border-radius: 10px; border: 1px groove gray")
            self.start_detec_track()
        else:
            self.start_button.setText('开始检测')
            self.start_button.setStyleSheet(
                "background-color: rgb(230, 230, 230);border-radius: 15px;border-style: outset;border-radius: 10px; border: 1px groove gray")
            self.pic_label.setPixmap(QPixmap())
            self.pic_label.setText('<html><head/><body><p align="center">视频显示区域</p></body></html>')

    def on_off_track(self):
        self.tracking = not self.tracking
        if self.tracking:
            self.onoff_button.setText('停止追踪')
            self.onoff_button.setStyleSheet(
                "background-color: rgb(150, 150, 150);border-radius: 15px;border-style: outset;border-radius: 10px; border: 1px groove gray")
        else:
            self.onoff_button.setText('开始追踪')
            self.onoff_button.setStyleSheet(
                "background-color: rgb(230, 230, 230);border-radius: 15px;border-style: outset;border-radius: 10px; border: 1px groove gray")
            self.x_pos.setText('')
            self.y_lable.setText('')

    def initTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.set_xy_pos)

    def video_open(self):
        print('视频打开中')
        if not self.cap:
            self.cap = cv2.VideoCapture(self.cameras)
            print('camera width:', self.cap_width)
            print('camera height:', self.cap_height)
            print('cap_width:', self.cap.get(3))
            print('cap_height:', self.cap.get(4))
            print('视频打开成功')

    def init_id(self):
        self.x_pos.setText('')
        self.y_lable.setText('')
        print('初始化...')
        if self.current_id:
            self.set_ID_Box()
            print('已经设置idbox')

    def start_detec_track(self):
        print('开始检测...')
        self.video_open()
        self.fps = int(self.cap.get(5))
        print('fps:', self.fps)
        t = int(1000 / self.fps)
        videoWriter = None
        while self.detecting:

            # try:
            _, im = self.cap.read()
            print(im.shape)
            if im is None:
                print('none')
                break
            # 读取并处理
            result = self.det.feedCap(im)
            self.current_id = result['outputs']
            result = result['frame']
            result = imutils.resize(result, height=500)
            result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

            if videoWriter is None:
                fourcc = cv2.VideoWriter_fourcc(
                    'm', 'p', '4', 'v')  # opencv3.0
                videoWriter = cv2.VideoWriter(
                    'result.mp4', fourcc, self.fps, (result.shape[1], result.shape[0]))
            videoWriter.write(result)

            # 结果显示到pic_labe控件之中
            height, width, channel = result.shape
            bytes_per_line = 3 * width
            q_image = QPixmap.fromImage(QImage(result.data, width, height, bytes_per_line, QImage.Format_RGB888))
            self.pic_label.setPixmap(q_image)
            self.pic_label.setScaledContents(True)
            cv2.waitKey(t)

            # 输出坐标和速度,判断检测到人，并且设定了检测id，打开了追踪按钮才追踪
            if self.track_id and self.current_id and self.tracking:
                self.track_id_pos = self.find_id_xy()


    # 返回指定ID的[x,y]坐标
    def find_id_xy(self):
        for element in self.current_id:
            if element[-1] == int(self.track_id):
                x = self.cap_width/640 * ((element[0] + element[2]) / 2)
                x = round(x)
                y = self.cap_height/480 * ((element[1] + element[3]) / 2)
                y= round(y)
                return [x, y]
        return None

    # 设置x,y的值
    def set_xy_pos(self):
        if self.track_id_pos:
            self.x_pos.setText("{:.2f}".format(self.track_id_pos[0]))
            self.y_lable.setText("{:.2f}".format(self.track_id_pos[1]))

    def stop_detec_track(self):
        self.detecting = 0
        print('已停止检测')

    def closeEvent(self, event):  # 函数名固定不可变
        reply = QtWidgets.QMessageBox.question(self, u'警告', u'确认退出?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.detecting = 0
            event.accept()  # 关闭窗口
            QCoreApplication.instance().quit()
        else:
            event.ignore()  # 忽视点击X事件


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_Dialog()
    window.setWindowTitle('检测系统')
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap('icon.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    window.timer.start(100)
    window.setWindowIcon(icon)
    window.show()
    sys.exit(app.exec_())
