



from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap
import sys


class CarWidget(QWidget):
    def __init__(self, image_path, car_name, price, on_click):
        super().__init__()
        
        layout = QVBoxLayout()

        self.image_label = QLabel(self)
        self.pixmap = QPixmap(image_path)
        self.image_label.setPixmap(self.pixmap.scaled(400, 300))
        self.image_label.setFixedSize(400, 300)

        self.info_label = QLabel(f"{car_name}\nNarxi: {price} so'm", self)
        
        self.register_button = QPushButton("Sotib olish", self)
        self.register_button.clicked.connect(on_click)

        layout.addWidget(self.image_label)
        layout.addWidget(self.info_label)
        layout.addWidget(self.register_button)
        
        self.setLayout(layout)


class Cars(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Savdoda mavjud avtomobillar")
        self.setFixedSize(1600, 900)

        grid_layout = QGridLayout()

        cars_data = [
            ("Captiva.jpg", "Chevrolet Captiva 5T", "304 900 000"),
            ("Malibu.jpg", "Chevrolet Malibu-2", "419 000 960"),
            ("Traverse.jpg", "Chevrolet Traverse", "689 730 560"),
            ("Equinox.jpg", "Chevrolet Equinox", "416 000 000"),
            ("Tracker.jpg", "Chevrolet Tracker-2", "215 951 360"),
            ("Onix.jpg", "Chevrolet Onix", "161 900 000"),
            ("Damas.jpg", "Chevrolet Damas-2", "93 156 000")
        ]

        for index, (image_path, name, price) in enumerate(cars_data):
            row = index // 4
            column = index % 4
            car_widget = CarWidget(image_path, name, price, lambda checked, name=name: self.register(name))
            grid_layout.addWidget(car_widget, row, column)

        self.setLayout(grid_layout)

    def register(self, car_name):
        print(f"{car_name} avtomobilini ro'yxatdan o'tkazish...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Cars()
    win.show()
    sys.exit(app.exec_())


































