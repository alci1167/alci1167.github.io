from typing import NamedTuple

#list of the 12 animals in the zodiac
zodiacs = ["OX","TIGER","RABBIT","DRAGON","SNAKE","HORSE","GOAT","MONKEY","ROOSTER","DOG","PIG","RAT",]

#NamedTuple to represent a relationship between two cows
class Relation(NamedTuple):
    name: str  #name of cow
    prev: bool  #whether the other cow's birth year is previous or next
    year: int  #index of the other cow's zodiac animal in the zodiacs list
    relative: str  #name of the other cow

#empty list to hold the relations between cows
relations = []

#read the number of relations from user and create a Relation object for each one
for _ in range(int(input())):
    rel = input().upper().split()
    #relation object using values from the input 
    relations.append(
        Relation(
            rel[0],  #name of the cow
            rel[3] == "PREVIOUS",  #whether the other cow's birth year is previous or next
            zodiacs.index(rel[4]),  #index of other cow's zodiac animal in the zodiacs list
            rel[7],  #name of the other cow
        )
    )

#dictionary to hold the birth years of each cow
birthYears = {"BESSIE": 0}     

#calc the birth year of each cow based on their relationships to other cows
for r in relations:
    #whether to add or subtract 1 from the other cow's birth year based on the prev value
    change = -1 if r.prev else 1
    #calc the birth year of the cow based on the other cow's birth year and the relative position of their zodiacs
    thisYear = birthYears[r.relative] + change
    while thisYear % len(zodiacs) != r.year:
        #if the birth year is not correct we can adjust it until it is
        thisYear += change
    #add the resulting birth year to the birth_years dict
    birthYears[r.name] = thisYear

#calc the age difference between Bessie and Elsie
dist = abs(birthYears["BESSIE"] - birthYears["ELSIE"])
print(dist)