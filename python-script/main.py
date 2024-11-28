
from service.Function import *
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionUI()
    window.show()
    window.start_python_conda_detection()
    sys.exit(app.exec_())
