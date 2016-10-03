# Import necessary modules
import sys
from PySide.QtGui import *
from PySide.QtCore import *

import add_new_person
import get_person
import add_expense

# Our main widget class
class MyWidget(QWidget):
    # Constructor function
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Bills Calculator")
        self.setFixedWidth(450)
        self.setMinimumSize(450, 500)
        self.setGeometry(100, 100, 270, 450)
    
        self.mainLayout = QVBoxLayout()

        #Create layout for Add Person GroupBox
        self.addPersonLayout = QFormLayout()
        self.addPersonLayout.setHorizontalSpacing(30)
        self.addNameLayout = QHBoxLayout()
        self.addNameLayout.setAlignment(Qt.AlignCenter)
        self.addPersonButtonBox = QHBoxLayout()
        self.addPersonButtonBox.setAlignment(Qt.AlignCenter)
        
        #Create layout for Add Expense GroupBox
        self.addExpenseLayout = QFormLayout()
        self.addExpenseLayout.setHorizontalSpacing(30)
        self.addExpenseButtonBox = QHBoxLayout()
        self.addExpenseButtonBox.setAlignment(Qt.AlignCenter)

        #Create layout for Total GroupBox
        self.totalLayout = QFormLayout()
        self.totalLayout.setHorizontalSpacing(30)

        self.showTotalButtonBox = QHBoxLayout()
        self.showTotalButtonBox.setAlignment(Qt.AlignCenter)
        self.fangLabelBox = QHBoxLayout()
        self.fangLabelBox.setAlignment(Qt.AlignCenter)
        self.modanLabelBox = QHBoxLayout()
        self.modanLabelBox.setAlignment(Qt.AlignCenter)
        self.changLabelBox = QHBoxLayout()
        self.changLabelBox.setAlignment(Qt.AlignCenter)


        #Design Add Person box
        self.addPersonLabel = QLabel("Enter new person first name:")

        self.firtNameText = QLineEdit()
        self.firtNameText.setFixedWidth(250)
        self.addNameLayout.addWidget(self.firtNameText)

        self.addPersonButton = QPushButton("Add")
        self.addPersonButton.setFixedWidth(100)
        #Set button clicked function
        self.connect(self.addPersonButton, SIGNAL("clicked()"),self.person_button_click)
        self.addPersonButtonBox.addWidget(self.addPersonButton)

        self.addPersonLayout.addRow(self.addPersonLabel)
        self.addPersonLayout.addRow(self.addNameLayout)
        self.addPersonLayout.addRow(self.addPersonButtonBox)

        
        #Design Add Expense box
        self.nameLabel = QLabel("First Name:")
        self.nameComboBox = QComboBox()
        self.nameComboBox.setFixedWidth(250)
        #Set button clicked function
        #self.nameComboBox.activated.connect(self.combobox_add_item)
        self.nameComboBox.addItems(get_person.get())
        #self.nameComboBox.addItem("Fang")
        #self.nameComboBox.addItem("Modan")
        #self.nameComboBox.addItem("Chang")

        self.dateLabel = QLabel("Date:")
        self.dateText = QLineEdit()
        self.dateText.setFixedWidth(250)
        self.dateText.setPlaceholderText("dd/mm/yyyy")

        self.amountLabel = QLabel("Amount(EUR):")
        self.amountText = QLineEdit()
        self.amountText.setFixedWidth(250)
        self.amountText.setPlaceholderText("0.00")

        self.addExpenseButton = QPushButton("Add")
        self.addExpenseButton.setFixedWidth(100)
        #Set button clicked function
        self.connect(self.addExpenseButton, SIGNAL("clicked()"),self.expense_button_click)
        self.addExpenseButtonBox.addWidget(self.addExpenseButton)

        self.addExpenseLayout.addRow(self.nameLabel, self.nameComboBox)
        self.addExpenseLayout.addRow(self.dateLabel, self.dateText)
        self.addExpenseLayout.addRow(self.amountLabel, self.amountText)
        self.addExpenseLayout.addRow(self.addExpenseButtonBox)

        #Design Total box
        self.showTotalButton = QPushButton("Show Expense")

        self.fangLabel = QLabel("Fang spent")
        self.fangAmountLabel = QLabel("4.00 Euro")
        self.modanLabel = QLabel("Modan spent")
        self.modanAmountLabel = QLabel("5.00 Euro")
        self.changLabel = QLabel("Chang spent")
        self.changAmountLabel = QLabel("4.87 Euro")

        self.showTotalButtonBox.addWidget(self.showTotalButton)
        self.fangLabelBox.addWidget(self.fangLabel)
        self.fangLabelBox.addWidget(self.fangAmountLabel)
        self.modanLabelBox.addWidget(self.modanLabel)
        self.modanLabelBox.addWidget(self.modanAmountLabel)
        self.changLabelBox.addWidget(self.changLabel)
        self.changLabelBox.addWidget(self.changAmountLabel)

        self.totalLayout.addRow(self.showTotalButtonBox)
        self.totalLayout.addRow(self.fangLabelBox)
        self.totalLayout.addRow(self.modanLabelBox)
        self.totalLayout.addRow(self.changLabelBox)

        #Create all group boxes
        self.addPersonGroupBox = QGroupBox("Add Person")
        self.addExpenseGroupBox = QGroupBox("Add Expense")
        self.totalGroupBox = QGroupBox("Total")

        #Add components to each group box
        self.addPersonGroupBox.setLayout(self.addPersonLayout)
        self.addExpenseGroupBox.setLayout(self.addExpenseLayout)
        self.totalGroupBox.setLayout(self.totalLayout)

        #Add group boxes to mainLayout
        self.mainLayout.addWidget(self.addPersonGroupBox)
        self.mainLayout.addWidget(self.addExpenseGroupBox)
        self.mainLayout.addWidget(self.totalGroupBox)

        self.setLayout(self.mainLayout)
        
    # Function reimplementing Key Press, Mouse Click and Resize Events
    def person_button_click(self):
        add_new_person.add_person(self.firtNameText.text())

    def expense_button_click(self):
        add_expense.add(self.dateText.text(), self.nameComboBox.currentText(), self.amountText.text())

    #def combobox_add_item(self):
    #    self.nameComboBox.addItems(get_person.get())

    #def keyPressEvent(self, event):
        #if event.key() == Qt.Key_Escape:
            #self.close()
                    
    #def mouseDoubleClickEvent(self, event):
        #self.close()
                            
    #def resizeEvent(self, event):
        #self.infoLabel.setText("Window Resized to QSize(%d, %d)" % (event.size().width(), event.size().height()))

if __name__ =='__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWidget = MyWidget()
        myWidget.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
