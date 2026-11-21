from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog,QComboBox
from PySide6.QtCore import Qt

def show_intro():
    dialog = QDialog()
    intro_label = QLabel("Welcome to LastTrain!")
    intro_panel = QWidget()
    intro_panel.setFixedWidth(520)
    layout = QVBoxLayout(intro_panel)
    layout.addWidget(intro_label)
    rules_label = QLabel("normal: 4 turns Survival 3 turns.\nThe Ticket office costs 2 turns.\nThe ticket machine costs 1 turn and requires your backpack.\nPicking up your backpack and going to the platform each cost 1 turn.\nBring both your ticket and backpack to board the train.")
    continue_button = QPushButton("Continue")
    continue_button.clicked.connect(dialog.accept)
    layout.addWidget(rules_label)
    mode_box = QComboBox()
    mode_box.addItem("Normal : (4 turns)",4)
    mode_box.addItem("Survival : (3 turns)",3)
    layout.addWidget(continue_button)
    layout.addWidget(mode_box)
    rules_label.setWordWrap(True)
    Qhbox = QHBoxLayout(dialog)
    intro_label.setStyleSheet("font-size:36px;font-weight:bold;color:gold;")
    rules_label.setStyleSheet("font-size: 20px")
    Qhbox.addWidget(intro_panel,0,Qt.AlignmentFlag.AlignCenter)
    if  dialog.exec() == QDialog.DialogCode.Accepted:
        return mode_box.currentData()
