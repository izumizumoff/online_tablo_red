import sys
import json
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QFile)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 1000)
        Form.setMinimumSize(QSize(700, 500))
        Form.setMaximumSize(QSize(720, 1000))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(700, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(350, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.LEFT_TITLE = QLineEdit(Form)
        self.LEFT_TITLE.setObjectName(u"LEFT_TITLE")
        self.LEFT_TITLE.setMaximumSize(QSize(350, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.LEFT_TITLE.setFont(font2)

        self.verticalLayout_6.addWidget(self.LEFT_TITLE)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(350, 30))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.RIGHT_TITLE = QLineEdit(Form)
        self.RIGHT_TITLE.setObjectName(u"RIGHT_TITLE")
        self.RIGHT_TITLE.setMaximumSize(QSize(350, 30))
        self.RIGHT_TITLE.setFont(font2)

        self.verticalLayout_5.addWidget(self.RIGHT_TITLE)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(700, 30))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(350, 30))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setItalic(True)
        self.label_7.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_7)

        self.MAIN_FONT = QSpinBox(Form)
        self.MAIN_FONT.setObjectName(u"MAIN_FONT")
        self.MAIN_FONT.setMaximumSize(QSize(350, 30))
        self.MAIN_FONT.setFont(font2)
        self.MAIN_FONT.setMinimum(3)
        self.MAIN_FONT.setMaximum(36)
        self.MAIN_FONT.setValue(14)

        self.verticalLayout_7.addWidget(self.MAIN_FONT)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(350, 30))
        self.label_8.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_8)

        self.REGULAR_FONT = QSpinBox(Form)
        self.REGULAR_FONT.setObjectName(u"REGULAR_FONT")
        self.REGULAR_FONT.setMaximumSize(QSize(350, 30))
        self.REGULAR_FONT.setFont(font2)
        self.REGULAR_FONT.setMinimum(3)
        self.REGULAR_FONT.setMaximum(36)
        self.REGULAR_FONT.setValue(12)

        self.verticalLayout_7.addWidget(self.REGULAR_FONT)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(350, 30))
        self.label_9.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_9)

        self.BIG_FONT = QSpinBox(Form)
        self.BIG_FONT.setObjectName(u"BIG_FONT")
        self.BIG_FONT.setMaximumSize(QSize(350, 30))
        self.BIG_FONT.setFont(font2)
        self.BIG_FONT.setMinimum(3)
        self.BIG_FONT.setMaximum(36)
        self.BIG_FONT.setValue(20)

        self.verticalLayout_7.addWidget(self.BIG_FONT)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(350, 30))
        self.label_10.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_10)

        self.SMALL_FONT = QSpinBox(Form)
        self.SMALL_FONT.setObjectName(u"SMALL_FONT")
        self.SMALL_FONT.setMaximumSize(QSize(350, 30))
        self.SMALL_FONT.setFont(font2)
        self.SMALL_FONT.setMinimum(3)
        self.SMALL_FONT.setMaximum(36)
        self.SMALL_FONT.setValue(11)

        self.verticalLayout_7.addWidget(self.SMALL_FONT)


        self.gridLayout.addLayout(self.verticalLayout_7, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(700, 30))
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.URL = QLineEdit(Form)
        self.URL.setObjectName(u"URL")
        self.URL.setMaximumSize(QSize(700, 30))
        font5 = QFont()
        font5.setPointSize(12)
        self.URL.setFont(font5)
        self.URL.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.URL)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(700, 30))
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.MAIN_TITLE = QLineEdit(Form)
        self.MAIN_TITLE.setObjectName(u"MAIN_TITLE")
        self.MAIN_TITLE.setMaximumSize(QSize(700, 30))
        self.MAIN_TITLE.setFont(font5)
        self.MAIN_TITLE.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.MAIN_TITLE)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.OK = QPushButton(Form)
        self.OK.setObjectName(u"OK")
        self.OK.setMaximumSize(QSize(330, 50))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        self.OK.setFont(font6)

        self.horizontalLayout_2.addWidget(self.OK)

        self.CANCEL = QPushButton(Form)
        self.CANCEL.setObjectName(u"CANCEL")
        self.CANCEL.setMaximumSize(QSize(330, 50))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        self.CANCEL.setFont(font7)

        self.horizontalLayout_2.addWidget(self.CANCEL)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"settings", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"SUB_TITLE (\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u043a\u043e\u043b\u043e\u043d\u043d)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"LEFT_TITLE", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"RIGHT_TITLE", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"FONTS_SIZE", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"MAIN_FONT (\u0448\u0440\u0438\u0444\u0442 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0439 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439)", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"REGULAR_FONT (\u0448\u0440\u0438\u0444\u0442 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0439 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439)", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"BIG_FONT (\u0448\u0440\u0438\u0444\u0442 \u0447\u0438\u0441\u0435\u043b \u0434\u043d\u0435\u0439)", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"SMALL_FONT (\u0448\u0440\u0438\u0444\u0442 \u0434\u043d\u0435\u0439 \u043d\u0435\u0434\u0435\u043b\u044c)", None))
        self.label.setText(QCoreApplication.translate("Form", u"URL (\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"MAIN_TITLE (\u043e\u0431\u0449\u0438\u0439 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a)", None))
        self.OK.setText(QCoreApplication.translate("Form", u"OK", None))
        self.CANCEL.setText(QCoreApplication.translate("Form", u"CANCEL", None))
    # retranslateUi



class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.data = {
                'URL':'url_of_calendar',
                'MAIN_TITLE': 'main_title_to_app',
                'RIGHT_TITLE': 'title_to_right_column',
                'LEFT_TITLE': 'title_to_left_column',
                'MAIN_FONT': 13,
                'REGULAR_FONT': 12,
                'BIG_FONT': 18,
                'SMALL_FONT': 10}
        try:
            with open('data.json', 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError: 
            pass

        self.ui.URL.setText(self.data.get('URL', ''))
        self.ui.MAIN_TITLE.setText(self.data.get('MAIN_TITLE', ''))
        self.ui.RIGHT_TITLE.setText(self.data.get('RIGHT_TITLE', ''))
        self.ui.LEFT_TITLE.setText(self.data.get('LEFT_TITLE', ''))
        self.ui.MAIN_FONT.setValue(int(self.data.get('MAIN_FONT', '')))
        self.ui.REGULAR_FONT.setValue(int(self.data.get('REGULAR_FONT', '')))
        self.ui.BIG_FONT.setValue(int(self.data.get('BIG_FONT', '')))
        self.ui.SMALL_FONT.setValue(int(self.data.get('SMALL_FONT', '')))


        # close app 
        self.ui.CANCEL.clicked.connect(self.close)
        # save & close
        self.ui.OK.clicked.connect(self.push_ok)

    # func for put all data to dictonary & save to json file
    def push_ok(self):
        self.data['MAIN_TITLE'] = self.ui.MAIN_TITLE.text()
        self.data['URL'] = self.ui.URL.text()
        self.data['LEFT_TITLE'] = self.ui.LEFT_TITLE.text()
        self.data['RIGHT_TITLE'] = self.ui.RIGHT_TITLE.text()
        self.data['MAIN_FONT'] = self.ui.MAIN_FONT.value()
        self.data['REGULAR_FONT'] = self.ui.REGULAR_FONT.value()
        self.data['BIG_FONT'] = self.ui.BIG_FONT.value()
        self.data['SMALL_FONT'] = self.ui.SMALL_FONT.value()
        
        with open('data.json', 'w') as file:
            json.dump(self.data, file, ensure_ascii=False)

        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

