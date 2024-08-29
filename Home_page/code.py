from PIL.GimpGradientFile import GimpGradientFile
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont

class Home_page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1930, 1000)
        self.setWindowTitle("Home page")

        self.label_for_img = QLabel(self)
        self.label_for_img.setGeometry(0, 0, 1930, 1000)
        self.label_for_img.setPixmap(QPixmap("uz.png"))
        self.label_for_img.setScaledContents(True)

        self.font = QFont("Arial", 15, 80)

        self.btn = QPushButton("Konpaniyalar", self)
        self.btn.setGeometry(30, 20, 171, 41)
        self.btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0);
                color: white;
                border: none;
            }
            QPushButton:hover {
                color: blue;
            }
        """)
        self.btn.setFont(self.font)

        self.btn1 = QPushButton("Mashinalar", self)
        self.btn1.setGeometry(210, 20, 171, 41)
        self.btn1.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0);
                color: white;
                border: none;
            }
            QPushButton:hover {
                color: blue;
            }
        """)
        self.btn1.setFont(self.font)

        self.btn2 = QPushButton("Haridlar", self)
        self.btn2.setGeometry(390, 20, 171, 41)
        self.btn2.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0);
                color: white;
                border: none;
            }
            QPushButton:hover {
                color: blue;
            }
        """)
        self.btn2.setFont(self.font)

        self.btn3 = QPushButton("Ehtiyot qisimlar", self)
        self.btn3.setGeometry(570, 20, 171, 41)
        self.btn3.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0);
                color: white;
                border: none;
            }
            QPushButton:hover {
                color: blue;
            }
        """)
        self.btn3.setFont(self.font)

        self.search = QLineEdit(self)
        self.search.setGeometry(1600, 20, 280, 50)
        self.search.setPlaceholderText("Search...")
        self.search.setStyleSheet("""
            border: 2px solid blue; 
            border-radius: 20px;  
        """)
        self.search.setFont(QFont("Arial", 20))

        self.btn.clicked.connect(self.cmp)

    def cmp(self):
        self.center_box = QLabel("""
General Motors Company (GM) - Amerika Qo'shma Shtatlaridagi mashhur avtomobil ishlab chiqaruvchi kompaniya.

GM 1908-yilda tashkil etilgan va dunyodagi eng katta avtomobil ishlab chiqaruvchilardan biri hisoblanadi. Kompaniya o'zining ko'plab avtomobil brendlari bilan tanilgan, masalan:

Chevrolet: Boshqa brendlar orasida mashhur bo'lgan bu markaning turli modellari mavjud.

Buick: Premium va qulay avtomobillar ishlab chiqaradi.

GMC: Asosan yuk mashinalari va SUV-lar bilan tanilgan.

Cadillac: Luxury segmentda joylashgan brend.

GM ning asosiy boshqaruv markazi Detroit, Michigan shahrida joylashgan. Kompaniya avtomobillar, yuk mashinalari va boshqa transport vositalarini ishlab chiqaradi va dunyo bo'ylab sotadi.

GM avtomobil sanoatida innovatsion texnologiyalarni rivojlantirish bilan ham mashhur, jumladan elektr va gidrojenli avtomobillar bo'yicha yangi loyihalar ustida ishlaydi
""", self)
        self.center_box.move(50, 100)
        self.center_box.setFont(self.font)
        self.center_box.setStyleSheet('background-color: lightblue; border-radius: 15px;')
        self.opasity = QGraphicsOpacityEffect(self)
        self.opasity.setOpacity(0.7)
        self.center_box.setGraphicsEffect(self.opasity)
        self.center_box.adjustSize()
        self.center_box.show()

        self.hide = QPushButton("Hide Text", self)
        self.hide.setFixedSize(250, 50)
        self.hide.setStyleSheet("""
                QPushButton {
                    border: 3px solid blue; 
                    border-radius: 10px;
                    font-size: 30px;
                    color: white;
                }
                QPushButton:hover {
                    background-color: blue;
                    border: 2px solid black;
                    color: black;
                }
            """)
        self.hide.setFont(QFont('Arial', 22, 60))
        self.hide.move(50, 900)
        self.hide.show()
        self.hide.clicked.connect(self.hidee)

    def hidee(self):
        self.hide.hide()
        self.center_box.hide()



app = QApplication([])
win = Home_page()
win.show()
app.exec_()
