def monty_door_avoid_both(doors, alice_door, prize_door):
    candidates = list(set(doors) - {prize_door, alice_door})
    monty_door = random.choice(candidates)
    return monty_door

>>> result = [None]*N
>>> for i in range(N):
...     alice_door = random.choice(doors)
...     prize_door = random.choice(doors)
...     monty_door = monty_door_avoid_both(doors, alice_door, prize_door)
...     remaining_doors = set(doors) - {alice_door} - {monty_door}
...     result[i] = random.choice(list(remaining_doors)) == prize_door

>>> print "Probability of getting prize when Monty chooses the door avoiding both Alice and Prize?\n %f" % (float(sum(result))/N)
