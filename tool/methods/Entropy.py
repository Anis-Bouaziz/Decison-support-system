import pandas as pd
import numpy as np


def normalize(df):
    col=df['Company']
    df2=df.drop('Company',axis=1)
    df2=df2.set_index(col)
    for c in df2.columns:
        df2[c]=df2[c]/df2[c].sum()
    return df2

def entropy(df):
    n=np.shape(df)[0]
    m=np.shape(df)[1]
    k=1/np.log(m)
    df2=normalize(df)
    dfnorm=df2.copy()
    df3=df2*np.log(df2)
    df_step3=df3.copy()
    s1=np.sum(df3,axis=0)
    e1=k*s1
    e2=1-e1
    e3=e2/sum(e2)
   
    col=df['Company']
    df2=df.drop('Company',axis=1)
    df2=df2.set_index(col)
    df3['score']=df2.dot(e3.T)
    return df3.reset_index().sort_values('score',ascending=False),dfnorm.reset_index(),df_step3.reset_index(),e1,e2,e3

    
