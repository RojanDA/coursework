# Coursework

A collection of my IT coursework — reports, presentations, data analysis workbooks, and source code — covering artificial intelligence, data analytics, database systems, SQL, and network design.

## Contents

| Folder | Topic | Highlights |
| --- | --- | --- |
| [`8_Puzzle`](./8_Puzzle) | Artificial Intelligence | Python 8-Puzzle solver using A* search with Manhattan Distance heuristic, plus a Tkinter GUI |
| [`AI`](./AI) | Artificial Intelligence | Final report on intelligent agents |
| [`DA`](./DA) | Data Analytics | Tableau dashboards and reports on video game sales and Australian retail turnover, including predictive analytics |
| [`DataBase`](./DataBase) | Database Systems | Database project report and presentation |
| [`E-commerce SQL`](./E-commerce%20SQL) | SQL | E-commerce database design and query report |
| [`LMS SQL`](./LMS%20SQL) | SQL | Library Management System database design, report, and presentation |
| [`Network design`](./Network%20design) | Networking | Network design report and presentation |
| [`Optus_Data_Breach_Report`](./Optus_Data_Breach_Report) | Cybersecurity | Case study report on the Optus data breach |

## 8-Puzzle Solver

The only project here with runnable code. It solves the 8-Puzzle (3×3 sliding tile puzzle) using **A\* search** with the **Manhattan Distance** heuristic.

Requirements: Python 3.10+ with Tkinter. No external packages needed — standard library only.

```bash
cd 8_Puzzle
python eight_puzzle_ui_solver.py
```

The GUI lets you load sample puzzles (easy, medium, hard, unsolvable), enter a custom state, solve it, animate the solution step by step, and view statistics such as total moves, nodes expanded, time taken, and path cost. See [`8_Puzzle/README.txt`](./8_Puzzle/README.txt) for full usage instructions.

## Data Analytics

The `DA` folder contains Tableau workbooks (`.twb` / `.twbx`) and their supporting datasets. To open these you need [Tableau Desktop](https://www.tableau.com/products/desktop) or Tableau Public. The packaged `.twbx` file includes its data source; the `.twb` files expect the CSV files in the same directory.

## Notes

- Documents are in Microsoft Word (`.docx`) and PowerPoint (`.pptx`) format.
- Some Tableau extracts (`.hyper`) and CSV datasets are included so the workbooks open as intended.

---

**Author:** Rojan Poudel
