#import VolumeHandControlModule as chv
from gui import HCapp_ui as HCapp

# class HCappFunc():
    # def __init__(self) -> None:
    #     self.ui = HCapp.Ui_MainWindow()
    #     pass

def VolumeHandControl(outputCam=True):
    #chv.VolumeHandControl.VoulumeControl(output=outputCam)
    pass


ui = HCapp.Ui_MainWindow()
def lineEdit():
    ui.lineEdit.setText("Hello cold world")


def main():
    # HCfunk=HCappFunc()
    VolumeHandControl()


if __name__ == "__main__":
    main()