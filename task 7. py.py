# Function to manually sort a list (using bubble sort)
def manual_sort(numbers):
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


# Function to calculate sum, average, min, max
def analyze_list(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    average = total / len(numbers)

    return {
        "Sorted List": manual_sort(numbers.copy()),
        "Sum": total,
        "Average": round(average, 2),
        "Minimum": minimum,
        "Maximum": maximum
    }


# Function to print dictionary using enumerate
def print_stats(stats):
    print("\n--- List Analysis Summary ---")
    for index, (key, value) in enumerate(stats.items(), start=1):
        print(f"{index}. {key}: {value}")


# Main program
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

results = analyze_list(numbers)
print_stats(results)
