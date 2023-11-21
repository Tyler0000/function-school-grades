def calculate_subject_results(subject_name, num_tests, grade_c, grade_b, grade_a):
    test_scores = []
    for i in range(num_tests):
        score = float(input(f"Enter {subject_name} test {i + 1} score: "))
        test_scores.append(score)

    average_marks = sum(test_scores) / num_tests

    if average_marks >= grade_a:
        final_grade = 'A'
    elif average_marks >= grade_b:
        final_grade = 'B'
    elif average_marks >= grade_c:
        final_grade = 'C'
    else:
        final_grade = 'Below C'

    total_marks = sum(test_scores)

    print(f"{subject_name}:")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Final Grade: {final_grade}")
    print(f"Total Marks: {total_marks}/{num_tests * 100}\n")

calculate_subject_results("English", 2, 64, 84, 104)

calculate_subject_results("Maths", 3, 56, 64, 78)

calculate_subject_results("Science", 3, 96, 113, 128)


