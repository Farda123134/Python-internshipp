# employee.py

class Employee:
    def __init__(self, name, department, salary, joining_year):
        self.name = name
        self.department = department
        self.salary = float(salary)
        self.joining_year = int(joining_year)

    def display(self):
        """Prints employee details in a formatted style."""
        print(f"Name: {self.name}, Department: {self.department}, Salary: ${self.salary:,.2f}, Joining Year: {self.joining_year}")

    def __str__(self):
        """Returns a string representation for file storage."""
        return f"{self.name},{self.department},{self.salary},{self.joining_year}"

    @staticmethod
    def from_string(emp_str):
        """Creates an Employee object from a string (e.g., from file)."""
        parts = emp_str.strip().split(',')
        if len(parts) == 4:
            return Employee(parts[0], parts[1], parts[2], parts[3])
        return None