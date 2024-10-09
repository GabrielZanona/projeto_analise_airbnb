import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plotar_histograma(df):
    plt.figure(figsize=(10, 6))

    sns.histplot(df['price'], bins=50, kde=True)

    plt.title('Distribuição de Preços de Imóveis')
    plt.xlabel('Preço')
    plt.ylabel('Contagem')

    plt.savefig('../output/figures/histograma_precos.png')

    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../output/dados_limpos.csv')

    plotar_histograma(df)
