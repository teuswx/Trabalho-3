import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Carregar os dados diretamente do arquivo Excel
data = pd.read_excel("dadosFiltrados.xlsx")

data.replace('\\N', pd.NA, inplace=True)

# Imputar valores ausentes

# Filtrar os dados de 2023 com pontuação acima de 10
data_2023 = data[(data['year'] == 2023) & (data['points'] > 10)]
data_2023.fillna(data_2023.mean(), inplace=True)

# Selecionar as colunas relevantes para treinamento
X_train = data_2023[['points', 'position', 'grid', 'fastestLapSpeed', 'constructorId', 'statusId']]  # Colunas de entrada
y_train = data_2023['target']  # Coluna alvo (defina o alvo, como 'Target' com base em sua análise)

# Dividir os dados de 2024
data_2024 = data[data['year'] == 2024]  # Filtrar corretamente os dados de 2024
data_2024.fillna(data_2024.mean(), inplace=True)
X_test = data_2024[['points', 'position', 'grid', 'fastestLapSpeed', 'constructorId', 'statusId']]  # Colunas de entrada (corrigido para 'points')
y_test = data_2024['target']  # Coluna alvo

# Criar e treinar a árvore de decisão
clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_train, y_train)

# Fazer previsões e avaliar
y_pred = clf.predict(X_test)
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")

# Visualizar a árvore de decisão
plt.figure(figsize=(16, 10))
plot_tree(clf, feature_names=X_train.columns, class_names=['Classe1', 'Classe2'], filled=True)
plt.show()

# Exibir os pilotos com maior chance de ganhar em 2025
# Para isso, podemos filtrar os pilotos com a maior pontuação prevista
predicted_data = data_2024.copy()
predicted_data['Predicted'] = clf.predict(X_test)

# Exibir os pilotos mais promissores para 2025
top_drivers = predicted_data[predicted_data['Predicted'] == 1]  # Altere '1' para a classe com maior chance de ganhar
print(top_drivers[['driverId', 'forename', 'name', 'points']])  # Corrigido para 'driverId', 'forename' e 'name'
