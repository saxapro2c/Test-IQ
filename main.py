import sys
import json
import im


from PyQt5 import QtWidgets
# from test3 import Ui_MainWindow
from test3 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QEvent


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.myclose = False
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        global CountPage
        global score
        CountPage = 0
        score = 0

        self.setFixedSize(800, 600)

        self.main_ui.pushButton_3.clicked.connect(self.Vihod)
        self.main_ui.pushButton_2.clicked.connect(self.Dalee)
        self.main_ui.pushButton_4.clicked.connect(self.Obratno)
        self.main_ui.pushButton.clicked.connect(self.NextPage2)
        self.main_ui.pushButton_5.clicked.connect(self.on_button_clicked)
        self.main_ui.pushButton_5.clicked.connect(self.NextPage)
        self.main_ui.pushButton_5.setEnabled(False)
        self.main_ui.pushButton_118.clicked.connect(self.Obratno)
        self.main_ui.pushButton_118.setEnabled(False)
        self.main_ui.pushButton_119.clicked.connect(self.Obratno)

        self.main_ui.lineEdit.textChanged.connect(self.checkLineEdit)
        self.main_ui.spinBox.valueChanged.connect(self.checkLineEdit)

        #Вопрос 1
        self.main_ui.pushButton_8.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_7.clicked.connect(self.NextPage)
        self.main_ui.pushButton_9.clicked.connect(self.NextPage)
        self.main_ui.pushButton_6.clicked.connect(self.NextPage)

        # Вопрос 2
        self.main_ui.pushButton_10.clicked.connect(self.NextPage)
        self.main_ui.pushButton_11.clicked.connect(self.NextPage)
        self.main_ui.pushButton_12.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_13.clicked.connect(self.NextPage)

        # Вопрос 3
        self.main_ui.pushButton_14.clicked.connect(self.NextPage)
        self.main_ui.pushButton_15.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_16.clicked.connect(self.NextPage)
        self.main_ui.pushButton_17.clicked.connect(self.NextPage)
        self.main_ui.pushButton_18.clicked.connect(self.NextPage)

        # Вопрос 4
        self.main_ui.pushButton_19.clicked.connect(self.NextPage)
        self.main_ui.pushButton_20.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_21.clicked.connect(self.NextPage)
        self.main_ui.pushButton_22.clicked.connect(self.NextPage)

        # Вопрос 5
        self.main_ui.pushButton_23.clicked.connect(self.NextPage)
        self.main_ui.pushButton_24.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_25.clicked.connect(self.NextPage)
        self.main_ui.pushButton_26.clicked.connect(self.NextPage)

        # вопрос 6
        self.main_ui.pushButton_28.clicked.connect(self.NextPage)
        self.main_ui.pushButton_29.clicked.connect(self.NextPage)
        self.main_ui.pushButton_30.clicked.connect(self.TrueScore)

        # вопрос 7
        self.main_ui.pushButton_31.clicked.connect(self.NextPage)
        self.main_ui.pushButton_32.clicked.connect(self.NextPage)
        self.main_ui.pushButton_33.clicked.connect(self.TrueScore)

        # вопрос 8
        self.main_ui.pushButton_34.clicked.connect(self.NextPage)
        self.main_ui.pushButton_35.clicked.connect(self.NextPage)
        self.main_ui.pushButton_36.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_37.clicked.connect(self.NextPage)

        # вопрос 9
        self.main_ui.pushButton_38.clicked.connect(self.NextPage)
        self.main_ui.pushButton_39.clicked.connect(self.NextPage)
        self.main_ui.pushButton_40.clicked.connect(self.NextPage)
        self.main_ui.pushButton_41.clicked.connect(self.NextPage)
        self.main_ui.pushButton_42.clicked.connect(self.TrueScore)

        # вопрос 10
        self.main_ui.pushButton_43.clicked.connect(self.NextPage)
        self.main_ui.pushButton_44.clicked.connect(self.NextPage)
        self.main_ui.pushButton_45.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_46.clicked.connect(self.NextPage)

        # вопрос 11
        self.main_ui.pushButton_47.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_48.clicked.connect(self.NextPage)
        self.main_ui.pushButton_49.clicked.connect(self.NextPage)
        self.main_ui.pushButton_50.clicked.connect(self.NextPage)


        # вопрос 12
        self.main_ui.pushButton_51.clicked.connect(self.NextPage)
        self.main_ui.pushButton_52.clicked.connect(self.NextPage)
        self.main_ui.pushButton_53.clicked.connect(self.NextPage)
        self.main_ui.pushButton_54.clicked.connect(self.TrueScore)

        # вопрос 13
        self.main_ui.pushButton_55.clicked.connect(self.NextPage)
        self.main_ui.pushButton_56.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_57.clicked.connect(self.NextPage)
        self.main_ui.pushButton_58.clicked.connect(self.NextPage)
        self.main_ui.pushButton_59.clicked.connect(self.NextPage)
        self.main_ui.pushButton_60.clicked.connect(self.NextPage)

        # вопрос 14
        self.main_ui.pushButton_61.clicked.connect(self.NextPage)
        self.main_ui.pushButton_62.clicked.connect(self.NextPage)
        self.main_ui.pushButton_63.clicked.connect(self.NextPage)
        self.main_ui.pushButton_64.clicked.connect(self.TrueScore)

        # вопрос 15
        self.main_ui.pushButton_65.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_66.clicked.connect(self.NextPage)
        self.main_ui.pushButton_67.clicked.connect(self.NextPage)
        self.main_ui.pushButton_68.clicked.connect(self.NextPage)

        # вопрос 16
        self.main_ui.pushButton_69.clicked.connect(self.NextPage)
        self.main_ui.pushButton_70.clicked.connect(self.NextPage)
        self.main_ui.pushButton_71.clicked.connect(self.NextPage)
        self.main_ui.pushButton_72.clicked.connect(self.NextPage)
        self.main_ui.pushButton_73.clicked.connect(self.TrueScore)

        # вопрос 17
        self.main_ui.pushButton_74.clicked.connect(self.NextPage)
        self.main_ui.pushButton_75.clicked.connect(self.NextPage)
        self.main_ui.pushButton_76.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_77.clicked.connect(self.NextPage)

        # вопрос 18
        self.main_ui.pushButton_78.clicked.connect(self.NextPage)
        self.main_ui.pushButton_79.clicked.connect(self.NextPage)
        self.main_ui.pushButton_80.clicked.connect(self.TrueScore)

        # вопрос 19
        self.main_ui.pushButton_81.clicked.connect(self.NextPage)
        self.main_ui.pushButton_82.clicked.connect(self.NextPage)
        self.main_ui.pushButton_83.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_84.clicked.connect(self.NextPage)

        # вопрос 20
        self.main_ui.pushButton_85.clicked.connect(self.NextPage)
        self.main_ui.pushButton_86.clicked.connect(self.NextPage)
        self.main_ui.pushButton_87.clicked.connect(self.NextPage)
        self.main_ui.pushButton_88.clicked.connect(self.NextPage)
        self.main_ui.pushButton_89.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_90.clicked.connect(self.NextPage)
        self.main_ui.pushButton_91.clicked.connect(self.NextPage)

        # вопрос 21
        self.main_ui.pushButton_92.clicked.connect(self.NextPage)
        self.main_ui.pushButton_93.clicked.connect(self.NextPage)
        self.main_ui.pushButton_94.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_95.clicked.connect(self.NextPage)

        # вопрос 22
        self.main_ui.pushButton_96.clicked.connect(self.NextPage)
        self.main_ui.pushButton_97.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_98.clicked.connect(self.NextPage)
        self.main_ui.pushButton_99.clicked.connect(self.NextPage)

        # вопрос 23
        self.main_ui.pushButton_100.clicked.connect(self.NextPage)
        self.main_ui.pushButton_101.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_102.clicked.connect(self.NextPage)
        self.main_ui.pushButton_103.clicked.connect(self.NextPage)

        # вопрос 24
        self.main_ui.pushButton_104.clicked.connect(self.NextPage)
        self.main_ui.pushButton_105.clicked.connect(self.TrueScore)
        self.main_ui.pushButton_106.clicked.connect(self.NextPage)
        self.main_ui.pushButton_107.clicked.connect(self.NextPage)

        # вопрос 25
        self.main_ui.pushButton_108.clicked.connect(self.NextPage)
        self.main_ui.pushButton_109.clicked.connect(self.NextPage)
        self.main_ui.pushButton_110.clicked.connect(self.NextPage)
        self.main_ui.pushButton_111.clicked.connect(self.TrueScore)

        # вопрос 26
        self.main_ui.pushButton_112.clicked.connect(self.NextPage)
        self.main_ui.pushButton_113.clicked.connect(self.NextPage)
        self.main_ui.pushButton_114.clicked.connect(self.TrueScore)


        self.main_ui.pushButton_27.clicked.connect(self.result)
        app.aboutToQuit.connect(self.closeEvent)



    def BackPage(self):
        global CountPage
        CountPage -= 1
        self.main_ui.stackedWidget.setCurrentIndex(CountPage)

    def NextPage(self):
        global CountPage
        CountPage += 1
        self.main_ui.stackedWidget.setCurrentIndex(CountPage)
        self.Spisok()

    def NextPage2(self):
        global CountPage
        CountPage = 2
        self.main_ui.stackedWidget.setCurrentIndex(CountPage)

    def TrueScore(self):
        global CountPage
        global score
        CountPage += 1
        score += 3
        self.main_ui.stackedWidget.setCurrentIndex(CountPage)

    def Obratno(self):
        CountPage = 0
        new_value = 1
        self.main_ui.stackedWidget.setCurrentIndex(CountPage)
        self.main_ui.lineEdit.setText(f"")
        self.main_ui.label_56.setText(f"")
        self.main_ui.spinBox.setValue(new_value)
        self.Spisok()

    def checkLineEdit(self):
        if self.main_ui.lineEdit.text() and self.main_ui.spinBox.value() >= 1:
            self.main_ui.pushButton_5.setEnabled(True)
        else:
            self.main_ui.pushButton_5.setEnabled(False)


    # def closeEvent(self,event):
    #     if self.myclose:
    #         print(self.myclose)
    #     else:
    #         event.ignore()
    #         print(self.myclose, "ignore")

    def Dalee(self):
        CountPage = 1
        self.main_ui.stackedWidget.setCurrentIndex(CountPage)

    def Spisok(self):
        with open("Пользователь.json", encoding="utf8") as file:
            Data = json.load(file)
            index = 1
            self.main_ui.listWidget.clear()
            for value in Data.values():
                self.main_ui.listWidget.addItem(f" №{index}  Имя: {value.get('Name')}  Возраст: {value.get('Age')}  IQ: {value.get('IQ')}")
                index += 1

    def on_button_clicked(self):
        global Age
        with open("Пользователь.json", encoding="utf8") as file:

            data = json.load(file)
            User_Name = self.main_ui.lineEdit.text()
            Age = self.main_ui.spinBox.text()
            chet = len(data) +1



            #Имя и возраст
            new_data = {
                'Name': User_Name,
                'Age': Age,
                'IQ': ""
            }
            data [chet ] = new_data

            # Запись инфы о пользователе в файл
            with open("Пользователь.json", "w", encoding="utf8") as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=3)
                outfile.close()
            file.close()



    def result(self):
        with open('Пользователь.json', encoding="utf8") as f:
            Data = json.load(f)
            index = Data[f"{len(Data)}"]
            age = int(index.get("Age"))
            iq = round(score / age * 100)
            index["IQ"] = iq
            Data[f"{len(Data)}"] = index
            self.main_ui.pushButton_118.setEnabled(True)

            with open("Пользователь.json", "w", encoding="utf8") as outfile:
                json.dump(Data, outfile, ensure_ascii=False, indent=3)
                print(score)
        self.main_ui.label_56.setText(f"ваш iq равен {iq}")





    def Vihod(self):
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MyMainWindow()
    Window.show()
    Window.Spisok()
    sys.exit(app.exec())




