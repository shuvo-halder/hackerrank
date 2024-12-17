import os
import sys


sword_damage = 10
player_health = 100
health_after_attack = player_health - sword_damage

print(f" sams health is: {player_health}")
print(f"sword damage {sword_damage}")
print(f"player health after sword damage : {health_after_attack}")



# list
listName = ["apple", "banana", "Number"]
print(type(listName))
print(listName[2])

secondList = ['name','email','number','sam']
print(type(secondList))
print(secondList[3])

# tupple
tuppleNameList = ('tupple1','tupple2','tupple3')
print(type(tuppleNameList)) 
print(tuppleNameList[1])