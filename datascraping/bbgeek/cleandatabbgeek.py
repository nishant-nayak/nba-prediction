import os
import csv

path = '\\datasets\\bbgeek'

def modify(season,game):
    data=[]
    with open(path+'\\'+season+'\\'+game,'r') as source:
        reader=csv.reader(source)
        for row in reader :
            newrow=[]
            


for season in os.scandir(path):
    if season.is_dir() :
        for game in os.scandir(path+'\\'+season.name):
            modify(season.name,game.name)