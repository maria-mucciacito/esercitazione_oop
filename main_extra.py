import csv
from tkinter import N
def is_integer(num):
    try:
        num = int(num)
        print(True)
        return True
    except:
        print(False)
        return False


def i(num):
    try:
        int(num)
    except:
        float(num)
    x = isinstance(num, int)
    print(x)


def read_from_csv():
    input_file = csv.DictReader(open("items.csv"))
    for item in input_file:
        is_integer(item['quantity'])
        print(item)
           
read_from_csv()





