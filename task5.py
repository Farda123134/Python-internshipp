# 🔹 Step 1: Define the function
def calculate_gpa(grades, total_credit_hours=15):
    """
    Calculates GPA from a list of grades.
    grades: list of grade points (e.g., [3.0, 3.7, 2.7])
    total_credit_hours: total number of credit hours (default is 15)
    """
    if not grades:
        return 0.0

    total_points = sum(grades)
    gpa = total_points / len(grades)
    return round(gpa, 2)


# 🔹 Step 2: Example usage

# Using positional arguments
grades_list = [3.7, 3.3, 2.7, 4.0, 3.0]
gpa1 = calculate_gpa(grades_list)
print("GPA (positional):", gpa1)

# Using named arguments
gpa2 = calculate_gpa(grades=[2.0, 2.7, 3.0, 3.3, 3.7], total_credit_hours=15)
print("GPA (named arguments):", gpa2)

