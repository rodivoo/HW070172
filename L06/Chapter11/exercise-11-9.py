# exercise-11-9.py
# A program to sort student grade information by GPA

from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s[1], s[2], s[3]), file = outfile)
    outfile.close()

def sortGPA(students):
    sortData = []
    for i in range(len(students)):
        x = (students[i].gpa(), students[i].getName(), students[i].getHours(), students[i].getQPoints())
        sortData.append(x)
        sortData.sort()
    return sortData

def main():
    print("This program sorts student grade information by GPA.")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    data = sortGPA(data)
    filename = input("Enter a name for the outputfile: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()