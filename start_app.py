"""
Creation date of this program: march 2019
Author: L. Gardy
E-mail: ludovic.gardy@cnrs.fr
Encoding: UTF-8
"""
import sys
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import (QApplication)

from ladybird_MRI_app.mri_main_window import Main_Win

if __name__ == "__main__":
    # Avoid python kernel from dying
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    # run
    mywindow = Main_Win()
    mywindow.show()
    sys.exit(app.exec())
