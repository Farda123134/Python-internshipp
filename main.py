# main.py

from manager import EmployeeManager
from utils import clear_screen # Assuming utils.py exists

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. List Employees")
    print("3. Search by Name/Department")
    print("4. Sort by Salary")
    print("5. Generate Report")
    print("6. Exit")
    print("----------------------------------")

def main():
    manager = EmployeeManager()

    while True:
        clear_screen() # Clear screen for a cleaner menu display
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.list_employees()
            input("\nPress Enter to continue...") # Pause to read output
        elif choice == '3':
            term = input("Enter search term (name or department): ").strip()
            manager.search_employee(term)
            input("\nPress Enter to continue...")
        elif choice == '4':
            while True:
                sort_order = input("Sort by salary (A for Ascending, D for Descending): ").strip().lower()
                if sort_order == 'a':
                    manager.sort_by_salary(desc=False)
                    break
                elif sort_order == 'd':
                    manager.sort_by_salary(desc=True)
                    break
                else:
                    print("Invalid choice. Please enter 'A' or 'D'.")
            input("\nPress Enter to continue...")
        elif choice == '5':
            manager.generate_report()
            input("\nPress Enter to continue...")
        elif choice == '6':
            manager.exit_system()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()