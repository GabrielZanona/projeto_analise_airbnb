import pandas as pd

def limpar_dados(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)

    df = df.dropna(subset=['price', 'neighbourhood', 'reviews_per_month'])

    df['preco_por_quarto'] = df['price'] / df['minimum_nights']
    df['avaliacoes_por_ano'] = df['reviews_per_month'] * 12
    
    return df

if __name__ == "__main__":
    caminho_arquivo = '../data/nyc_airbnb_data.csv'

    df_limpo = limpar_dados(caminho_arquivo)

    df_limpo.to_csv('../output/dados_limpos.csv', index=False)

    print("Dados foram limpos e tambem salvos!")
