import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DBMSProject.dbmsProject import dbInterface


class App(QMainWindow):
    left = 400
    top = 100
    width = 900
    height = 740

    leftAlign = 20
    topAlign = 20
    bufferX = 20
    bufferY = 30
    labelHeight = 30
    buttonHeight = 40

    selectLabelX = leftAlign
    selectLabelY = topAlign

    selectBoxX = leftAlign
    selectBoxY = selectLabelY + labelHeight
    selectBoxWidth = width - leftAlign * 2
    selectBoxHeight = labelHeight

    submitSelectedButtonX = leftAlign
    submitSelectedButtonY = selectBoxY + selectBoxHeight + bufferY
    submitSelectedButtonHeight = buttonHeight

    textLabelX = leftAlign
    textLabelY = submitSelectedButtonY + submitSelectedButtonHeight + bufferY

    messageBoxX = leftAlign
    messageBoxY = textLabelY + bufferY
    messageBoxWidth = width - leftAlign *2
    messageBoxHeight = selectBoxHeight * 3

    buttonX = leftAlign
    buttonY = messageBoxY + messageBoxHeight + bufferY
    buttonWidth = width - bufferX *2

    resultLabelX = leftAlign
    resultLabelY = buttonY + buttonHeight + bufferY

    resultBoxX = leftAlign
    resultBoxY = resultLabelY + bufferY
    resultBoxWidth = width - leftAlign * 2
    resultBoxHeight = selectBoxHeight * 5

    def __init__(self):
        super().__init__()
        self.title = 'Car dealership'
        self.initUI()
        self.interface = dbInterface.dbManager()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Password text Line
        self.selectText = QLabel(self)
        self.selectText.move(self.selectLabelX, self.selectLabelY)
        self.selectText.setText("Select Query")

        # Create textbox for Password
        self.selectBox = QComboBox(self)
        self.selectBox.move(self.selectBoxX, self.selectBoxY)
        self.selectBox.resize(self.selectBoxWidth, self.selectBoxHeight)
        selectBoxOptions = ['Select Option',
                            'Which car model is the best seller ?',
                            'What is the name of the staff with the most selling record by month ?',
                            'What is Car X’s next service date ?',
                            'What are some cars available for under $?',
                            'Which vendor provided the most cars last year ?']
        self.selectBox.addItems(selectBoxOptions)

        self.submitselectedButtton = QPushButton('Submit selectected Query', self)
        self.submitselectedButtton.move(self.submitSelectedButtonX, self.submitSelectedButtonY)
        self.submitselectedButtton.resize(self.buttonWidth, self.submitSelectedButtonHeight)

        # Create Message text line
        self.textLabel = QLabel(self)
        self.textLabel.move(self.textLabelX, self.textLabelY)
        self.textLabel.setText("Custom Query")

        # Create textbox for message
        self.textboxIn = QPlainTextEdit(self)
        self.textboxIn.move(self.messageBoxX, self.messageBoxY)
        self.textboxIn.resize(self.messageBoxWidth,self.messageBoxHeight)

        # Create a button in the window
        self.button1 = QPushButton('Submit Custom Query', self)
        self.button1.move(self.buttonX, self.buttonY)
        self.button1.resize(self.buttonWidth,self.buttonHeight)

        # connect button to function on_click
        # self.submitselectedButtton.connect(self.selectedQuery)
        self.submitselectedButtton.clicked.connect(self.selectedQuery)
        self.button1.clicked.connect(self.selectedQuery)
        # self.button1.connect(self.customQuery)

        # Create result text Line
        self.resultText = QLabel(self)
        self.resultText.move(self.resultLabelX, self.resultLabelY)
        self.resultText.setText("Result")

        # Create textbox for result
        self.resultBox = QTableWidget(self)
        self.resultBox.setRowCount(5)
        self.resultBox.setColumnCount(5)
        self.resultBox.move(self.resultBoxX, self.resultBoxY)
        self.resultBox.resize(self.resultBoxWidth, self.resultBoxHeight)

        self.show()

    @pyqtSlot()
    def selectedQuery(self):
        query = self.selectBox.currentIndex()
        if query == 1:
            res = self.interface.getTopSellingCar()
            self.formatResults([res])

        elif query == 2:
            pass

        elif query == 3:
            res = self.interface.getNextService(2)
            self.formatResults([res])

        elif query == 4:
            res = self.interface.getVehiclesUnderLimit(20000)
            self.formatResults([res])

        elif query == 5:
            res = self.interface.getTopVendor()
            print(res)

    def customQuery(self):
        textboxValue = self.textboxIn.toPlainText()
        result = self.interface.customQueries(textboxValue)

    def formatResults(self, data):
        self.resultBox.setRowCount(len(data))
        self.resultBox.setColumnCount(len(data[0]))
        for i in range(len(data)):
            for j in range(len(data[i])):
                entry = QTableWidgetItem(str(data[i][j]))
                self.resultBox.setItem(i, j, entry)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())