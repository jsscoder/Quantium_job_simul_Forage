import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# ---------------- DATA ----------------
# Replace this with your generated CSV if you already have one
dates = pd.date_range("2021-01-01", "2021-01-31")

data = []
regions = ["north", "east", "south", "west"]

for region in regions:
    base = {"north": 120, "east": 140, "south": 110, "west": 130}[region]
    for i, d in enumerate(dates):
        sales = base + i * 3
        if d >= pd.Timestamp("2021-01-15"):
            sales += 30
        data.append([d, sales, region])

df = pd.DataFrame(data, columns=["date", "sales", "region"])

# ---------------- APP ----------------
app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        html.H1("Soul Foods – Pink Morsel Sales Dashboard", className="title"),

        html.Div(
            className="controls",
            children=[
                html.Label("Select Region", className="label"),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    className="radio"
                ),
            ],
        ),

        dcc.Graph(id="sales-chart")
    ],
)

# ---------------- CALLBACK ----------------
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    if region == "all":
        filtered = df.groupby("date", as_index=False)["sales"].sum()
    else:
        filtered = df[df["region"] == region]

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title="Daily Sales Trend – January 2021",
        labels={"date": "Date", "sales": "Sales ($)"}
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase (Jan 15)",
        annotation_position="top left"
    )

    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        font=dict(size=14)
    )

    return fig


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run_server(debug=True)
