import select
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QDialog
from PySide6.QtCore import Qt
from game import Game
from intro import show_intro
import station
game = Game(4,False,False)
app = QApplication()
result_label = QLabel()
backpack_label = QLabel("Backpack: No")
button = QPushButton("Buy a ticket")
machine_button = QPushButton("Use tikcet machine(1 turn)")
platform_button = QPushButton("Go to the Platform")
restart_button = QPushButton("Play Again")
menu_button = QPushButton("Exit to main menu")
restart_button.setStyleSheet("background-color: red;color: white;border: none;border-radius: 8px;")
restart_button.hide()
restart_button.setMinimumHeight(64)
backpack_button = QPushButton("Pick Up  backpack")
backpack_button.setMinimumHeight(64)
button.setMinimumHeight(64)
platform_button.setMinimumHeight(64)
window = QWidget()
window.setObjectName("gameWindow")
window.setStyleSheet("background-color: blue;")
ticket_label = QLabel("Ticket: No")
label = QLabel(f"Turns left: {game.count}")
location_label = QLabel(f"Location: {game.location}")
map_label = QLabel("\n".join(station.location))
window.setWindowTitle("LastTrain")
outher_layout = QHBoxLayout(window)
panel = QWidget()
panel.setMaximumWidth(600)
panel.setMinimumWidth(520)
outher_layout.addWidget(panel,0,Qt.AlignmentFlag.AlignCenter)
layout = QVBoxLayout(panel)
layout.setSpacing(12)
layout.addWidget(location_label)
layout.addWidget(map_label)
title_label = QLabel("LAST TRAIN")
title_label.setStyleSheet("color : gold;font-size: 36px;font-weight: bold;")
actions_panel = QWidget()
actions_layout = QVBoxLayout(actions_panel)
layout.addWidget(title_label)
layout.addWidget(label)
layout.addWidget(ticket_label)
layout.addWidget(backpack_label)
actions_layout.addWidget(button)
actions_layout.addWidget(machine_button)
actions_layout.addWidget(backpack_button)
actions_layout.addWidget(platform_button)
layout.addWidget(result_label)
layout.addWidget(actions_panel)
layout.addWidget(restart_button)
layout.addWidget(menu_button)
actions_panel.setStyleSheet("color: black;background-color: gold;border: none;border-radius: 8px;")
def update_map():
    row = []
    for i in station.location:
        place = i
        if place == game.location:
            row.append(f"▶{place}")
        else:
            row.append(place)
    map_label.setText("\n".join(row))
update_map()
def buy_ticket():
    bouht = game.buy_ticket()
    if bouht:
        pass
    else:
        result_label.setText(f"You need 2 turns to buy a ticket at the ticket office.")
        return
    label.setText(f"Turns left: {game.count}")
    location_label.setText(f"Location: {game.location}")
    update_map()
    if game.has_ticket:
        ticket_label.setText("Ticket: Yes")

    if game.count == 0:
        finish_game("The train has left.")
button.clicked.connect(buy_ticket)
def pick_up_backed():
    pick_up = game.pick_up_backed()
    if not pick_up:
        result_label.setText("You already have your backpack")
    backpack_label.setText("Backpack: Yes")
    label.setText(f"Turns left: {game.count}")
    location_label.setText(f"Location: {game.location}")
    update_map()
    if game.count == 0:
        finish_game("The train has left.")


backpack_button.clicked.connect(pick_up_backed)
def click():
    boarder = game.go_to_platform()
    label.setText(f"Turns left: {game.count}")
    location_label.setText(f"Location: {game.location}")
    update_map()
    if boarder:
        if game.count == 0:
            finish_game("Just in time! You caught the last train")
        else:
            finish_game("You caught the last train with time to spare!")
    elif game.count == 0:
        finish_game("The train has left.")
    else:
        result_label.setText("You need your ticket and backpack to board.")

platform_button.clicked.connect(click)

def finish_game(message):
    result_label.setText(message)
    button.setEnabled(False)
    platform_button.setEnabled(False)
    backpack_button.setEnabled(False)
    machine_button.setEnabled(False)
    restart_button.show()

def restart_game():
    game.count = start_tuwns
    game.has_ticket = False
    game.has_backed = False
    game.location = station.Entrance
    location_label.setText(f"Location: {game.location}")
    label.setText(f"Turns left: {game.count}")
    backpack_label.setText("Backpack: No")
    ticket_label.setText("Ticket: No")
    update_map()
    result_label.clear()
    button.setEnabled(True)
    platform_button.setEnabled(True)
    backpack_button.setEnabled(True)
    machine_button.setEnabled(True)
    restart_button.hide()

def use_machine():
    bouht = game.buy_from_machine()

    if bouht:
        result_label.clear()
    else:
        result_label.setText(f"Pick up your backpack before using the ticket machine")
        return
    label.setText(f"Turns left: {game.count}")
    location_label.setText(f"Location: {game.location}")
    update_map()
    if game.has_ticket:
        ticket_label.setText("Ticket: Yes")

    if game.count == 0:
        finish_game("The train has left.")
def back_to_menu():
    global start_tuwns
    select_turns = show_intro()
    if select_turns is None:
        return
    else:
        start_tuwns = select_turns
    restart_game()
menu_button.setStyleSheet("background-color: pink; color: black")
machine_button.clicked.connect(use_machine)
menu_button.clicked.connect(back_to_menu)
start_tuwns = show_intro()
if start_tuwns is not None:
    restart_button.clicked.connect(restart_game)
    restart_game()
    window.show()
    app.exec()