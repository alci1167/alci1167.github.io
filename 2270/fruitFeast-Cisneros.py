from collections import deque

with open("feast.in") as read:
    max_fullness, orange, lemon = map(int, read.readline().split())

#set containing all possible fullness levels that can be achieved
poss_fullness = {(0, False)}
#queue for BFS traversal of all possible fullness levels
to_process = deque([(0, False)])

#BFS traversal of all possible fullness levels
while to_process:
    fullness, drank_water = to_process.pop()

    #if the previous state didn't drink water, we can drink water now
    if not drank_water:
        #calc the fullness level after drinking water
        water = (fullness // 2, True)
        #if the new state isn't already in the set of possible fullness levels, add to the queue and set
        if water not in poss_fullness:
            to_process.appendleft(water)
            poss_fullness.add(water)

    #check all possible fruits that can be eaten
    for fruit in (orange, lemon):
        #calc the fullness level after eating fruit
        after = fullness + fruit
        to_add = (after, drank_water)
        #if the new state is not already in the set of possible fullness levels and the fullness level is within bounds, add it to the queue and set
        if after <= max_fullness and to_add not in poss_fullness:
            to_process.appendleft(to_add)
            poss_fullness.add(to_add)

#find the maximum fullness level from all possible states
best = max([n[0] for n in poss_fullness])
print(best, file=open("feast.out", "w"))
