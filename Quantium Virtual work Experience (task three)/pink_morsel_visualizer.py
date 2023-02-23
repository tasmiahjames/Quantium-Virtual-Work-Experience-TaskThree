import pandas
from dash import Dash, html, dcc

from plotly.express import line

DATA_PATH = "./data.csv"

# upload data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

#init dash
dash_app = Dash(__name__)

#Visualization
line_chart = line(data, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)

header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

dash_app.layout = html.Div(
    [
        header,
        visualization
    ]
)

if __name__ == '__main__':
    dash_app.run_server()
