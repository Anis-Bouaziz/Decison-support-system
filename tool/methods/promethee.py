import numpy as np
import pandas as pd
def scores(row,df,phi):
    df=row-df
    df[df<0]=0
    phi.loc[row.name]=df.sum(axis=1).T.values

def promethee(df):

    col=df['Company']
    df2=df.drop('Company',axis=1)
    df2=df2.set_index(col)
    max1=df2.max(axis=0)
    min1=df2.min(axis=0)
    normdf2=(df2-min1)/(max1-min1)
    phi=pd.DataFrame(columns=df2.index,index=df2.index.values)
    normdf2.apply(lambda row : scores(row,df2,phi),axis=1)
    df2['phi+']=phi.sum(axis=1)
    df2['-phi-']=phi.sum(axis=0)*-1
    return df2.reset_index().sort_values(['phi+','-phi-'],ascending=False),normdf2,phi.head(10)