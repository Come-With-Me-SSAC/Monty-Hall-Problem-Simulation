def monty_door_avoid_alice(doors, alice_door, prize_door):
    candidates = list(set(doors) - {alice_door})
    monty_door = random.choice(candidates)
    return monty_door

>>> result = [None]*N
>>> for i in range(N):
...     alice_door = random.choice(doors)
...     prize_door = random.choice(doors)
...     monty_door = monty_door_avoid_alice(doors, alice_door, prize_door)
...     while monty_door == prize_door:
...         alice_door = random.choice(doors)
...         prize_door = random.choice(doors)
...         monty_door = monty_door_avoid_alice(doors, alice_door, prize_door)
...     
...     remaining_doors = set(doors) - {alice_door} - {monty_door}
...     result[i] = random.choice(list(remaining_doors)) == prize_door

