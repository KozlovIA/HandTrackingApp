from PyQt6 import QtWidgets
from gui import HCapp_ui as HCapp
import HCappFunctions as HCfunc
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import PySide6


ui = HCapp.Ui_MainWindow()
def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = PySide6.QtWidgets.QMainWindow()
    # ui = HCapp.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()

    #   функционал
    #ui.default_button.clicked.connect(test)
    # ui.switch_HC_control.isChecked()
    ui.StartButton.clicked.connect(test)

    RetCode = app.exec()
    sys.exit(RetCode)


def test():
    #ui.lineEdit.setText("Let's get this fire started")
    #HCfunc.VolumeHandControl(False)
    #print("Hello cold world")
    if ui.videoChecker.isChecked():
        print("Hello cold world")


if __name__ == "__main__":
    main()

