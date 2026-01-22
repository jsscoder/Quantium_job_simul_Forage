import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# --- sample data (replace with YOUR generated data if already saved) ---
dates = pd.date_range("2021-01-01", "2021-01-31")
sales = [
    120, 130, 125, 140, 135, 150, 145,
    155, 160, 158, 162, 165, 170, 168,
    200, 210, 205, 215, 220, 225, 230,
    235, 240, 238, 245, 250, 255, 260,
    265, 270
]

df = pd.DataFrame({
    "date": dates,
    "sales": sales
}).sort_values("date")

# --- plot ---
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Soul Foods – Daily Sales Trend (Jan 2021)",
    labels={
        "date": "Date",
        "sales": "Total Sales ($)"
    }
)

# vertical line for price increase
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase (Jan 15)",
    annotation_position="top left"
)

# --- Dash app ---
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Soul Foods Sales Visualiser"),
        dcc.Graph(figure=fig)
    ],
    style={"width": "80%", "margin": "auto"}
)

if __name__ == "__main__":
    app.run_server(debug=True)
