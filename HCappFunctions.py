import HandTrackingModule as HTM
from gui import HCapp_ui as HCapp

# class HCappFunc():
    # def __init__(self) -> None:
    #     self.ui = HCapp.Ui_MainWindow()
    #     pass

HDet = HTM.handDetector()

def HandControlStart(CameraNumber = 0, outputCam=True):
    HDet.finishWhile = False
    HDet.main(CameraNumber = CameraNumber, outputCam=outputCam)
    
def HandControlFinish():
    HDet.finishWhile = True
    HDet.close_window()


#ui = HCapp.Ui_MainWindow()
def main():
    # HCfunk=HCappFunc()
    HandControlStart()


if __name__ == "__main__":
    main()