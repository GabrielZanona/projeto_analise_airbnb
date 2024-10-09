import plotly.express as px
import pandas as pd

def plotar_mapa(df):
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="price",
                            size="price", hover_name="neighbourhood", hover_data=["price"],
                            color_continuous_scale=px.colors.cyclical.IceFire, zoom=10, height=600)
    
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    
    fig.show()

if __name__ == "__main__":
    df = pd.read_csv('../output/dados_limpos.csv')
    
    plotar_mapa(df)
