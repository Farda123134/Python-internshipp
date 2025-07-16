# manager.py

from employee import Employee
import os

class EmployeeManager:
    def __init__(self, data_file='employee_data.txt', report_file='employee_report.txt'):
        self.data_file = data_file
        self.report_file = report_file
        self.employees = []
        self._load_from_file()

    def _load_from_file(self):
        """Loads employee data from the specified text file on startup."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                for line in f:
                    employee = Employee.from_string(line)
                    if employee:
                        self.employees.append(employee)
        print(f"Loaded {len(self.employees)} employee records from {self.data_file}")

    def _save_to_file(self):
        """Saves current employee data to the specified text file on exit."""
        with open(self.data_file, 'w') as f:
            for employee in self.employees:
                f.write(str(employee) + '\n')
        print(f"Saved {len(self.employees)} employee records to {self.data_file}")

    def add_employee(self):
        """Inputs new employee details and adds to the list."""
        print("\nEnter New Employee Details:")
        while True:
            name = input("Name: ").strip()
            if name:
                break
            else:
                print("Name cannot be empty. Please try again.")

        while True:
            department = input("Department: ").strip()
            if department:
                break
            else:
                print("Department cannot be empty. Please try again.")

        while True:
            try:
                salary = float(input("Salary: "))
                if salary <= 0:
                    print("Salary must be a positive number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid salary. Please enter a number.")

        while True:
            try:
                joining_year = int(input("Joining Year: "))
                if not (1900 <= joining_year <= 2025): # Simple year validation
                    print("Joining year seems unrealistic. Please enter a more reasonable year (e.g., between 1900 and 2025).")
                else:
                    break
            except ValueError:
                print("Invalid year. Please enter a whole number.")

        new_employee = Employee(name, department, salary, joining_year)
        self.employees.append(new_employee)
        print(f"Employee {name} added successfully!")
        self._save_to_file() # Save immediately after adding

    def list_employees(self):
        """Displays all employee records."""
        if not self.employees:
            print("\nNo employee records found.")
            return
        print("\n--- All Employee Records ---")
        for emp in self.employees:
            emp.display()
        print("----------------------------")

    def search_employee(self, term):
        """Filters employees by name or department using lambda."""
        search_results = list(filter(lambda emp: term.lower() in emp.name.lower() or term.lower() in emp.department.lower(), self.employees))
        if not search_results:
            print(f"\nNo employees found matching '{term}'.")
            return
        print(f"\n--- Search Results for '{term}' ---")
        for emp in search_results:
            emp.display()
        print("-----------------------------------")

    def sort_by_salary(self, desc=False):
        """Sorts employees by salary."""
        self.employees.sort(key=lambda emp: emp.salary, reverse=desc)
        order = "descending" if desc else "ascending"
        print(f"\nEmployees sorted by salary in {order} order.")
        self.list_employees() # Display sorted list

    def generate_report(self):
        """Writes a summary report to employee_report.txt."""
        total_employees = len(self.employees)
        if total_employees == 0:
            report_content = "No employee records available to generate a report."
        else:
            total_salary = sum(emp.salary for emp in self.employees)
            average_salary = total_salary / total_employees

            department_salaries = {}
            for emp in self.employees:
                department_salaries.setdefault(emp.department, {'count': 0, 'total_salary': 0})
                department_salaries[emp.department]['count'] += 1
                department_salaries[emp.department]['total_salary'] += emp.salary

            report_content = "--- Employee Summary Report ---\n"
            report_content += f"Total Employees: {total_employees}\n"
            report_content += f"Total Payroll: ${total_salary:,.2f}\n"
            report_content += f"Average Salary: ${average_salary:,.2f}\n\n"
            report_content += "--- Department-wise Summary ---\n"
            for dept, data in department_salaries.items():
                report_content += f"Department: {dept} (Employees: {data['count']}, Avg Salary: ${data['total_salary']/data['count']:,.2f})\n"
            report_content += "-------------------------------\n"

        with open(self.report_file, 'w') as f:
            f.write(report_content)
        print(f"\nSummary report generated and saved to {self.report_file}")

    def exit_system(self):
        """Saves data and prepares for exit."""
        self._save_to_file()
        print("Exiting Employee Management System. Goodbye!")