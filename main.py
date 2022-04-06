from operator import itemgetter
import utils


def read_file(file):

  antenna_list = []
  line = ' '
  while line != '':
    line = file.readline()
    if not line:
      print()
      break
    else:
      antenna = parse_line(line.strip('\n'))
      antenna_list.append(antenna)
  antenna_list.sort(key=itemgetter(0), reverse=True)
  return antenna_list


def parse_line(line):
  splitted_line = line.split(',')
  ic = int(splitted_line[1]) - int(splitted_line[2])
  if ic < 0:
    ic = 0
  fc = int(splitted_line[1]) + int(splitted_line[2])
  antena_id = int(splitted_line[0])

  return (fc, [antena_id, ic])


def resolve_problem(antenna_list, km):
  antenna_list.append((-1, [-1, -1]))
  actual = 0
  selected_antennas = []

  while km != 0 and actual != len(antenna_list):

    candidates = []

    try: 
      while antenna_list[actual][0] >= km:
        candidates.append(antenna_list[actual])
        actual += 1
    except IndexError:
      actual = len(antenna_list)

    if len(candidates) == 0:
      antenna_list =[]

    min_ic = km
    selected = None
    for candidate in candidates: 
      if(candidate[1][1] < min_ic):
        min_ic = candidate[1][1]
        selected = candidate[1][0]
    km = min_ic
    selected_antennas.append(selected)

  if km > 0:
    selected_antennas = [] 
  return selected_antennas

    
def run():
  args = utils.parse_args()
  kilometers = int(args.kilometers)
  print(kilometers)
  if (kilometers > 0):

    file = utils.open_file(args.file)
    antenna_list = read_file(file)
    print('The Answer is:')
    print(resolve_problem(antenna_list, int(args.kilometers)))
    file.close()
  else: 
    print('Kilometers must be greater than 0')

if __name__ == "__main__":
    run()