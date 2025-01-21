# Trabalho IA: Comparação entre Algoritmos de Busca Informada

## Objetivo 🎯 

O trabalho tem como objetivo explorar e implementar árvores de decisão em diferentes contextos, com foco em dois aspectos principais:  

### 1. Desafio Interativo - Árvore de Decisão com 10 Perguntas  
- Desenvolver uma árvore de decisão interativa capaz de ajudar os usuários a escolher entre hobbies ou carreiras com base em suas preferências e habilidades.  
- Estruturar a lógica de perguntas e respostas para fornecer recomendações personalizadas de forma clara e intuitiva.  
- Estimular a reflexão pessoal ao explorar aspectos como trabalho em equipe, habilidades técnicas, criatividade e comunicação.  

### 2. Exploração de Datasets Reais  
- Aplicar árvores de decisão para resolver problemas práticos utilizando datasets disponíveis no Kaggle e no UCI Machine Learning Repository.  
- Analisar um dataset real, desde o pré-processamento até a criação de um modelo de árvore de decisão para classificação ou previsão.  
- Avaliar o desempenho do modelo com métricas apropriadas, como acurácia, e apresentar os resultados de forma visual e documentada.  

### Dataset Escolhido para a parte 2 do trabalho 📈

Os dados escolhidos são referentes ao Campeonato Mundial de Fórmula 1, abrangendo o período de 1950 a 2024. O dataset foi obtido no Kaggle através do seguinte link: [Fórmula 1 World Championship Dataset (1950-2020)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020). Os dados foram filtrados em um arquivo para facilitar a análise.

O objetivo é analisar os dados de 2023 e 2024, utilizando os dados de 2023 para treinamento e os de 2024 para teste, também prever quais pilotos mantiveram um desempenho consistente em 2024, com base no número de voltas realizadas e na posição inicial no grid.  

#### Dados Selecionados  

Os dados utilizados para o treinamento incluem as seguintes colunas:  
- **`raceId`**: Identificador da corrida.  
- **`driverId`**: Identificador do piloto.  
- **`laps`**: Número de voltas completadas pelo piloto.  
- **`grid`**: Posição inicial no grid de largada.  

A variável alvo (**`target`**) é uma coluna no arquivo `dadosFiltrados.xlsx`, que classifica os pilotos com base em sua pontuação na corrida:  
- **1**: Pilotos com pontuação acima de 10.  
- **0**: Pilotos com pontuação abaixo de 10.  

Este critério foi estabelecido para identificar pilotos que apresentaram uma pontuação consistente nas corridas, permitindo avaliar sua performance ao longo do campeonato. Como a coluna **`target`** utiliza como parâmetro a pontuação de cada piloto, métricas muito relacioandas a pontuação são descartadas.


## Descrição dos Algoritmos Implementados 📜  

- **Arquivo `arvore.py`**:  
  Implementa uma árvore de decisão iterativa com diversas perguntas para auxiliar o usuário na escolha de hobbies ou carreiras com base em suas preferências e respostas. O código é estruturado para fornecer sugestões personalizadas, criando uma interação simples.
- **Notebook `ML.ipynb`**:  
  Contém o código desenvolvido utilizando a biblioteca `scikit-learn` para análise e previsão com base no dataset selecionado. O notebook realiza o pré-processamento dos dados, treina uma árvore de decisão para identificar padrões e faz previsões sobre o desempenho dos pilotos no dataset de Fórmula 1.

## Estrutura do Projeto 🏗️

- **Linguagem:** Python.
- **Bibliotecas Utilizadas:**
  - **pandas**: Para manipulação e análise de dados, incluindo carregamento e pré-processamento do dataset.
  - **scikit-learn**:
    - `DecisionTreeClassifier`: Para criação e treinamento da árvore de decisão.
    - `train_test_split`: Para dividir os dados em conjuntos de treino e teste.
    - `accuracy_score`: Para calcular a acurácia do modelo.
    - `plot_tree`: Para visualização gráfica da árvore de decisão.
  - **matplotlib.pyplot**: Para criar gráficos e visualizar a árvore de decisão.


## Resultados das medicões de desempenho ⏱️
Com o modelo desenvolvido, foi possível analisar os dados do dataset e visualizar a árvore de decisão gerada durante o treinamento. A árvore de decisão foi construída para classificar os pilotos com base nos atributos selecionados, e sua estrutura fornece uma visão clara das regras usadas pelo modelo para fazer as previsões.  

Abaixo está a visualização da árvore de decisão treinada:

![Árvore de Decisão](https://github.com/user-attachments/assets/c73e75f1-aa2e-4b4e-9434-749bd2bc3342)

Foi possível obter uma acurácia de **0.88**, o que significa um valor **muito bom** de acerto para previsão.

## Pilotos com Maior Chance de Obter Pontos em 2025

Com base nas previsões realizadas, foi possível obter as probabilidades médias de cada piloto para conseguir pontos acima de 10. Abaixo estão os **10 pilotos com maior chance** de alcançar esse feito, classificados em ordem decrescente de probabilidade:

| Posição | Driver ID | Forename    | Surname    | Probabilidade de Pontos |
|---------|-----------|-------------|------------|-------------------------|
| 1       | 830       | Max         | Verstappen | 1.0000                  |
| 2       | 846       | Lando       | Norris     | 0.8333                  |
| 3       | 844       | Charles     | Leclerc    | 0.7500                  |
| 4       | 832       | Carlos      | Sainz      | 0.7273                  |
| 5       | 815       | Sergio      | Pérez      | 0.6667                  |
| 6       | 857       | Oscar       | Piastri    | 0.6667                  |
| 7       | 847       | George      | Russell    | 0.5833                  |
| 8       | 1         | Lewis       | Hamilton   | 0.5000                  |
| 9       | 4         | Fernando    | Alonso     | 0.3333                  |
| 10      | 807       | Nico        | Hülkenberg | 0.0833                  |

### Análise dos Resultados

- **Max Verstappen** lidera com uma probabilidade de **1.0000**, indicando que ele é o piloto com a maior chance de conseguir pontos em 2025.
- **Lando Norris** e **Charles Leclerc** também têm chances muito altas, com probabilidades de **0.8333** e **0.7500**, respectivamente.
- Outros pilotos como **Carlos Sainz** e **Sergio Pérez** também apresentam boas chances, com probabilidades superiores a 0.66.
- **Lewis Hamilton** e **Fernando Alonso** estão em posições mais baixas, mas ainda têm chances razoáveis de alcançar pontos.
- **Nico Hülkenberg** apresenta a menor probabilidade entre os 10 primeiros, com **0.0833**, sugerindo uma chance consideravelmente baixa.

Esses resultados são baseados em um modelo de previsão que utiliza dados históricos para estimar as probabilidades de cada piloto alcançar mais de 10 pontos ao longo da temporada de 2025.



## Considerações Finais 📝

O trabalho foi desenvolvido com o objetivo de explorar a aplicação de árvores de decisão em diferentes contextos, com ênfase na previsão de desempenho de pilotos de Fórmula 1 para a temporada de 2025. Através do uso de dados históricos, foi possível criar um modelo que permitiu calcular a probabilidade de cada piloto alcançar pontos acima de 10, com uma acurácia de **0.88**.

O trabalho foi realizado em duas partes principais: a criação de um modelo interativo para ajudar usuários a escolher entre hobbies ou carreiras para entender melhor como funciona uma árvore de decisão, e a utilização de um dataset real de Fórmula 1 para prever a performance dos pilotos em 2025. O modelo mostrou um bom desempenho, refletido na sua acurácia e nas previsões de probabilidade de sucesso de cada piloto.

Os resultados obtidos, principalmente para pilotos como **Max Verstappen** e **Lando Norris**, confirmam a consistência do modelo e sua capacidade de identificar padrões de performance em dados históricos. Em termos de impacto, a análise pode ser útil para ver pilotos que possuem melhor constância e desempenho, oferecendo uma base sólida para previsões e decisões baseadas em dados. 

Por fim, é importante ressaltar que, apesar da acurácia obtida, sempre há espaço para melhorias no modelo, como a inclusão de mais variáveis que possam influenciar o desempenho dos pilotos, o que pode aprimorar ainda mais as previsões em cenários futuros.


## Autores

- Frank Leite Lemos Costa – Aluno do 6º período de Engenharia da Computação.
- Mateus Henrique Pereira – Aluno do 8º período de Engenharia da Computação.

