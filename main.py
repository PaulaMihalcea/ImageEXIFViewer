import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from model import ImageModel
from view import View
from controller import Controller

app = QApplication(sys.argv)  # Note: There must be exactly one instance of QApplication active at a time
app.setWindowIcon(QIcon('icons/ieviewer.png'))

model = ImageModel()
view = View(model)

controller = Controller(model, view)

main_window = controller.get_main_window()
main_window.show()

sys.exit(app.exec_())
