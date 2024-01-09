from threading import Lock
from typing import List
from pathlib import Path
from functools import partial
from typing import List, Dict, Union, Tuple
import os

from PyQt5.QtWidgets import QMainWindow, QOpenGLWidget
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QCloseEvent, QAction

from QtForms.MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # Предустановка свойств
        self.setup_properties()

        # Установка соединений между виджетами
        self.setup_connections()

        # Финальное завершение вида окна
        self.showMaximized()