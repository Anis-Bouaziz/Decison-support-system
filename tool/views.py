from django.shortcuts import render
from django_plotly_dash import DjangoDash
from dash import dash_table
import dash_bootstrap_components as dbc
from tool.methods.WSM import WSM
from tool.methods.Entropy import entropy
from tool.methods.promethee import promethee
from tool.methods.topsis import topsis
import pandas as pd
import plotly.express as px
from tool.methods.waspass import waspass
from dash import html
from dash import dcc


df = pd.read_csv('tool/data/data.csv')
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
df.drop(['Global Rank', 'Continent', 'Latitude',
        'Longitude', 'Country'], axis=1, inplace=True)


def index(request):

    return render(request, 'tool/index.html', {'topCountries': topCountries.to_dict(), 'topassets': topassets, 'topprofits': topprofits, 'topmarket': topmarket, 'topsales': topsales})


def charts(request):

    return render(request, 'tool/charts.html')


def WS(request):
    w, wn = WSM.wsm(df)

    top1 = df[df['Company'] == w[:1]['Company'].values[0]]

    return render(request, 'tool/WSM.html', {'top1': top1})


def entropyMethod(request):
    w, wnorm, w_step3, e1, e2, e3 = entropy(df)

    top1 = df[df['Company'] == w[:1]['Company'].values[0]]

    return render(request, 'tool/entropy.html', {'top1': top1})


def topsisMethod(request):

    w, wnorm, step2, step3, step4 = topsis(df)
    top1 = df[df['Company'] == w[:1]['Company'].values[0]]

    return render(request, 'tool/topsis.html', {'top1': top1})


def waspassMethod(request):

    w, wnorm = waspass(df)
    top1 = df[df['Company'] == w[:1]['Company'].values[0]]

    return render(request, 'tool/waspass.html', {'top1': top1})


def prometheeMethod(request):
    w, wnorm, phi = promethee(df)
    top1 = df[df['Company'] == w[:1]['Company'].values[0]]
    #############################################################
    return render(request, 'tool/promethee.html', {'top1': top1})
