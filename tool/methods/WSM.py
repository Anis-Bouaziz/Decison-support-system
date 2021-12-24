import pandas as pd
import numpy as np
class WSM:
    def wsm(df):
        col=df['Company']
        df2=df.drop('Company',axis=1)
        df2=df2.set_index(col)
       
        for c in df2.columns:
            df2.loc[:,c]=(df2.loc[:,c]/sum(df2.loc[:,c]))
        norm=df2.copy()    
        df2.loc[:,'AGG']=df2.sum(axis=1)
        df2.loc[:,'AGG']=df2.loc[:,'AGG']/sum(df2['AGG'])
        
        df2=df2.sort_values('AGG',ascending=False)
        
        return df2.reset_index(),norm.reset_index()