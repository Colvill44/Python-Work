'''
materialFarming.py : Collect data on overall farmed materials.

created by : Will Colvill

3/6/2020
'''

def getDate():
    date = input("What is the current date? ")
    time = input("How long did you spend farming materials? ")
    return date, time

def getMaterialsUsed():
    herbs = input("Did you gather any herbs? (1 for yes or 2 for no) ")
    ore = input("Did you collect any ore? (1 for yes or 2 for no) ")
    enchants = input("Were there any enchanting materials? (1 for yes or 2 for no) ")
    other = input("Were there any other materials gathered? (1 for yes or 2 for no) ")
    return herbs, ore, enchants, other

def enterMaterials(herbs, ore, enchants, other):
    if
