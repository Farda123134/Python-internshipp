# 🔹 Step 1: Store student IDs in a tuple (immutable)
student_ids = (101, 102, 103, 104)
print("Student IDs (Tuple):", student_ids)

# 🔹 Step 2: Create a set of unique course names
courses = {"Python", "AI", "ML"}
print("Initial Courses (Set):", courses)

# 🔹 Step 3: Add a new course to the set
courses.add("Data Science")  # Adds 'Data Science' if not already in the set
print("After Adding 'Data Science':", courses)

# 🔹 Step 4: Try to add a duplicate course
courses.add("Python")  # Duplicate, won't be added
print("After Adding Duplicate 'Python':", courses)

# 🔹 Step 5: Remove a course from the set
courses.remove("ML")  # Removes 'ML' from the set
print("After Removing 'ML':", courses)

# 🔹 Step 6: Print final course list
print("Final Course List:", courses)

