import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog, QMessageBox


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):

        self.add_formula.clicked.connect(self.add_f)
        self.delete_formula.clicked.connect(self.delete_f)
        self.save_button.clicked.connect(self.save_to_file)
        self.result.clicked.connect(self.result_sum)
        self.type_main1.clicked.connect(self.change_main1)
        self.type_main2.clicked.connect(self.change_main2)

    def change_main1(self):
        self.type_doc2_1.enable = False
        self.type_doc2_2.enable = False
        self.result_text.setText("1")

    def change_main2(self):
        self.type_doc2_1.enabled = True
        self.type_doc2_2.enabled = True
        self.result_text.setText("2")

    def add_f(self):
        self.formuls.addItem(self.new_formula.text())
        self.new_formula.setText("")

    def delete_f(self):
        item = self.formuls.takeItem(self.formuls.currentRow())
        item = None

    def save_to_file(self):
        pass

    def result_sum(self):
        summa = 0
        if self.type_main1.isChecked():
            if self.type_doc1.isChecked():
                if self.type_user1.isChecked():
                    summa = 1400
                    if self.formuls.count() > 10:
                        summa += 700 * (self.formuls.count() - 10)
                if self.type_user2.isChecked():
                    summa = 140
                    if self.formuls.count() > 10:
                        summa += 70 * (self.formuls.count() - 10)
                if self.type_user3.isChecked():
                    summa = 350
                    if self.formuls.count() > 10:
                        summa += 175 * (self.formuls.count() - 10)
                if self.type_user4.isChecked():
                    summa = 490
                    if self.formuls.count() > 10:
                        summa += 245 * (self.formuls.count() - 10)
            if self.type_doc2.isChecked():
                if self.type_user1.isChecked():
                    summa = 2500
                if self.type_user2.isChecked():
                    summa = 250
                if self.type_user3.isChecked():
                    summa = 625
                if self.type_user4.isChecked():
                    summa = 875
            if self.type_doc3.isChecked():
                if self.type_user1.isChecked():
                    summa = 3000
                if self.type_user2.isChecked():
                    summa = 300
                if self.type_user3.isChecked():
                    summa = 750
                if self.type_user4.isChecked():
                    summa = 1050
            if self.type_doc4.isChecked():
                if self.type_user1.isChecked():
                    summa = 1500
                if self.type_user2.isChecked():
                    summa = 1500
                if self.type_user3.isChecked():
                    summa = 1500
                if self.type_user4.isChecked():
                    summa = 1500
        if self.type_main2.isChecked():
            if self.type_doc1.isChecked():
                if self.type_user1.isChecked():
                    summa = 3300
                    if self.formuls.count() > 10:
                        summa += 700 * (self.formuls.count() - 10)
                if self.type_user2.isChecked():
                    summa = 330
                    if self.formuls.count() > 10:
                        summa += 70 * (self.formuls.count() - 10)
                if self.type_user3.isChecked():
                    summa = 825
                    if self.formuls.count() > 10:
                        summa += 175 * (self.formuls.count() - 10)
                if self.type_user4.isChecked():
                    summa = 1155
                    if self.formuls.count() > 10:
                        summa += 245 * (self.formuls.count() - 10)
            if self.type_doc2.isChecked():
                if self.type_user1.isChecked():
                    summa = 2500
                if self.type_user2.isChecked():
                    summa = 250
                if self.type_user3.isChecked():
                    summa = 625
                if self.type_user4.isChecked():
                    summa = 875
            if self.type_doc3.isChecked():
                if self.type_user1.isChecked():
                    summa = 3000
                if self.type_user2.isChecked():
                    summa = 300
                if self.type_user3.isChecked():
                    summa = 750
                if self.type_user4.isChecked():
                    summa = 1050
            if self.type_doc4.isChecked():
                if self.type_user1.isChecked():
                    summa = 1500
                if self.type_user2.isChecked():
                    summa = 1500
                if self.type_user3.isChecked():
                    summa = 1500
                if self.type_user4.isChecked():
                    summa = 1500
        self.result_text.setText(str(summa))
      

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
