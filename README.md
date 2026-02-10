# Malom (Nine Men's Morris) – Python GUI

## 📌 Project Overview

This project is a **Python-based, graphical (GUI) implementation** of the classic board game **Malom** (also known as **Nine Men's Morris** or *Three Men's Game* in some variations).

The goal of the project was to recreate a **traditional strategy board game** in a digital form, focusing on game logic, state management, and GUI interaction. The project was developed primarily for **learning and portfolio purposes**.

The game is **playable in its current state**, with the core mechanics implemented. Some advanced rules and edge cases are still under development, but the project already demonstrates:

* problem-solving and algorithmic thinking,
* object-oriented design in Python,
* integration of game rules with a graphical user interface,
* clean and modular code structure.

---

## 🎮 Game Description

Malom is a two-player strategic board game where the objective is to reduce the opponent to fewer than three pieces or block all possible moves.

### Implemented Rules

* Two players take turns
* Players place pieces on the board during the placement phase
* Forming a **mill** (three pieces in a row) allows a player to remove one opponent piece
* After all pieces are placed, players can move pieces to **adjacent positions**
* The game state updates dynamically through the GUI

### Not Fully Implemented / Known Limitations

* ⚠️ **Flying rule**: when a player has only three pieces left, they should be able to move to any empty position (not yet implemented)
* ⚠️ Minor bugs may occur in rare edge cases related to move validation or GUI updates

---

## 🎯 Project Goals

* Recreate a classic board game in Python
* Practice object-oriented programming principles
* Implement and manage complex game rules
* Build a presentable portfolio project for IT / game development paths

This project is **not intended for production use**, but as a learning and demonstration project.

---

## 🗂️ Project Structure

```
malom/
│
├── main.py        # Program entry point, GUI initialization
├── game.py        # Game rules, turns, and state management
├── ring.py        # Board rings and connection logic
├── dot.py         # Representation of board positions
└── README.md      # Project documentation
```

The codebase follows a modular structure, with each file having a clear responsibility.

---

## ▶️ How to Run

### Requirements

* Python 3.9 or newer
* No external dependencies (standard Python libraries only)

### Run the Game

```bash
python main.py
```

---

## 🧪 Testing

No automated unit tests are included at this stage. The game has been tested manually through gameplay using the GUI.

---

## 🐞 Known Issues and Missing Features

* Flying rule (movement with only 3 pieces remaining) is missing
* Some edge cases may cause incorrect move validation
* Win conditions related to fully blocking an opponent are not fully handled

---

## 🔧 Possible Improvements

* Implement the flying rule
* Complete win-condition logic
* Refactor and further document the code
* Add a simple AI opponent
* Introduce unit tests
* Improve graphical assets and UI feedback

---

## 👤 Author

**Milán Zupán**
Python / Game Development practice project

---

## 📜 Notes

This project was created for learning and portfolio purposes. The focus is on gameplay logic and structure rather than polished visuals or full feature completeness.
