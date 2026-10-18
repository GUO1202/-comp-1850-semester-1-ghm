# Worksheet 1.3: Task 3
filename = input("Enter the filename of the student data: ")

with open(filename, "r") as file:
    with open(filename + "_out.csv", "w") as output_file:
        next(file)  # 跳过表头

        for line in file:
            data = line.strip().split(",")
            student_id = data[0]

            grades = []
            for grade in data[1:]:
                if grade.strip() != "":
                    grades.append(float(grade))

            average_grade = sum(grades) / len(grades)

            if average_grade >= 70:
                classification = "1"
            elif average_grade >= 60:
                classification = "2:1"
            elif average_grade >= 50:
                classification = "2:2"
            elif average_grade >= 40:
                classification = "3"
            else:
                classification = "F"

            output_file.write(
                f"{student_id},{average_grade:.2f},{classification}\n"
            )
# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder