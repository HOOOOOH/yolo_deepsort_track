# 导入所需的库
import sys
import openai
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit

# 设置API密钥
openai.api_key = "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"

# 创建一个窗口类
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle("ChatGPT")
        self.resize(600, 400)

        # 创建一个文本编辑框，用于输入和显示对话内容
        self.textEdit = QTextEdit(self)
        #self.textEdit.setReadOnly(True)
        self.textEdit.append("这是Bing。我可以帮你回答任何问题。")

        # 创建一个按钮，用于发送消息给机器人
        self.button = QPushButton("发送", self)
        self.button.clicked.connect(self.send_message)

        # 调整控件的位置和大小
        self.textEdit.setGeometry(10, 10, 580, 350)
        self.button.setGeometry(500, 370, 80, 20)

    def send_message(self):
        # 获取用户输入的消息，并清空输入框
        user_message = self.textEdit.toPlainText().split("\n")[-1]
        self.textEdit.clear()

        # 调用OpenAI API，使用chatgpt模型生成机器人回答
        response = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            prompt=self.textEdit.toPlainText() + "\n" + user_message + "\n",
            temperature=0.7,
            max_tokens=1500,
            n=1
            )

        # 将用户消息和机器人回答添加到文本编辑框，并以markdown格式显示
        self.textEdit.append(f"**User:** {user_message}\n")
        self.textEdit.append(f"**Bing:** {response['choices'][0]['message']['content']}\n")

# 创建应用程序对象和窗口对象，并显示窗口
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())