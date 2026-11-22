# Last Train

A small turn-based game about catching the last train of the night, made with Python and PySide6.

## Description

You're at a train station late at night and the last train is about to leave. To get on it you need two things: your backpack and a ticket. Then you have to make it to the platform. The catch is that you only have a few turns, and almost everything you do uses some of them.

So the game is really about figuring out the right order of actions. If you waste even one turn on something you didn't need, you'll probably watch the train leave without you. If that happens, you can just restart and try a different plan.

There are two modes:

- **Normal** – you get 4 turns. Good for your first try while you're still working out how things work.
- **Survival** – you get 3 turns. There's basically no room for mistakes, so you need to find the most efficient route.

I made this as a small project to practice Python and building a GUI with PySide6.

### Screenshots

<img width="575" height="651" alt="Снимок экрана — 2026-11-21 в 14 23 17" src="https://github.com/user-attachments/assets/ae727a8a-4a40-42ea-ad46-84c2b23a7123" />


## Getting Started

### Dependencies

* Python 3.9 or newer
* PySide6
* Works on Windows, macOS and Linux (anywhere PySide6 runs)

### Installing

* Clone the repository or download it as a ZIP:
```
git clone https://github.com/YOUR_USERNAME/last-train.git
cd last-train
```
* Install PySide6:
```
pip install PySide6
```

### Executing program

* Go to the project folder
* Run the main file:
```
python main.py
```
* Choose Normal or Survival mode
* Pick your actions and try to board the train before you run out of turns

## Help

If the game doesn't start, first check that PySide6 is installed:
```
pip show PySide6
```
If `python` doesn't work, try `python3` instead (on macOS and Linux it's usually `python3`).

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
