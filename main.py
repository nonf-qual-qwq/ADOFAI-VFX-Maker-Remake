from PyQt6.QtWidgets import QApplication
import sys

import src.gui.GUI

if __name__ == '__main__':
    app = QApplication(sys.argv)

    src.gui.GUI.window = src.gui.GUI.MainWindow()
    src.gui.GUI.window.show()

    app.exec()

