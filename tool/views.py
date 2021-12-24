from django.shortcuts import render

import pandas as pd
from tool.dash import top_wsm ,top_topsis,top_ent,top_prom,top_was

df = pd.read_csv('tool/data/data.csv')




def index(request):
    topassets = df.groupby(by=['Company']).sum().sort_values(
    by='Assets ($billion)', ascending=False).head(10)['Assets ($billion)'].to_dict()
    topmarket = df.groupby(by=['Company']).sum().sort_values(
    by='Market Value ($billion)', ascending=False).head(10)['Market Value ($billion)'].to_dict()
    topprofits = df.groupby(by=['Company']).sum().sort_values(
    by='Profits ($billion)', ascending=False).head(10)['Profits ($billion)'].to_dict()
    topCountries = df.groupby(by=['Country']).sum().sort_values(
    by='Market Value ($billion)', ascending=False).head(10)['Market Value ($billion)']
    topsales = df.groupby(by=['Company']).sum().sort_values(
    by='Sales ($billion)', ascending=False).head(10)['Sales ($billion)'].to_dict()
    return render(request, 'tool/index.html', {'topCountries': topCountries.to_dict(), 'topassets': topassets, 'topprofits': topprofits, 'topmarket': topmarket, 'topsales': topsales})


def charts(request):

    return render(request, 'tool/charts.html')


def WS(request):
   
    return render(request, 'tool/WSM.html', {'top1': top_wsm})


def entropyMethod(request):
    
    return render(request, 'tool/entropy.html', {'top1': top_ent})


def topsisMethod(request):

    return render(request, 'tool/topsis.html', {'top1': top_topsis})


def waspassMethod(request):

    return render(request, 'tool/waspass.html', {'top1': top_was})


def prometheeMethod(request):
 
    return render(request, 'tool/promethee.html', {'top1': top_prom})
