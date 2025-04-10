import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px
from risk_assessment import get_news_risk

# Load supplier data
df = pd.read_csv('data/suppliers.csv')

# Add risk score based on country
df['risk_score'] = df['country'].apply(get_news_risk)

# Create map
fig = px.scatter_geo(df,
    lat='latitude',
    lon='longitude',
    text='name',
    color='risk_score',  # Color by risk score
    color_continuous_scale='reds',  # Redder = higher risk
    title='Global Supplier Risk Dashboard'
)

# Dash App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Global Supplier Risk Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)

