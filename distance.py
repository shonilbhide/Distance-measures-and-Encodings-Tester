import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from abydos import phonetic
from abydos import distance

dist=[distance.dist_cosine,distance.dist_dice,distance.dist_editex,distance.dist_euclidean,distance.dist_hamming,distance.dist_jaccard,distance.dist_jaro_winkler,distance.dist_levenshtein,distance.dist_manhattan,distance.dist_overlap,distance.dist_prefix]
phone=[str,phonetic.caverphone,phonetic.dolby,phonetic.eudex,phonetic.fuzzy_soundex,phonetic.nysiis,phonetic.phonem,phonetic.phonex,phonetic.phonix,phonetic.refined_soundex,phonetic.soundex,phonetic.statistics_canada,phonetic.metaphone]
dist_label=[]
phone_label=[]
for i in dist:
    dist_label.append({'label': str(i).split()[1], 'value': dist.index(i)})
for i in phone:
    phone_label.append({'label': str(i).split()[1], 'value': phone.index(i)})
#dist_label=[{'label':"str",'value':1}]
#phone_label=[{'label':"str",'value':1}]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        dcc.Dropdown(
            id='type_of_ip',
            options=[
                {'label': 'single word', 'value': 's'},
                {'label': 'double word', 'value': 'd'},
            ],
            value='s'
        ),
    ]),
    html.Div(children=[
        html.Div(children=[
            dcc.Dropdown(
                id='phone_type',
                options=phone_label,
                value=0
            )]),
        html.Div([
            dcc.Textarea(
                id='sip1',
                value='add input',
                style={'width': '40%', 'height': 50},
            ),
            dcc.Textarea(
                id='sip2',
                value='add input',
                style={'width': '40%', 'height': 50},
            ),
        ]),
        html.Div([
            html.Button('Submit', id='ssubmit', n_clicks=0),
        ]),
        html.Div([
            dcc.Textarea(
                id='sop1',
                value='',
                style={'width': '40%', 'height': 50},
            ),
            dcc.Textarea(
                id='sop2',
                value='',
                style={'width': '40%', 'height': 50},
            ),
        ]),
        html.Div(children=[
            dcc.Dropdown(
                id='dist_type',
                options=dist_label,
                value=0
        )]),
        html.Div([
            html.Button('Submit', id='ssubmit2', n_clicks=0),
            dcc.Textarea(
                id='sop3',
                value='',
                style={'width': '100%', 'height': 20},
            ),
        ]),


        ]),


    ])





@app.callback(
    Output('sop1', 'value'),
    [Input('sip1', 'value'),
    Input('ssubmit','n_clicks'),
    Input('phone_type','value')]
)
def update_sop1(inp,n,k):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'ssubmit' in changed_id:
        a=phone[k](inp)
        return str(a)
    else:
        return ""

@app.callback(
    Output('sop2', 'value'),
    [Input('sip2', 'value'),
    Input('ssubmit','n_clicks'),
    Input('phone_type','value')]
)
def update_sop2(inp,n,k):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'ssubmit' in changed_id:
        a=phone[k](inp)
        return str(a)
    else:
        return ""

@app.callback(
    Output('sop3', 'value'),
    [Input('sip1', 'value'),
    Input('sip2', 'value'),
    Input('ssubmit2','n_clicks'),
    Input('phone_type','value'),
    Input('dist_type','value'),
    ]
)
def update_sop3(inp1,inp2,n,p,k):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'ssubmit2' in changed_id:
        if (str(inp1) != "") or (str(inp2)  != "") or (str(inp1)  != "add input") or (str(inp2)  != "add input"):
            a=dist[k](str(phone[p](inp1)),str(phone[p](inp2)))
            return str(a)
    else:
        return ""

           
            



if __name__ == '__main__':
    app.run_server(debug=True)

