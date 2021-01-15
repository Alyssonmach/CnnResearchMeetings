import sys
sys.path.append('../implementations')

from implementations.players import players

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print('Total players: {}'.format(players))
