# Coursework

A collection of my IT coursework — reports, presentations, data analysis workbooks, lab exercises, and source code — covering artificial intelligence, data analytics, database systems, programming, networking, and security.

## Contents

### Programming & Computer Science

| Folder | Description |
| --- | --- |
| [`8_Puzzle`](./8_Puzzle) | Python 8-Puzzle solver using A* search with Manhattan Distance heuristic, plus a Tkinter GUI |
| [`python`](./python) | Python lesson exercises and practice scripts |
| [`Java`](./Java) | Java workbook exercises and projects |
| [`HtmlCssJavaScript`](./HtmlCssJavaScript) | HTML, CSS, and JavaScript lessons and practice pages |
| [`information security`](./information%20security) | Information security lab report and Python lab work (Huffman coding, JPEG DCT, encryption exercises) |

### Databases & SQL

| Folder | Description |
| --- | --- |
| [`DataBase`](./DataBase) | Database project report and presentation |
| [`MySQL`](./MySQL) | MySQL practice — data cleaning, exploratory data analysis, and an HR dataset project |
| [`PostgreSQL`](./PostgreSQL) | PostgreSQL lessons, Q&A exercises, and table design scripts |
| [`E-commerce SQL`](./E-commerce%20SQL) | E-commerce database design and query report |
| [`LMS SQL`](./LMS%20SQL) | Library Management System database design, report, and presentation |

### Data Analytics

| Folder | Description |
| --- | --- |
| [`Tableau`](./Tableau) | Tableau dashboards and reports on video game sales and Australian retail turnover, including predictive analytics |
| [`Excel`](./Excel) | Excel lesson workbooks — formulas, conditional formatting, pivot tables, Power Pivot, and Office 365 formulas |

### Artificial Intelligence

| Folder | Description |
| --- | --- |
| [`AI Report`](./AI%20Report) | Final report on intelligent agents |

### Networking & Security

| Folder | Description |
| --- | --- |
| [`Network design`](./Network%20design) | Network design report and presentation |
| [`Optus_Data_Breach_Report`](./Optus_Data_Breach_Report) | Case study report on the Optus data breach |

### Other

| Folder | Description |
| --- | --- |
| [`CareLink_HMS`](./CareLink_HMS) | Hospital management system project report and budget |
| [`HealthCare`](./HealthCare) | Healthcare report |
| [`multimedia system`](./multimedia%20system) | Multimedia systems lab report with audio and image assets |
| [`CorporateFinancialManagement`](./CorporateFinancialManagement) | FIN200 corporate financial management assessment |
| [`Certificate`](./Certificate) | Course completion certificates (Excel, Python, SQL) |

## 8-Puzzle Solver

The most complete runnable project here. It solves the 8-Puzzle (3×3 sliding tile puzzle) using **A\* search** with the **Manhattan Distance** heuristic.

Requirements: Python 3.10+ with Tkinter. No external packages needed — standard library only.

```bash
cd 8_Puzzle
python eight_puzzle_ui_solver.py
```

The GUI lets you load sample puzzles (easy, medium, hard, unsolvable), enter a custom state, solve it, animate the solution step by step, and view statistics such as total moves, nodes expanded, time taken, and path cost. See [`8_Puzzle/README.txt`](./8_Puzzle/README.txt) for full usage instructions.

## Notes

- Documents are in Microsoft Word (`.docx`) and PowerPoint (`.pptx`) format.
- Tableau workbooks (`.twb` / `.twbx`) require [Tableau Desktop](https://www.tableau.com/products/desktop) or Tableau Public. The packaged `.twbx` file includes its data source; `.twb` files expect the CSV files in the same directory.
- Some Tableau extracts (`.hyper`) and CSV datasets are included so the workbooks open as intended.
- IDE configuration folders (`.idea/`, `.vscode/`), build output, and OS thumbnail files are excluded via `.gitignore`.

---

**Author:** Rojan Poudel
