import pandas as pd

# Carregar os arquivos (corrigir os métodos de leitura e caminhos)
drivers = pd.read_csv("data/drivers.csv")
races = pd.read_csv("data/races.csv")
results = pd.read_csv("data/results.csv")

# Realizar um join (relacionando os dados)
merged_data = pd.merge(results, races, on="raceId", how="inner")
merged_data = pd.merge(merged_data, drivers, on="driverId", how="inner")

# Filtrar os anos de 2023 e 2024
filtered_data = merged_data[(merged_data['year'] == 2023) | (merged_data['year'] == 2024)]

# Selecionar apenas as colunas relevantes

# Criar a coluna 'target' com base na condição de points
filtered_data['target'] = (filtered_data['points'] > 10).astype(int)

# Salvar o resultado em um novo Excel
filtered_data.to_excel("dadosFiltrados.xlsx", index=False)

print("Consulta realizada e salva em 'dadosFiltrados_com_target.xlsx'")