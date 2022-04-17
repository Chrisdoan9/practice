import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
#matplotlib parameters
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams.update({'font.size': 10})

def gamblers_ruin():
  gambling_money = 50
  gambling_goal = 100
  gambling_simulation = []

  while gambling_money in range(1,gambling_goal):
    bet_size = 1
    w_or_l = random.randrange(-1, 1, step = 2)
    gambling_money += bet_size * w_or_l
    gambling_simulation.append(gambling_money)
  return gambling_simulation

plt.plot(gamblers_ruin())
plt.yticks(np.arange(-20,100,5))
plt.axhline(y=0, color='r', linestyle='-')
plt.axhline(y=100, color='black', linestyle='-')
plt.xlabel('Number of bets')
plt.ylabel('Winnings')
plt.title('Gambling Simulation')
plt.show()