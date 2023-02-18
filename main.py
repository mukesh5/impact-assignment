import sys

from attendance import Attendance

if __name__ == "__main__":
    max_miss_allowed = 4
    try:
        total_classes = int(sys.argv[1])
        print("Total Number of Classes are {}".format(total_classes))
    except IndexError:
        print("Please pass 'total classes' for the program to run")
    except Exception as e:
        print(e)
    else:
        attendance = Attendance(total_classes, max_miss_allowed)
