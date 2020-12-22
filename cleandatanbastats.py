import csv
import os

path="D:\\Pranav\\Code\\IEEE\\nbastats"

def modify(season,month):
    data=[]
    with open(path+'\\'+season+'\\'+month,'r') as source:
        reader=csv.reader(source)
        for row in reader: data.append(row[1:])
        
    with open(path+'\\'+season+'\\'+month,'w',newline='') as source:
        writer=csv.writer(source)
        writer.writerows(data)

for season in os.scandir(path) :
    if season.is_dir() and season.name=='crossvalidation':
        for month in os.scandir(path+'\\'+season.name):
            modify(season.name,month.name)