import csv
import os

path="D:\\Pranav\\Code\\IEEE\\bbref"

def modify(season,month):
    data=[]
    with open(path+'\\'+season+'\\'+month,'r') as source:
        reader=csv.reader(source)
        for row in reader :
            if row[5]!='' and row[1]!='Date' :data.append(row[2:6])
            elif row[5]!='' : data.append(['Team1','Team1Score','Team2','Team2Score'])
    with open(path+'\\'+season+'\\'+month,'w',newline='') as source:                        
        writer=csv.writer(source)
        writer.writerows(data)

for season in os.scandir(path):
    if season.is_dir() and season.name=='crossvalidation':
        for month in os.scandir(path+'\\'+season.name) :
            print(season.name,month.name)
            modify(season.name,month.name)
        break