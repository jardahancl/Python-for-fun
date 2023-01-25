import collections
# A = X = 1 (Rock) -> lose
# B = Y = 2 (Paper) -> draw
# C = Z = 3 (Scissors) -> win

data = open('resources/02.txt').read()
frequency = collections.Counter(data.splitlines())
my_hand = collections.Counter(map(lambda x: x[-1], data.splitlines()))

winner_points = 6 * sum([frequency['C X'], frequency['A Y'], frequency['B Z']])
draw_points = 3 * sum([frequency['A X'], frequency['B Y'], frequency['C Z']])
hand_points = my_hand['X'] + 2 * my_hand['Y'] + 3 * my_hand['Z']
total_points_1 = winner_points + draw_points + hand_points

game_points = 3 * my_hand['Y'] + 6 * my_hand['Z']
rock_points = 1 * sum([frequency['A Y'], frequency['B X'], frequency['C Z']])
paper_points = 2 * sum([frequency['A Z'], frequency['B Y'], frequency['C X']])
scissors_points = 3 * sum([frequency['A X'], frequency['B Z'], frequency['C Y']])
total_points_2 = game_points + rock_points + paper_points + scissors_points

print(f'02a - total points {total_points_1}.')
print(f'02b - total points {total_points_2}.')
# time 1h





