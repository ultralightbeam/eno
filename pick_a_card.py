
import numpy as np

path_to_cards = 'cards/cards.csv'

if __name__ == '__main__':
  with open(path_to_cards) as f:
    data = [line.rstrip('\n') for line in f.readlines()[1:]]
  num_of_cards = len(data)
  idx = int(np.floor(np.random.rand() * num_of_cards))
  print('\nCard #' + str(idx) + '\n' + data[idx] + '\n')
