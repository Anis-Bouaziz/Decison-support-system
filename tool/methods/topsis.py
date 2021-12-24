import numpy as np

def topsis(df):
    n=np.shape(df)[0]
    m=np.shape(df)[1]
    col=df['Company']
    df2=df.drop('Company',axis=1)
    df2=df2.set_index(col)
    s=df2.sum(axis=0)
    sp=np.sqrt(np.sum(df2*df2,axis=0))
    df2=df2/sp
    norm=df2.copy()
    s2=df2.sum(axis=0)
    max1=df2.max(axis=0)
    min1=df2.min(axis=0)
    vjp=max1.T.append(min1.T,ignore_index=True)
    vjm=max1.T.append(min1.T,ignore_index=True)
    vjp.name='VJ+'
    vjm.name='VJ-'
    df3=(df2-max1)**2
    sdf3=np.sqrt(np.sum(df3,axis=1))
    df4=(df2-min1)**2
    sdf4=np.sqrt(np.sum(df4,axis=1))
    df3['S_i+']=sdf3
    df4['S_i-']=sdf4
    s5=sdf3+sdf4
    df2['pi']=sdf4/s5
    return df2.reset_index().sort_values('pi',ascending=False),norm.reset_index(),vjp.to_frame().T.append(vjm.T).reset_index(),df3.reset_index(),df4.reset_index()