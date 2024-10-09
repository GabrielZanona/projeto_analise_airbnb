Projeto Análise Airbnb - Feito por Alexandre Augusto Longhini Junior e Gabriel Landarin Zanona

**Se quiser reinstalar o dataset do Kaggle:**
Baixe o dataset do Kaggle: https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data
Renomeie o arquivo baixado para nyc_airbnb_data.csv.
Coloque o arquivo na pasta data/.

1. Instalar dependências:
pip install pandas seaborn matplotlib plotly

2. Colocar o arquivo de dados na pasta certa
O dataset original do Airbnb foi baixado e trocamos o nome para nyc_airbnb_data.csv para manter um padrão de nome simples. Coloque o arquivo renomeado na pasta data/.

3. Rodar o script de limpeza de dados:
python scripts/limpeza_dados.py

Esse script gera um arquivo chamado dados_limpos.csv na pasta output/. Esse arquivo vai ser usado pelos outros scripts

4. Rodar o script de análise exploratória:
python scripts/analise_exploratoria.py
 O gráfico vai ser salvo em output/figures.

5. Rodar o script de visualização geoespacial:
python scripts/visualizacao_geoespacial.py
Abre um mapa em New york mostrando onde os imóveis estão localizados.

6. Rodar o script de histograma de preços:
python scripts/histograma_precos.py
O histograma vai ser salvo na pasta output/figures.