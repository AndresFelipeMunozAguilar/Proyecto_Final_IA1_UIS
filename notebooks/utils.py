import itertools

def generate_experiments(lr=[0.01, 0.001, 0.0001], bs = [8, 16, 32]):
  # Generar todas las combinaciones posibles de hiperparámetros
  experiments = list(itertools.product(lr, bs))

  # Imprimir la lista de experimentos
  for exp in experiments:
      print(f'lr: {exp[0]}, bs: {exp[1]}')

generate_experiments()
