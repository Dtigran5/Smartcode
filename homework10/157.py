def convert_grade(grade):
    grade_points = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'D-': 0.7,
        'F': 0.0
    }
    
    letter_grades = {v: k for k, v in grade_points.items()}

    try:
        grade_point_value = float(grade)
        if grade_point_value in letter_grades:
            return letter_grades[grade_point_value]
        else:
            return "Invalid grade points."
    except ValueError:
        upper_grade = grade.upper()
        if upper_grade in grade_points:
            return grade_points[upper_grade]
        else:
            return "Invalid letter grade."

def main():
    while True:
        user_input = input("Enter a grade (or press Enter to exit): ")
        if user_input == "":
            break
        
        result = convert_grade(user_input)
        if isinstance(result, str) and result == "Invalid grade points.":
            print(f"Invalid input for grade points: {user_input}")
        elif isinstance(result, str) and result == "Invalid letter grade.":
            print(f"Invalid input for letter grade: {user_input}")
        else:
            print(f"Converted: {result}")

if __name__ == "__main__":
    main()
