from operator import itemgetter

def open_file(fileName, mode="r"):
  try:
    file = open("{}".format(fileName), mode)
  except IOError:
    print("I/O Error")
    sys.exit(1)
  except FileNotFoundError:
    print("File not found Error", end='')
  return file



def read_file(file):

  lista_antenas = []

  while True:
    line = file.readline()
    if not line:
      print()
      break
    else:
      elemento = parse_line(line.strip('\n'))
      lista_antenas.append(elemento)
  lista_antenas.sort(key=itemgetter(0), reverse=True)
  print('lista de antenas')
  print(lista_antenas)
  print('---------------')
  return lista_antenas


def parse_line(line):
  splitted_line = line.split(',')
  ic = int(splitted_line[1]) - int(splitted_line[2])
  if ic < 0:
    ic = 0
  fc = int(splitted_line[1]) + int(splitted_line[2])
  antena_id = int(splitted_line[0])

  return (fc, [antena_id, ic])



def resolve_problem(lista_antenas, km):
  lista_antenas.append((-1, [-1, -1]))
  actual = 0
  seleccionados = []

  while km != 0 and actual != len(lista_antenas):

    candidatos = []

    while lista_antenas[actual][0] >= km:
      candidatos.append(lista_antenas[actual])
      actual += 1
    if len(candidatos) == 0:
      lista_antenas =[]
    min_ic = km
    seleccionado = None
    for candidato in candidatos: 
      if(candidato[1][1] <= min_ic):
        min_ic = candidato[1][1]
        seleccionado = candidato[1][0]
    km = min_ic
    seleccionados.append(seleccionado)

  if km > 0:
    seleccionados = [] 
  return seleccionados

    
def run():
  file = open_file('contratos.txt')
  lista_antenas = read_file(file)
  print(resolve_problem(lista_antenas, 5000))



if __name__ == "__main__":
    run()