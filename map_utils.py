import pandas as pd
import plotly.express as px

def create_map(supplier_data):
    df = pd.DataFrame(supplier_data)
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', color='risk_score',
                         hover_name='supplier_name', size='risk_score', 
                         projection="natural earth", title="Supplier Risk Map")

    fig.update_layout(showlegend=True)
    return fig

