import argparse
import sys

def parse_args():
  usage = "[-h] [-k KILOMETERS] [-f FILE]"
  description = """Program to cover k km with the minimum posible antennas of a set of n antennas.
The antennas must be provided on a txt file with the next fromat:
  antena_number,center,radius
If the k km are covered, it prints de selected antena number's. 
Otherwise it prints an empty list
"""

  parser = argparse.ArgumentParser("./main.py",
    usage='%(prog)s {}\n{}'.format(usage, description))

  group = parser.add_mutually_exclusive_group()
  group.add_argument("-km", "--kilometers", default=500,
    type=int, const=500, nargs='?',
    help="kilometers to be covered. Default value: 500")
  group.add_argument("-f", "--file", default='contratos.txt',
    type=str, const='contratos.txt', nargs='?',
    help="file with antena's data. Default value: contratos.txt")

  return parser.parse_args()

def open_file(fileName, mode="r"):
  try:
    file = open("{}".format(fileName), mode)
  except IOError:
    print("I/O Error")
    sys.exit(1)
  except FileNotFoundError:
    print("File not found Error", end='')
  return file