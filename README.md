# 🐍 CodSoft Python Programming Internship

A collection of **five command-line Python applications** built during the CodSoft internship program. Each project demonstrates core Python fundamentals — from control flow and data structures to input validation, exception handling, and modular design.

---

## 📂 Projects

| # | Project | Directory | Description |
|---|---------|-----------|-------------|
| 1 | [Calculator](#-calculator) | `calc/` | Multi-mode scientific calculator with history & settings |
| 2 | [Rock Paper Scissors](#-rock-paper-scissors) | `Rock Paper Scissors/` | Classic RPS game with score tracking & auto-play mode |
| 3 | [Password Generator](#-password-generator) | `PASS-GEN/` | Secure password generator with configurable complexity |
| 4 | [To-Do List](#-to-do-list) | `To-do/` | Task manager with add, complete & delete functionality |
| 5 | [Contact Book](#-contact-book) | `contact/` | CRUD-based contact management system |

---

## 🔧 Prerequisites

- **Python 3.x** — no external packages required  
- All projects use only the Python standard library (`math`, `os`, `random`, `secrets`)

---

## 🧮 Calculator

**File:** [`cal_cui.py`](calc/cal_cui.py)

A feature-rich, menu-driven calculator with three calculation modes, a configurable settings panel, and a built-in calculation history system.

### Modes

| Mode | Operations |
|------|-----------|
| **Arithmetic** | Addition, Subtraction, Multiplication, Division |
| **Advanced** | Power, Exponential (e^x), Natural Logarithm, Nth Root |
| **Trigonometric** | sin, cos, tan, cot, sec, csc |

### Highlights

- **Calculation History** — stores recent results with configurable capacity (default: 3 records)
- **Settings Module** — adjust decimal precision (default: 2), switch between Degree / Radian mode, manage history size
- **Robust Error Handling** — catches division by zero, log of non-positive numbers, undefined trig values, overflow errors, and invalid inputs
- **Built-in Documentation** — in-app *How to Use* guide and full project documentation

### Run

```bash
python calc/cal_cui.py
```

---

## ✊ Rock Paper Scissors

**File:** [`RPS_CUI.py`](Rock%20Paper%20Scissors/RPS_CUI.py)

A classic Rock Paper Scissors game against the computer with live score tracking and detailed session statistics.

### Features

- Standard RPS gameplay with random computer moves
- **Live Scoreboard** — tracks wins, losses, ties, total games, and win-rate percentage
- **🥚 Secret Auto-Play Mode** — enter `420` at the menu to run *N* automated rounds
- In-app *How to Play* guide and full documentation

### Run

```bash
python "Rock Paper Scissors/RPS_CUI.py"
```

---

## 🔐 Password Generator

**File:** [`PSGEN-CUI.py`](PASS-GEN/PSGEN-CUI.py)

A secure, customisable password generator powered by Python's cryptographically secure `secrets` module.

### Complexity Levels

| Setting | Character Set |
|---------|--------------|
| 1 | Letters only (a-z, A-Z) |
| 2 | Letters + Digits (0-9) |
| 3 *(default)* | Letters + Digits + Symbols (!@#$%^&*()) |

### Features

- User-specified password length (any positive integer)
- Persistent complexity setting across generations within a session
- Cryptographically secure randomness via `secrets.choice()`
- In-app help guide

### Run

```bash
python PASS-GEN/PSGEN-CUI.py
```

---

## ✅ To-Do List

**File:** [`to-do_CUI.py`](To-do/to-do_CUI.py)

A lightweight task manager for adding, viewing, completing, and deleting tasks from the command line.

### Features

- **Add** tasks with a title
- **View** all tasks with `[Done]` / `[Pending]` status indicators
- **Mark tasks as complete** — prevents redundant completion
- **Delete** tasks by number
- Input validation and empty-task protection

### Run

```bash
python To-do/to-do_CUI.py
```

---

## 📇 Contact Book

**File:** [`contact-cui.py`](contact/contact-cui.py)

A full CRUD contact management system storing name, phone, email, and address for each entry.

### Features

- **Add** contacts with duplicate phone-number detection
- **View** all contacts in a formatted list
- **Search** by name (case-insensitive) or phone number
- **Update** any field — leave blank to keep the current value
- **Delete** contacts by index
- In-app documentation and usage guide

### Run

```bash
python contact/contact-cui.py
```

---

## 🛠️ Tech Stack & Concepts

All projects are **pure Python 3** with zero external dependencies.

| Concept | Used In |
|---------|---------|
| Menu-driven architecture | All projects |
| Input validation & exception handling | All projects |
| Cross-platform console clearing | All projects |
| Cryptographic randomness (`secrets`) | Password Generator |
| `math` module (trig, log, exp, pow) | Calculator |
| List of dictionaries (CRUD) | Contact Book, To-Do List |
| Score / state management | RPS, Calculator (history) |
| Randomisation (`random`) | Rock Paper Scissors |

---

## 📁 Repository Structure

```
codsoft/
├── calc/
│   └── cal_cui.py              # Scientific calculator
├── Rock Paper Scissors/
│   └── RPS_CUI.py              # Rock Paper Scissors game
├── PASS-GEN/
│   └── PSGEN-CUI.py            # Password generator
├── To-do/
│   └── to-do_CUI.py            # To-do list manager
├── contact/
│   └── contact-cui.py          # Contact management system
└── README.md
```

---

## 👨‍💻 Developer

**Aaron Shibu Mammen**  
B.E. Computer Science and Engineering — First Year  
GitHub: [@aaroninplayz](https://github.com/aaroninplayz)

---

## 📄 License

This project is open-source and available for educational purposes.
