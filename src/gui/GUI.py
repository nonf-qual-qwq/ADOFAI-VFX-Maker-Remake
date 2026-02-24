import os
import sys
import json
import src.lib.generate.main

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit, QMessageBox, QFileDialog
)

class MainWindow(QMainWindow):
    """ 主窗口 """

    def __init__(self):
        """基础设置"""
        super().__init__()

        self.json_file_path = None
        self.adofai_file_path = None

        self.setWindowTitle("ADOFAI VFX Maker")
        self.resize(1280, 720)
        self._setup_menu()
        self._setup_ui()

    def _setup_menu(self):
        """菜单设置"""
        menubar = self.menuBar()

        new_file_button = QAction("新建", self)
        open_file_button = QAction("打开JSON文件", self)
        save_file_button = QAction("保存", self)
        exit_button = QAction("退出", self)

        new_file_button.setShortcut(QKeySequence.StandardKey.New)
        open_file_button.setShortcut(QKeySequence.StandardKey.Open)
        save_file_button.setShortcut(QKeySequence.StandardKey.Save)

        new_file_button.triggered.connect(self.new_file)
        open_file_button.triggered.connect(self.open_file_json)
        save_file_button.triggered.connect(self.save_file)
        exit_button.triggered.connect(self.exit_button_clicked)

        file_menu = menubar.addMenu("&文件")
        file_menu.addAction(new_file_button)
        file_menu.addAction(open_file_button)
        file_menu.addAction(save_file_button)
        file_menu.addSeparator()
        file_menu.addAction(exit_button)

    def _setup_ui(self):
        """UI布局设置"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_v_layout = QVBoxLayout(central_widget)
        main_v_layout.setContentsMargins(10, 10, 10, 10)
        main_v_layout.setSpacing(12)

        h_layout1 = QHBoxLayout()
        self.json_label = QLabel("还未选.json文件", self)
        self.json_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.json_label.setMinimumWidth(150)

        btn1 = QPushButton("选择.json文件", self)
        btn1.clicked.connect(self.open_file_json)  # 移除冗余的wrapper

        self.generate_btn = QPushButton("生成", self)
        self.generate_btn.setMinimumWidth(80)
        self.generate_btn.clicked.connect(self.on_generate_clicked)

        h_layout1.addWidget(self.json_label)
        h_layout1.addWidget(btn1)
        h_layout1.addStretch()
        h_layout1.addWidget(self.generate_btn)

        h_layout2 = QHBoxLayout()
        self.adofai_label = QLabel("还未选.adofai文件", self)
        self.adofai_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.adofai_label.setMinimumWidth(150)

        btn2 = QPushButton("选择.adofai文件", self)
        btn2.clicked.connect(self.open_file_adofai)  # 移除冗余的wrapper

        h_layout2.addWidget(self.adofai_label)
        h_layout2.addWidget(btn2)
        h_layout2.addStretch()

        self.code_editor = QTextEdit(self)
        font = self.code_editor.font()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.code_editor.setFont(font)
        self.code_editor.setMinimumHeight(500)

        main_v_layout.addLayout(h_layout1)
        main_v_layout.addLayout(h_layout2)
        main_v_layout.addWidget(self.code_editor)

    def exit_button_clicked(self):
        self.close()

    def new_file(self):
        """新建文件"""
        if self.code_editor.toPlainText().strip():
            reply = QMessageBox.question(
                self, "提示", "当前有未保存的内容，是否先保存？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.save_file()

        self.code_editor.clear()
        self.json_file_path = None
        self.adofai_file_path = None
        self.json_label.setText("还未选.json文件")
        self.adofai_label.setText("还未选.adofai文件")
        self.setWindowTitle("ADOFAI VFX Maker - 未命名")

    def open_file_json(self):
        """打开json文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "打开JSON文件", "", "JSON文件 (*.json);;所有文件 (*.*)"
        )
        if not file_path:
            return

        if not file_path.endswith(".json"):
            QMessageBox.critical(self, "错误", "请选择.json格式的文件！")
            return

        try:
            with open(file_path, "r", encoding='utf-8-sig') as f:
                content = f.read()
                # 验证JSON格式是否合法
                json.loads(content)
                self.code_editor.setPlainText(content)

            self.json_file_path = file_path
            self.json_label.setText(os.path.basename(file_path))
            self.setWindowTitle(f"ADOFAI VFX Maker - {file_path}")
            QMessageBox.information(self, "成功", "JSON文件加载成功！")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "错误", "所选文件不是合法的JSON格式！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"读取文件失败：{str(e)}")

    def open_file_adofai(self):
        """加载ADOFAI文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "加载ADOFAI文件", "", "ADOFAI文件 (*.adofai);;所有文件 (*.*)"
        )
        if not file_path:
            return

        if not file_path.endswith(".adofai"):
            QMessageBox.critical(self, "错误", "请选择.adofai格式的文件！")
            return

        self.adofai_file_path = file_path
        self.adofai_label.setText(os.path.basename(file_path))
        # 更新窗口标题（保留JSON文件路径）
        if self.json_file_path:
            self.setWindowTitle(f"ADOFAI VFX Maker - {self.json_file_path}")
        QMessageBox.information(self, "成功", "ADOFAI文件加载成功！")

    def save_file(self):
        """保存JSON文件"""
        content = self.code_editor.toPlainText().strip()
        if not content:
            QMessageBox.warning(self, "警告", "文件内容为空，无需保存！")
            return

        # 验证保存内容是否为合法JSON
        try:
            json.loads(content)
        except json.JSONDecodeError:
            QMessageBox.critical(self, "错误", "内容不是合法的JSON格式，无法保存！")
            return

        if not self.json_file_path:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "保存JSON文件", "", "JSON文件 (*.json)"
            )
            if not file_path:
                return
            if not file_path.endswith(".json"):
                file_path += ".json"
            self.json_file_path = file_path

        try:
            with open(self.json_file_path, "w", encoding="utf-8-sig") as f:
                f.write(content)
            self.json_label.setText(os.path.basename(self.json_file_path))
            self.setWindowTitle(f"ADOFAI VFX Maker - {self.json_file_path}")
            QMessageBox.information(self, "成功", "文件保存成功！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存失败：{str(e)}")

    def on_generate_clicked(self):
        """生成按钮点击事件处理（核心逻辑）"""
        # 1. 检查必要文件是否选择
        if not self.json_file_path:
            QMessageBox.warning(self, "提示", "请先选择.json文件！")
            return
        if not self.adofai_file_path:
            QMessageBox.warning(self, "提示", "请先选择.adofai文件！")
            return

        # 2. 读取文件内容（使用with语句自动关闭文件）
        try:
            # 读取JSON文件内容
            with open(self.json_file_path, "r", encoding='utf-8-sig') as f_json:
                json_content = f_json.read()

            # 读取ADOfAI文件内容
            with open(self.adofai_file_path, "r", encoding='utf-8-sig') as f_adofai:
                adofai_content = f_adofai.read()

            # 3. 调用生成函数
            src.lib.generate.main.generate(json_content, adofai_content, self.adofai_file_path)
            QMessageBox.information(self, "成功", "成功生成到output.adofai！")


        except Exception as e:
            # 捕获所有异常并提示用户
            QMessageBox.critical(self, "生成失败", f"生成过程出错：\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()