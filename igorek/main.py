from PyQt5 import QtWidgets
import pymysql
from igor import *
conn = pymysql.connect(host="localhost", user="root", password="", database="igor")

def getdata():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM prod')
    res = cursor.fetchall()
    print(res)
    return res

class MainWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def init(self, parent=None):
        super(MainWin, self).init(parent)
        self.setupUi(self)
        resdata = getdata()
        height = 0
        tup = []
        for i in res_data:
            height += 50
            tup.append(i[1])
        textlb = ' \n'.join(tup)
        self.label_1.setText(textlb)
        self.label_1.setGeometry(10, 10, 500, height)

        for i in res_data:
            height += 25
            lb = QtWidgets.QLabel(self)
            lb.setGeometry(QtCore.QRect(20, height, 500, 21))
            lb.setObjectName(f"{i[0]}")
            lb.setText(f"{i[1]}")

if __name__ == "__main":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec_())