import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

main_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
    "Fruit": ["Apples", "Grapes", "Apples"],
    "Amount": [13, 56, 78],
    "City": ["Haldwani", "Nainital", "Nainital"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

main_app.layout = html.Div(children=[
    html.H1(children="First try at DASH"),
    html.Div(children="Pandas dataframe plotting using DASH"),
    dcc.Graph(id='example-graph', figure=fig)
])

if __name__ == '__main__':
    main_app.run_server(debug=True)

