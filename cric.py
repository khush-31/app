from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        import requests
        from bs4 import BeautifulSoup
        URL = "https://www.cricbuzz.com"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content,features='lxml')
        table = soup.find_all('li', {
            'class': 'cb-col cb-col-25 cb-mtch-blk cb-vid-sml-card-api videos-carousal-item cb-carousal-item-large cb-view-all-ga'})
        # print(table)

        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(598, 600)
        self.hbox = QtWidgets.QGridLayout()
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(0, 0, 120, 33)
        self.pushButton.setMaximumSize(120,33)
        self.hbox.addWidget(self.pushButton,0,0)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        c = []

        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        for li in table:
            match = li.text.strip()
            b3 = QtWidgets.QPushButton(self.centralwidget)
            b3.setText(match)
            self.hbox.addWidget(b3)
            b3.setStyleSheet('QPushButton {background-color: red; color: white; border:1px solid black}')
            b3.setFont(font)
            b3.setMinimumHeight(50)
        mainwindow.setLayout(self.hbox)

        self.pushButton.setStyleSheet("QPushButton {background-color: white;border:1.5px solid black}")
        mainwindow.setStyleSheet("background-color:#98DBC6")
        self.pushButton.clicked.connect(mainwindow.close)
        self.pushButton.clicked.connect(lab)
        self.retranslateUi(mainwindow)
        self.pushButton.setFont(font)
        self.pushButton.setMinimumSize(150,40)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Cricket Score"))
        self.pushButton.setText(_translate("mainwindow", "🔄 REFRESH"))
        # self.pushButton_2.setText(_translate("mainwindow", "CRICKET SCHEDULE"))


def lab():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        mainwindow = QtWidgets.QDialog()
        ui = Ui_mainwindow()
        ui.setupUi(mainwindow)
        mainwindow.show()
        sys.exit(mainwindow.exec_())
        # app.exec_()


lab()