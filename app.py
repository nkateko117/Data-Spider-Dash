from dash import Dash, html, dcc
import dash
import plotly.express as px
import pandas as pd

px.defaults.template = "ggplot2"

bootstrap_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

app = Dash(__name__, pages_folder='components', use_pages=True, external_stylesheets=bootstrap_css)

app.layout = html.Div([
	html.Br(),
	html.P('Data Spider Genesis', className="text-dark text-center fw-bold fs-1"),
    html.Div(children=[
	    dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5")\
			  for page in dash.page_registry.values()]
	),
	dash.page_container
], className="col-8 mx-auto")

if __name__ == '__main__':
	app.run(debug=True)