from sport import data
from user import User

a = 0
def what(user):
    for sport, stats in data.items():
        a = user.strength / stats[1]
        b = user.endurance / stats[2]
        c = user.speed / stats[3]
        d = user.flexibility / stats[4]
        e = user.coordination / stats[5]

        if round(((a + b + c + d + e) / 5) * 100) >= 85:
            a += 1
            print(stats[0], round(((a + b + c + d + e) / 5) * 100), '%')
        if a == 0:
            print("Вам нужно позаниматься")

pasha = User("Паша", 2, 3, 4, 3, 2)
what(pasha)
if a == 0:    print("Вам нужно позаниматься")
