def read_marks_file(file_path):
    student_marks = {}
    skipped_entries = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                try:
                    name, mark = line.split(',')
                    name = name.strip()
                    mark = mark.strip()

                    if name == "" or mark == "":
                        raise ValueError("Missing value")

                    mark = int(mark)
                    student_marks[name] = mark

                except ValueError:
                    print(f"Skipped invalid line: {line}")
                    skipped_entries += 1

    except FileNotFoundError:
        raise

    return student_marks, skipped_entries


def display_marks(student_marks):
    try:
        if not student_marks:
            raise ZeroDivisionError("No valid data to display.")

        total = 0
        print("\nStudent Marks:")
        for name, mark in student_marks.items():
            print(f"{name}: {mark}")
            total += mark

        average = total / len(student_marks)
        print(f"\nAverage Marks: {average:.2f}")

    except ZeroDivisionError as e:
        print(e)


def main():
    while True:
        file_path = input("Enter the file path: ")
        try:
            student_marks, skipped = read_marks_file(file_path)
            display_marks(student_marks)
            print(f"\nSkipped Entries: {skipped}")
            break  # Exit the loop after successful execution
        except FileNotFoundError:
            print("File not found. Please try again.\n")


if __name__ == "__main__":
    main()
