# Day11_EmployeeManager

A command-line-based Employee Management System built with Python, demonstrating OOP principles, file handling, and modular design.

## Features

* **Employee Class**: Stores and displays employee details (name, department, salary, joining year).
* **EmployeeManager Class**:
    * Loads/saves employee data from/to `employee_data.txt`.
    * Adds new employees with input validation.
    * Lists all registered employees.
    * Searches employees by name or department.
    * Sorts employees by salary (ascending/descending).
    * Generates a summary report (`employee_report.txt`).
* **Modular Design**: Code is split into `employee.py`, `manager.py`, and `main.py` (with `utils.py` for common functions).
* **Error Handling**: Basic `try-except` blocks for invalid numerical inputs.
* **CLI Menu**: Interactive command-line interface.

## How to Run

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/Farda123134/Python-internshipp.git](https://github.com/Farda123134/Python-internshipp.git)
    cd Python-internshipp
    ```
2.  **Run the main application**:
    ```bash
    python main.py
    ```
   

## Project Structure