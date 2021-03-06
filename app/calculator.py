# Import necessary modules
import sys
from PySide.QtGui import *
from PySide.QtCore import *

import add_new_person
import get_person
import add_expense
import cal_sum

# Our main widget class
class MyWidget(QWidget):
    # Constructor function
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Bills Calculator")
        self.setFixedWidth(450)
        self.setMinimumSize(450, 525)
        self.setGeometry(100, 100, 300, 450)
    
        self.mainLayout = QVBoxLayout()
        self.infoLabel = QLabel("")

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

        self.totalButtonBox = QHBoxLayout()
        self.totalButtonBox.setAlignment(Qt.AlignCenter)

        #---------------------
        #Design Add Person box
        self.addPersonLabel = QLabel("Enter new person first name:")

        self.firtNameText = QLineEdit()
        self.firtNameText.setFixedWidth(250)
        self.addNameLayout.addWidget(self.firtNameText)

        self.addPersonButton = QPushButton("Add")
        self.addPersonButton.setFixedWidth(100)
        #Set button clicked function
        self.connect(self.addPersonButton, SIGNAL("clicked()"), self.person_button_click)
        self.addPersonButtonBox.addWidget(self.addPersonButton)

        self.addPersonLayout.addRow(self.addPersonLabel)
        self.addPersonLayout.addRow(self.addNameLayout)
        self.addPersonLayout.addRow(self.addPersonButtonBox)

        #---------------------
        #Design Add Expense box
        self.nameLabel = QLabel("First Name:")
        self.nameComboBox = QComboBox()
        self.nameComboBox.setFixedWidth(250)
        #Set button clicked function
        self.nameComboBox.addItems(get_person.get())

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
        self.connect(self.addExpenseButton, SIGNAL("clicked()"), self.expense_button_click)
        self.addExpenseButtonBox.addWidget(self.addExpenseButton)

        self.addExpenseLayout.addRow(self.nameLabel, self.nameComboBox)
        self.addExpenseLayout.addRow(self.dateLabel, self.dateText)
        self.addExpenseLayout.addRow(self.amountLabel, self.amountText)
        self.addExpenseLayout.addRow(self.addExpenseButtonBox)

        #---------------------
        #Design Total box
        self.showTotalButton = QPushButton("Show Expense")
        #Set button clicked function
        self.connect(self.showTotalButton, SIGNAL("clicked()"), self.total_button_click)

        self.totalButtonBox.addWidget(self.showTotalButton)
        self.totalLayout.addRow(self.totalButtonBox)

        #---------------------
        #Create all group boxes
        self.addPersonGroupBox = QGroupBox("Add Person")
        self.addExpenseGroupBox = QGroupBox("Add Expense")
        self.totalGroupBox = QGroupBox("Total")

        #---------------------
        #Add components to each group box
        self.addPersonGroupBox.setLayout(self.addPersonLayout)
        self.addExpenseGroupBox.setLayout(self.addExpenseLayout)
        self.totalGroupBox.setLayout(self.totalLayout)

        #---------------------
        #Add group boxes to mainLayout
        self.mainLayout.addWidget(self.addPersonGroupBox)
        self.mainLayout.addWidget(self.addExpenseGroupBox)
        self.mainLayout.addWidget(self.totalGroupBox)
        self.mainLayout.addWidget(self.infoLabel)

        self.setLayout(self.mainLayout)
        
    # Function reimplementing Key Press, Mouse Click and Resize Events
    def person_button_click(self):
        infoPersonText = add_new_person.add_person(self.firtNameText.text())
        if self.firtNameText.text() != "":
            self.nameComboBox.addItem(self.firtNameText.text())
        self.infoLabel.setText(infoPersonText)

    def expense_button_click(self):
        infoExpText = add_expense.add(self.dateText.text(), self.nameComboBox.currentText(), self.amountText.text())
        self.infoLabel.setText(infoExpText)

    def total_button_click(self):
        totalDict = cal_sum.calSum()

        while self.totalLayout.count() > 1:
            child = self.totalLayout.takeAt(1).widget()
            if child:
                child.deleteLater()

        self.totalLayout.update()

        for key, value in totalDict.iteritems():
            self.personMoneyLabel = QLabel(key + " spent " + value + " Euro")
            self.personMoneyLabelBox = QHBoxLayout()
            self.personMoneyLabelBox.setAlignment(Qt.AlignCenter)
            self.personMoneyLabelBox.addWidget(self.personMoneyLabel)
            self.totalLayout.setLayout(totalDict.keys().index(key)+1, QFormLayout.SpanningRole, self.personMoneyLabelBox)
   
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
