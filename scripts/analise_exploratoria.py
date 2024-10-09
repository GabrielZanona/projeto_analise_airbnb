import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plotar_distribuicao_preco(df):
    plt.figure(figsize=(10, 6))
    
    sns.boxplot(x='neighbourhood_group', y='price', data=df)
    
    plt.title('Distribuição de Preços por Bairro')

    plt.savefig('../output/figures/distribuicao_precos.png')

    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../output/dados_limpos.csv')
    
    plotar_distribuicao_preco(df)
