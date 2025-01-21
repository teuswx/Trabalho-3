import pandas as pd

drivers = pd.read_csv("data/drivers.csv")
races = pd.read_csv("data/races.csv")
results = pd.read_csv("data/results.csv")

merged_data = pd.merge(results, races, on="raceId", how="inner")
merged_data = pd.merge(merged_data, drivers, on="driverId", how="inner")

filtered_data = merged_data[(merged_data['year'] == 2023) | (merged_data['year'] == 2024)]

filtered_data['target'] = (filtered_data['points'] > 10).astype(int)

filtered_data.to_excel("dadosFiltrados.xlsx", index=False)

print("Consulta realizada e salva em 'dadosFiltrados_com_target.xlsx'")
