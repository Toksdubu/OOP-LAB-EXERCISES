# Module 2 - File Handling
# Problem 2

import csv

with open('GWA.csv', 'r') as csvfile:
    GWAfile = csv.reader(csvfile)
    next(GWAfile)
    gwascore = 0
    highest_gwa_students = []
    for row in GWAfile:
        student_name = row[0]
        GWA = float(row[1])
        if gwascore == 0 or GWA < gwascore:
            gwascore = GWA
            highest_gwa_students = [student_name]
        elif GWA == gwascore:
            highest_gwa_students.append(student_name)
    if highest_gwa_students:
        for student in highest_gwa_students:
            print(student, gwascore)
