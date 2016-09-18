# Import required modules
import sys, time
from PySide.QtGui import QApplication, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    """ Our Main Window Class
    """

    def __init__(self):
        """ Constructor Fucntion
        """
        QMainWindow.__init__(self)
        self.setWindowTitle("Main Window")
        self.setGeometry(300, 250, 400, 300)

    def SetupComponents(self):
        """ Setting the central widget
        """
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        mainWindow.SetupComponents()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
