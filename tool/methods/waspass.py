import numpy as np
def waspass(df):
    col=df['Company']
    df2=df.drop('Company',axis=1)
    df2=df2.set_index(col)
    m=np.max(df2,axis=0)
    df2=df2/m
    norm=df2.copy()
    s=np.sum(df2,axis=0)
    wsm=df2*0.25
    df2['wsm']=wsm.sum(axis=1)
    wpm=df2**0.25
    df2['wpm']=np.prod(wpm,axis=1)
    df2['Qi']=df2['wsm']*0.5+df2['wpm']*0.5
    return df2.reset_index().sort_values('Qi',ascending=False),norm