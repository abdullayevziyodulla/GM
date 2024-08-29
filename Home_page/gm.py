from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Asosiy layout
        layout = QVBoxLayout()

        # Kompaniya tugmasi
        self.company_button = QPushButton('Kompaniya', self)
        self.company_button.clicked.connect(self.onCompanyButtonClick)
        layout.addWidget(self.company_button)

        # Layoutni o'rnatish
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 Application')
        self.setGeometry(300, 300, 300, 200)

    def onCompanyButtonClick(self):
        # Yangi label yaratish
        label = QLabel('GM haqida ma\'lumot', self)
        self.layout().addWidget(label)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
