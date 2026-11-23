import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


from PySide6.QtCore import QTimer



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Class5")
        self.setMinimumWidth(200)

        self.counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)


        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10000)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet("background-color: lightgray;")

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        layout = QVBoxLayout()
        layout.addWidget(self.spin_box)
        layout.addWidget(self.toggle_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def button_method(self, is_running: bool) -> None:
        checked = self.toggle_button.isChecked()
        self.toggle_button.setText("Stop" if is_running else "Start")
        if checked:
            self.counter = 0
            self.timer.start(10)
        else:
            self.timer.stop()


    def timer_method(self):
        self.counter+=1
        self.spin_box.setValue(self.counter)



def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
