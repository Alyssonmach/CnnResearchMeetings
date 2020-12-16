import sys
sys.path.append('../implementations/')

from implementations.players import players

print(players)
print(players[0])
print(players[-1])
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[4:])
print(players[-3:])
print(players[:-3])