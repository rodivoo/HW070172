# exercise-11-2.py
# A program to sort student information

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
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file = outfile)
    outfile.close()

def main():
    print("This program sorts student grade information.")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)

    while True:
        sort = input("Type GPA, name, or credits: ")
        if sort == "GPA":
            data.sort(key=Student.gpa)
            break
        elif sort == "name":
            data.sort(key=Student.getName)
            break
        elif sort == "credits":
            data.sort(key=Student.getQPoints)
            break
        else:
            print("Try it again.")

    filename = input("Enter a name for the outputfile: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()