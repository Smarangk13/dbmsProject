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

    cellHeight = 40
    cellWidh = 105
    resultBoxX = leftAlign
    resultBoxY = resultLabelY + bufferY
    resultBoxWidth = 10 + cellWidh * 5
    resultBoxHeight = cellHeight * 5

    def __init__(self):
        super().__init__()
        self.interface = dbInterface.dbManager()
        self.selectedButton = QPushButton('Submit selected Query', self)
        self.resultBox = QTableWidget(self)
        self.resultText = QLabel(self)
        self.queryButton = QPushButton('Submit Custom Query', self)
        self.textboxIn = QPlainTextEdit(self)
        self.selectBox = QComboBox(self)
        self.selectText = QLabel(self)
        self.textLabel = QLabel(self)
        self.title = 'Car dealership'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Password text Line
        self.selectText.move(self.selectLabelX, self.selectLabelY)
        self.selectText.setText("Select Query")

        # Create textbox for Password
        self.selectBox.move(self.selectBoxX, self.selectBoxY)
        self.selectBox.resize(self.selectBoxWidth, self.selectBoxHeight)
        selectBoxOptions = ['Select Option',
                            'Which car model is the best seller ?',
                            'What is the name of the salesman with the best sales record?',
                            'What is Car X’s next service date ?',
                            'What are some cars available for under $?',
                            'Which vendor provided the most cars last year ?']
        self.selectBox.addItems(selectBoxOptions)

        self.selectedButton.move(self.submitSelectedButtonX, self.submitSelectedButtonY)
        self.selectedButton.resize(self.buttonWidth, self.submitSelectedButtonHeight)

        # Create Message text line
        self.textLabel.move(self.textLabelX, self.textLabelY)
        self.textLabel.setText("Custom Query")

        # Create textbox for message
        self.textboxIn.move(self.messageBoxX, self.messageBoxY)
        self.textboxIn.resize(self.messageBoxWidth,self.messageBoxHeight)

        # Create a button in the window
        self.queryButton.move(self.buttonX, self.buttonY)
        self.queryButton.resize(self.buttonWidth, self.buttonHeight)

        # connect button to function on_click
        self.selectedButton.clicked.connect(self.selectedQuery)
        self.queryButton.clicked.connect(self.customQuery)

        # Create result text Line
        self.resultText.move(self.resultLabelX, self.resultLabelY)
        self.resultText.setText("Result")

        # Create textbox for result
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
            res = self.interface.getTopSalesperson()
            # print(res)
            self.formatResults(res)

        elif query == 3:
            text = self.textboxIn.toPlainText()
            if text == "":
                res = self.interface.getAllSoldCars()
                self.formatResults(res)
                print(res)
                message = QMessageBox()
                message.setText("Enter Car vin into custom query box")
                message.showNormal()
                message.exec_()

            else:
                res = self.interface.getNextService(text)
                self.formatResults([res])

        elif query == 4:
            text = self.textboxIn.toPlainText()
            if text == "":
                message = QMessageBox()
                message.setText("Enter budget into custom query box")
                message.showNormal()
                message.exec_()
            else:
                res = self.interface.getVehiclesUnderLimit(text)
                self.formatResults(res)

        elif query == 5:
            res = self.interface.getTopVendor()
            self.formatResults([res])

    @pyqtSlot()
    def customQuery(self):
        textboxValue = self.textboxIn.toPlainText()
        result = self.interface.custom(textboxValue)
        self.formatResults(result)

    def formatResults(self, data):
        if data is None or data[0] is None or len(data) == 0:
            return
        if type(data) == tuple:
            data = [data]

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