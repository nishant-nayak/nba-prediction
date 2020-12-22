import pandas as pd 
import numpy as np
import os
import csv
import math

path="D:\\Pranav\\Code\\IEEE\\nbastats"

def merge(season,month):
    results=pd.read_csv('D:\\Pranav\\Code\\IEEE\\bbref\\'+season+'\\'+month)
    stats=pd.read_csv('D:\\Pranav\\Code\\IEEE\\nbastats\\'+season+'\\'+month)

    conditions=[
        results['Team1Score']>results['Team2Score'],
        results['Team1Score']<results['Team2Score']
    ]

    choices=[1,0]

    results['Team1Win']=np.select(conditions,choices,1)

    df = results.merge(stats.add_prefix('Team1'), how='left', left_on=['Team1'], 
            right_on=['Team1TEAM']).drop(['Team1TEAM','Team1GP','Team1W','Team1L','Team1MIN'],
                axis=1).merge(stats.add_prefix('Team2'), how='left', left_on=['Team2'], 
                    right_on=['Team2TEAM']).drop(['Team2TEAM','Team2GP','Team2W','Team2L','Team2MIN'],axis=1)
    remove=[]
    col=df.head()
    for index,row in df.iterrows():
        for cell in col: 
            if isinstance(row[cell],float) and math.isnan(row[cell]) : remove.append(index)
    df=df.drop(df.index[remove])
    df.to_csv('D:\\Pranav\\Code\\IEEE\\combined\\'+season+'\\'+month,index=False,header=True)


for season in os.scandir(path):
    if season.is_dir() and season.name=='crossvalidation':
        for month in os.scandir(path+'\\'+season.name):
            merge(season.name,month.name)
            #print(season.name,month.name)
