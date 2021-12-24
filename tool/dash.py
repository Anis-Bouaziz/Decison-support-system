from django_plotly_dash import DjangoDash
from dash import dash_table
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
from tool.methods.waspass import waspass
from tool.methods.WSM import WSM
from tool.methods.Entropy import entropy
from tool.methods.promethee import promethee
from tool.methods.topsis import topsis
##########################################################
df = pd.read_csv('tool/data/data.csv')
df.drop(['Global Rank', 'Continent', 'Latitude',
        'Longitude', 'Country'], axis=1, inplace=True)

wsm1, wsmn = WSM.wsm(df)
top_wsm = df[df['Company'] == wsm1[:1]['Company'].values[0]]
ent, ent_norm, ent_step3, e1, e2, e3 = entropy(df)
top_ent = df[df['Company'] == ent[:1]['Company'].values[0]]
top, top_norm, top_step2, top_step3, top_step4 = topsis(df)
top_topsis = df[df['Company'] == top[:1]['Company'].values[0]]
was, was_norm = waspass(df)
top_was = df[df['Company'] == was[:1]['Company'].values[0]]
prom, prom_norm, phi = promethee(df)
top_prom = df[df['Company'] == prom[:1]['Company'].values[0]]
######################################################
app1 = DjangoDash('SimpleExample', external_stylesheets=[
                     dbc.themes.BOOTSTRAP])
app1.layout = dash_table.DataTable(
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

##############################################################################################################
wsm_plot = df[df['Company'].isin(wsm1['Company'].head(3).values)]
entropy_plot = df[df['Company'].isin(ent['Company'].head(3).values)]
topsis_plot = df[df['Company'].isin(top['Company'].head(3).values)]
waspass_plot = df[df['Company'].isin(was['Company'].head(3).values)]
promethee_plot = df[df['Company'].isin(prom['Company'].head(3).values)]
fig1 = px.bar(wsm_plot, x='Company', y=df.columns,
                barmode="group", template='plotly_dark')
fig2 = px.bar(entropy_plot, x='Company', y=df.columns,
                barmode="group", template='plotly_dark')
fig3 = px.bar(topsis_plot, x='Company', y=df.columns,
                barmode="group", template='plotly_dark')
fig4 = px.bar(waspass_plot, x='Company', y=df.columns,
                barmode="group", template='plotly_dark')
fig5 = px.bar(promethee_plot, x='Company', y=df.columns,
                barmode="group", template='plotly_dark')
app2 = DjangoDash('bar1', external_stylesheets=[dbc.themes.BOOTSTRAP])
app2.layout = html.Div(children=[
    html.H1(children='Weighted sum'),

    html.Div(children='''
    Company Ranking based on weighted sum.
'''),

    dcc.Graph(
        id='example-graph',
        figure=fig1
    )
])
app3 = DjangoDash('bar2', external_stylesheets=[dbc.themes.BOOTSTRAP])
app3.layout = html.Div(children=[
    html.H1(children='Entropy'),

    html.Div(children='''
    Company Ranking based on Entropy.
'''),

    dcc.Graph(
        id='example-graph',
        figure=fig2
    )
])
app4 = DjangoDash('bar3', external_stylesheets=[dbc.themes.BOOTSTRAP])
app4.layout = html.Div(children=[
    html.H1(children='Topsis'),

    html.Div(children='''
    Company Ranking based on Topsis.
'''),

    dcc.Graph(
        id='example-graph',
        figure=fig3
    )
])
app5 = DjangoDash('bar4', external_stylesheets=[dbc.themes.BOOTSTRAP])
app5.layout = html.Div(children=[
    html.H1(children='waspass'),

    html.Div(children='''
    Company Ranking based on WASPASS.
'''),

    dcc.Graph(
        id='example-graph',
        figure=fig4
    )
])
app6 = DjangoDash('bar5', external_stylesheets=[dbc.themes.BOOTSTRAP])
app6.layout = html.Div(children=[
    html.H1(children='Promethee I'),

    html.Div(children='''
    Company Ranking based on Promethee I.
'''),

    dcc.Graph(
        id='example-graph',
        figure=fig5
    )
])
########################################################################

app7 = DjangoDash('wsm1', external_stylesheets=[dbc.themes.BOOTSTRAP])
app7.layout = dash_table.DataTable(
    id='wsm1',
    columns=[{"name": i, "id": i} for i in wsm1.columns],
    data=wsm1.to_dict('records'),

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
app8 = DjangoDash('wsm_norm', external_stylesheets=[dbc.themes.BOOTSTRAP])
app8.layout = dash_table.DataTable(
    id='wsm_norm',
    columns=[{"name": i, "id": i} for i in wsmn.columns],
    data=wsmn.to_dict('records'),

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
#########################################################################

app9 = DjangoDash('entropy', external_stylesheets=[dbc.themes.BOOTSTRAP])
app9.layout = dash_table.DataTable(
    id='entropy',
    columns=[{"name": i, "id": i} for i in ent.columns],
    data=ent.to_dict('records'),

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
app10 = DjangoDash('ent_norm', external_stylesheets=[dbc.themes.BOOTSTRAP])
app10.layout = dash_table.DataTable(
    id='ent_norm',
    columns=[{"name": i, "id": i} for i in ent_norm.columns],
    data=ent_norm.to_dict('records'),

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
app11 = DjangoDash('ent_step3', external_stylesheets=[dbc.themes.BOOTSTRAP])
app11.layout = dash_table.DataTable(
    id='ent_step3',
    columns=[{"name": i, "id": i} for i in ent_step3.columns],
    data=ent_step3.to_dict('records'),

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
app12 = DjangoDash('e1', external_stylesheets=[dbc.themes.BOOTSTRAP])
app12.layout = dash_table.DataTable(
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
app13 = DjangoDash('e2', external_stylesheets=[dbc.themes.BOOTSTRAP])
app13.layout = dash_table.DataTable(
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
app14 = DjangoDash('e3', external_stylesheets=[dbc.themes.BOOTSTRAP])
app14.layout = dash_table.DataTable(
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

app15 = DjangoDash('topsis', external_stylesheets=[dbc.themes.BOOTSTRAP])
app15.layout = dash_table.DataTable(
    id='topsis',
    columns=[{"name": i, "id": i} for i in top.columns],
    data=top.to_dict('records'),

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
app16 = DjangoDash('top_norm', external_stylesheets=[dbc.themes.BOOTSTRAP])
app16.layout = dash_table.DataTable(
    id='top_norm',
    columns=[{"name": i, "id": i} for i in top_norm.columns],
    data=top_norm.to_dict('records'),

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
app17 = DjangoDash('vj', external_stylesheets=[dbc.themes.BOOTSTRAP])
app17.layout = dash_table.DataTable(
    id='vj',
    columns=[{"name": i, "id": i} for i in top_step2.columns],
    data=top_step2.to_dict('records'),

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
app18 = DjangoDash('top_step3', external_stylesheets=[dbc.themes.BOOTSTRAP])
app18.layout = dash_table.DataTable(
    id='top_step3',
    columns=[{"name": i, "id": i} for i in top_step3.columns],
    data=top_step3.to_dict('records'),

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
app19 = DjangoDash('top_step4', external_stylesheets=[dbc.themes.BOOTSTRAP])
app19.layout = dash_table.DataTable(
    id='top_step4',
    columns=[{"name": i, "id": i} for i in top_step4.columns],
    data=top_step4.to_dict('records'),

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
app20 = DjangoDash('waspass', external_stylesheets=[dbc.themes.BOOTSTRAP])
app20.layout = dash_table.DataTable(
    id='waspass',
    columns=[{"name": i, "id": i} for i in was.columns],
    data=was.to_dict('records'),

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
app21 = DjangoDash('was_norm', external_stylesheets=[dbc.themes.BOOTSTRAP])
app21.layout = dash_table.DataTable(
    id='was_norm',
    columns=[{"name": i, "id": i} for i in was_norm.columns],
    data=was_norm.to_dict('records'),

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

app22 = DjangoDash('promethee', external_stylesheets=[dbc.themes.BOOTSTRAP])
app22.layout = dash_table.DataTable(
    id='promethee',
    columns=[{"name": i, "id": i} for i in prom.columns],
    data=prom.to_dict('records'),

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
app23 = DjangoDash('prom_norm', external_stylesheets=[dbc.themes.BOOTSTRAP])
app23.layout = dash_table.DataTable(
    id='prom_norm',
    columns=[{"name": i, "id": i} for i in prom_norm.columns],
    data=prom_norm.to_dict('records'),

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
app24 = DjangoDash('phi', external_stylesheets=[dbc.themes.BOOTSTRAP])
app24.layout = dash_table.DataTable(
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