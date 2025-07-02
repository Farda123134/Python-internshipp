# Function to convert numeric score into letter grade
def get_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# Function to print grade summary
def print_grade_summary(*, name, score):
    grade = get_grade(score)
    if grade == "Invalid score":
        print(f"Student {name} has an invalid score: {score}")
    else:
        print(f"Student {name} scored {score} → Grade: {grade}")

# Example usage
print_grade_summary(name="Zara", score=87.5)
print_grade_summary(name="Ali", score=92)
print_grade_summary(name="Hassan", score=67)
print_grade_summary(name="Sara", score=49)
print_grade_summary(name="John", score=105)  # Invalid score
