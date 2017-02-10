import sys
from maingui import MainGui
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    form = MainGui()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()