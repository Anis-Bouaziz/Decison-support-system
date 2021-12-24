from django.shortcuts import render
from django_plotly_dash import DjangoDash
import dash_table
import dash_bootstrap_components as dbc
from tool.methods.WSM import WSM
from tool.methods.Entropy import entropy
from tool.methods.promethee import promethee
from tool.methods.topsis import topsis
import pandas as pd
import plotly.express as px
from tool.methods.waspass import waspass
import dash_html_components as html
import dash_core_components as dcc


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
    app = DjangoDash('SimpleExample', external_stylesheets=[
                     dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.sample(frac=1).to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=20
    )
    return render(request, 'tool/index.html', {'topCountries': topCountries.to_dict(), 'topassets': topassets, 'topprofits': topprofits, 'topmarket': topmarket, 'topsales': topsales})


def charts(request):
    w = df[df['Company'].isin(WSM.wsm(df)[0]['Company'].head(3).values)]
    w2 = df[df['Company'].isin(entropy(df)[0]['Company'].head(3).values)]
    w3 = df[df['Company'].isin(topsis(df)[0]['Company'].head(3).values)]
    w4 = df[df['Company'].isin(waspass(df)[0]['Company'].head(3).values)]
    w5 = df[df['Company'].isin(promethee(df)[0]['Company'].head(3).values)]
    fig1 = px.bar(w, x='Company', y=df.columns,
                  barmode="group", template='plotly_dark')
    fig2 = px.bar(w2, x='Company', y=df.columns,
                  barmode="group", template='plotly_dark')
    fig3 = px.bar(w3, x='Company', y=df.columns,
                  barmode="group", template='plotly_dark')
    fig4 = px.bar(w4, x='Company', y=df.columns,
                  barmode="group", template='plotly_dark')
    fig5 = px.bar(w5, x='Company', y=df.columns,
                  barmode="group", template='plotly_dark')
    app = DjangoDash('bar1', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = html.Div(children=[
        html.H1(children='Weighted sum'),

        html.Div(children='''
        Company Ranking based on weighted sum.
    '''),

        dcc.Graph(
            id='example-graph',
            figure=fig1
        )
    ])
    app = DjangoDash('bar2', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = html.Div(children=[
        html.H1(children='Entropy'),

        html.Div(children='''
        Company Ranking based on Entropy.
    '''),

        dcc.Graph(
            id='example-graph',
            figure=fig2
        )
    ])
    app = DjangoDash('bar3', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = html.Div(children=[
        html.H1(children='Topsis'),

        html.Div(children='''
        Company Ranking based on Topsis.
    '''),

        dcc.Graph(
            id='example-graph',
            figure=fig3
        )
    ])
    app = DjangoDash('bar4', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = html.Div(children=[
        html.H1(children='waspass'),

        html.Div(children='''
        Company Ranking based on WASPASS.
    '''),

        dcc.Graph(
            id='example-graph',
            figure=fig4
        )
    ])
    app = DjangoDash('bar5', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = html.Div(children=[
        html.H1(children='Promethee I'),

        html.Div(children='''
        Company Ranking based on Promethee I.
    '''),

        dcc.Graph(
            id='example-graph',
            figure=fig5
        )
    ])
    return render(request, 'tool/charts.html')


def WS(request):
    w, wn = WSM.wsm(df)

    top1 = df[df['Company'] == w[:1]['Company'].values[0]]
    app = DjangoDash('wsm', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='wsm',
        columns=[{"name": i, "id": i} for i in w.columns],
        data=w.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    app = DjangoDash('wsm_norm', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='wsm_norm',
        columns=[{"name": i, "id": i} for i in wn.columns],
        data=wn.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    return render(request, 'tool/WSM.html', {'top1': top1})


def entropyMethod(request):
    w, wnorm, w_step3, e1, e2, e3 = entropy(df)

    top1 = df[df['Company'] == w[:1]['Company'].values[0]]
    app = DjangoDash('entropy', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='entropy',
        columns=[{"name": i, "id": i} for i in w.columns],
        data=w.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    ####################################################
    app = DjangoDash('wnorm', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='wnorm',
        columns=[{"name": i, "id": i} for i in wnorm.columns],
        data=wnorm.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    #############################
    ####################################################
    app = DjangoDash('step3', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='step3',
        columns=[{"name": i, "id": i} for i in w_step3.columns],
        data=w_step3.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    #############################
    ####################################################
    app = DjangoDash('e1', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='e1',
        columns=[{"name": i, "id": i} for i in e1.to_frame().T.columns],
        data=e1.to_frame().T.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        }
    )
    #############################
    ####################################################
    app = DjangoDash('e2', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='e2',
        columns=[{"name": i, "id": i} for i in e2.to_frame().T.columns],
        data=e2.to_frame().T.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        }
    )
    #############################
    ####################################################
    app = DjangoDash('e3', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='e3',
        columns=[{"name": i, "id": i} for i in e3.to_frame().T.columns],
        data=e3.to_frame().T.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        }
    )
    #############################
    return render(request, 'tool/entropy.html', {'top1': top1})


def topsisMethod(request):

    w, wnorm, step2, step3, step4 = topsis(df)
    top1 = df[df['Company'] == w[:1]['Company'].values[0]]
    app = DjangoDash('topsis', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='topsis',
        columns=[{"name": i, "id": i} for i in w.columns],
        data=w.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    ##########################################################
    app = DjangoDash('wnorm', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='wnorm',
        columns=[{"name": i, "id": i} for i in wnorm.columns],
        data=wnorm.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    #############################################################
    ##########################################################
    app = DjangoDash('vj', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='vj',
        columns=[{"name": i, "id": i} for i in step2.columns],
        data=step2.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=2
    )
    #############################################################
    ##########################################################
    app = DjangoDash('step3', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='s+',
        columns=[{"name": i, "id": i} for i in step3.columns],
        data=step3.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=5
    )
    #############################################################
    ##########################################################
    app = DjangoDash('step4', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='s-',
        columns=[{"name": i, "id": i} for i in step4.columns],
        data=step4.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=5
    )
    #############################################################
    return render(request, 'tool/topsis.html', {'top1': top1})


def waspassMethod(request):

    w, wnorm = waspass(df)
    top1 = df[df['Company'] == w[:1]['Company'].values[0]]
    app = DjangoDash('waspass', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='waspass',
        columns=[{"name": i, "id": i} for i in w.columns],
        data=w.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=20
    )
    ##########################################################
    app = DjangoDash('wnorm', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='wnorm',
        columns=[{"name": i, "id": i} for i in wnorm.columns],
        data=wnorm.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    #############################################################
    return render(request, 'tool/waspass.html', {'top1': top1})


def prometheeMethod(request):

    w, wnorm, phi = promethee(df)
    top1 = df[df['Company'] == w[:1]['Company'].values[0]]
    app = DjangoDash('promethee', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='promethee',
        columns=[{"name": i, "id": i} for i in w.columns],
        data=w.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=20
    )
    ##########################################################
    app = DjangoDash('wnorm', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='wnorm',
        columns=[{"name": i, "id": i} for i in wnorm.columns],
        data=wnorm.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    #############################################################
    ##########################################################
    app = DjangoDash('phi', external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dash_table.DataTable(
        id='phi',
        columns=[{"name": i, "id": i} for i in phi.columns],
        data=phi.to_dict('records'),

        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': '#4272d7',
            'color': 'white'
        },
        page_size=10
    )
    #############################################################
    return render(request, 'tool/promethee.html', {'top1': top1})
