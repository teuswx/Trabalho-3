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

Este critério foi estabelecido para identificar pilotos que apresentaram uma pontuação consistente nas corridas, permitindo avaliar sua performance ao longo do campeonato. Como a coluna **`target`** utiliza como parâmetro a pontuação de cada piloto, métricas muito relacionadas a pontuação são descartadas.

## Descrição dos Algoritmos Implementados 📜  

- **Arquivo `arvore.py`**:  
  Implementa uma árvore de decisão iterativa com diversas perguntas para auxiliar o usuário na escolha de hobbies ou carreiras com base em suas preferências e respostas. O código é estruturado para fornecer sugestões personalizadas, criando uma interação simples.
  
- **Notebook `ML.ipynb`**:  
  Contém o código desenvolvido utilizando a biblioteca `scikit-learn` para análise e previsão com base no dataset selecionado. O notebook realiza o pré-processamento dos dados, treina uma árvore de decisão para identificar padrões e faz previsões sobre o desempenho dos pilotos no dataset de Fórmula 1.

## Algoritmos de Classificação 📊

Além da árvore de decisão, foram implementados outros algoritmos de classificação para comparar seu desempenho. Os algoritmos escolhidos são:

### 1. **Support Vector Machine (SVM)**  
SVM é um algoritmo de aprendizado supervisionado que pode ser usado tanto para problemas de classificação quanto de regressão. O principal objetivo do SVM é encontrar um hiperplano que melhor separe as diferentes classes em um espaço de características. No contexto de classificação, o SVM tenta encontrar a "margem máxima" entre as classes, o que significa que ele busca o hiperplano que tem a maior distância de qualquer ponto de dados de ambas as classes.

- **Vantagens:**
  - Eficiente em espaços de alta dimensão.
  - Funciona bem em casos onde o número de dimensões é maior do que o número de amostras.
  - Utiliza o conceito de margem, o que pode resultar em uma boa generalização.

- **Desvantagens:**
  - Requer mais tempo de treinamento em grandes datasets.
  - Difícil de interpretar em alguns casos.
  - Sensível a outliers.

### 2. **K-Nearest Neighbors (KNN)**  
O KNN é um algoritmo de aprendizado supervisionado que classifica um ponto de dados com base na classe da maioria de seus vizinhos mais próximos no espaço das características. A ideia é simples: para classificar uma amostra, o algoritmo encontra os K vizinhos mais próximos e faz a classificação com base na maioria das classes desses vizinhos.

- **Vantagens:**
  - Fácil de entender e implementar.
  - Não requer um modelo explícito de treinamento, o que torna o treinamento rápido.
  - Funciona bem com dados não-lineares e com muitas classes.

- **Desvantagens:**
  - Pode ser computacionalmente caro, especialmente com grandes volumes de dados.
  - Sensível ao valor de K e à escolha da distância.
  - Pode sofrer de alta variação em datasets com ruído.

## Estrutura do Projeto 🏗️

- **Linguagem:** Python.
- **Bibliotecas Utilizadas:**
  - **pandas**: Para manipulação e análise de dados, incluindo carregamento e pré-processamento do dataset.
  - **scikit-learn**:
    - `DecisionTreeClassifier`: Para criação e treinamento da árvore de decisão.
    - `SVC`: Para criação e treinamento do modelo SVM.
    - `KNeighborsClassifier`: Para criação e treinamento do modelo KNN.
    - `train_test_split`: Para dividir os dados em conjuntos de treino e teste.
    - `accuracy_score`: Para calcular a acurácia do modelo.
    - `plot_tree`: Para visualização gráfica da árvore de decisão.
  - **matplotlib.pyplot**: Para criar gráficos e visualizar a árvore de decisão.

## Resultados das Medições de Desempenho ⏱️

### Decision Tree
Com o modelo desenvolvido, foi possível analisar os dados do dataset e visualizar a árvore de decisão gerada durante o treinamento. A árvore de decisão foi construída para classificar os pilotos com base nos atributos selecionados, e sua estrutura fornece uma visão clara das regras usadas pelo modelo para fazer as previsões.  

Abaixo está a visualização da árvore de decisão treinada:

![Árvore de Decisão](https://github.com/user-attachments/assets/c73e75f1-aa2e-4b4e-9434-749bd2bc3342)

Foi possível obter uma acurácia de **0.88**, o que significa um valor **muito bom** de acerto para previsão.

# KNN (K-Nearest Neighbors)

K-Nearest Neighbors (KNN) é um algoritmo de aprendizado supervisionado usado para **classificação** e **regressão**. Ele baseia suas previsões na proximidade dos dados de entrada em relação a outros pontos do conjunto de treinamento.

## Funcionamento do KNN
1. **Escolha do número de vizinhos (K)**: Define quantos vizinhos mais próximos serão considerados na predição.
2. **Cálculo da distância entre os pontos**: Normalmente, usa-se a **distância Euclidiana** para medir a proximidade.
3. **Seleção dos K vizinhos mais próximos**.
4. **Classificação ou regressão**:
   - **Classificação**: O novo ponto recebe a classe mais frequente entre os vizinhos.
   - **Regressão**: O novo ponto recebe a média dos valores dos vizinhos.

---

## Cálculo da Distância no KNN

O KNN usa fórmulas matemáticas para medir a similaridade entre os pontos. A mais comum é a **distância Euclidiana**, definida por:

$$
d(p, q) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}
$$

Onde:
- \( p \) e \( q \) são dois pontos no espaço n-dimensional.
- \( q_i \) e \( p_i \) são as coordenadas dos pontos nos diferentes atributos.
- \( d(p, q) \) é a distância Euclidiana entre os pontos.

### Exemplo de Cálculo:
Se temos dois pontos \( A(2, 3) \) e \( B(5, 7) \), a distância Euclidiana entre eles é:

$$
d(A, B) = \sqrt{(5 - 2)^2 + (7 - 3)^2}
$$

$$
d(A, B) = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

Além da distância Euclidiana, outras métricas podem ser usadas, como:
- **Distância de Manhattan**: 

$$
d(p, q) = \sum |q_i - p_i|
$$

- **Distância de Minkowski**: Generaliza as anteriores com um parâmetro \( p \):

$$
d(p, q) = \left( \sum |q_i - p_i|^p \right)^{\frac{1}{p}}
$$

---

## Variância doa acurácia do KNN
A acurácia do KNN pode variar por diferentes motivos, mesmo usando os mesmos dados:

- **Escolha do valor de K**: Valores diferentes podem gerar resultados distintos.
- **Divisão dos dados (Treino/Teste)**: Pequenas variações na separação dos dados podem mudar a classificação.
- **Normalização dos dados**: A escala dos atributos pode influenciar no cálculo das distâncias.
- **Pontos de fronteira**: Pequenas alterações nos dados podem mudar os vizinhos mais próximos, impactando a predição.

Após o embaralhamento dos dados, a média passou a oscilar entre 0,8577 e 0,8661. Embora a diferença entre esses valores seja insignificativa, observou-se uma alteração na variância dos dados após o processo de embaralhamento. Isso indica que o embaralhamento teve um impacto relevante na dispersão dos valores, mesmo que a média tenha se mantido em uma faixa estreita.
 
### Support Vector Machine (SVM)

Support Vector Machine (SVM) é um algoritmo de aprendizado de máquina supervisionado usado principalmente para classificação, mas também pode ser aplicado em regressão. Ele trabalha encontrando o hiperplano ótimo que separa as classes de forma mais eficiente possível.

---

## Como Funciona o SVM?

1. **Margem Máxima**:
   - O SVM busca encontrar o hiperplano que maximiza a margem entre as classes de dados. A margem é definida como a distância entre o hiperplano e os pontos mais próximos de cada classe, chamados de **vetores de suporte**.

2. **Vetores de Suporte**:
   - São os pontos de dados que estão mais próximos do hiperplano e definem sua posição. A remoção de qualquer um desses pontos pode alterar a posição do hiperplano.

3. **Hiperplano Ótimo**:
   - O hiperplano é uma linha (em 2D), um plano (em 3D) ou um hiperplano em dimensões superiores que separa as classes da melhor maneira possível.

4. **Classificação Linear e Não Linear**:
   - Se os dados forem linearmente separáveis, o SVM encontrará um hiperplano reto.
   - Se os dados não forem linearmente separáveis, usa-se o **truque do kernel**, que transforma os dados para um espaço dimensional superior onde se tornam linearmente separáveis.

---

## Função do Kernel

O kernel é uma função que transforma os dados em um espaço dimensional superior para tornar a separação possível. Os principais tipos de kernel são:

- **Linear**: $ K(x, y) = x \cdot y $
- **Polinomial**: $ K(x, y) = (x \cdot y + c)^d $
- **RBF (Radial Basis Function)**: $ K(x, y) = e^{-\gamma ||x - y||^2} $
- **Sigmóide**: $ K(x, y) = \tanh(x \cdot y + c) $

---

## Fórmula Matemática do SVM

Dado um conjunto de treinamento com $ n $ amostras $ (x_i, y_i) $, onde $ y_i \in \{-1, 1\} $, o SVM resolve o seguinte problema de otimização:

$$
\min_{{w, b}} \frac{1}{2} ||w||^2 \quad \text{sujeito a } \quad y_i (w \cdot x_i + b) \geq 1, \forall i
$$

Caso haja erros de classificação, usa-se a versão com **variáveis de folga** $ \xi_i $:

$$
\min_{{w, b, \xi}} \frac{1}{2} ||w||^2 + C \sum \xi_i \quad \text{sujeito a } \quad y_i (w \cdot x_i + b) \geq 1 - \xi_i, \forall i
$$

Onde $ C $ é um hiperparâmetro que controla o trade-off entre margem e erro de classificação.

---

## Aplicações do SVM

- **Reconhecimento de padrões** (exemplo: reconhecimento de escrita)
- **Diagnóstico médico** (exemplo: detecção de câncer)
- **Detecção de fraudes**
- **Processamento de imagens**

---

## Vantagens e Desvantagens

### Vantagens:
- Funciona bem em conjuntos de dados com margens claras de separação.
- Eficiente em espaços de alta dimensão.
- Usa um subconjunto de pontos de treinamento (vetores de suporte), tornando-o eficiente em termos de memória.

### Desvantagens:
- Sensível à escolha do tipo de kernel e dos hiperparâmetros.
- Pode ser computacionalmente caro para conjuntos de dados muito grandes.

---

## Conclusão

O SVM é um poderoso algoritmo de aprendizado de máquina usado principalmente para classificação. Seu princípio central é encontrar um hiperplano ótimo que maximize a margem entre as classes. Com o uso de funções de kernel, ele pode lidar com dados não linearmente separáveis, tornando-se uma ferramenta versátil para diversas aplicações.

Com o SVM foi possível obter uma acurácia de 0.86, o que é um valor muito bom de acertos
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

## Compilação e Execução 

A pilha dinâmica disponibilizada possui um arquivo Makefile que realiza todo o procedimento de compilação e execução. Para tanto, temos as seguintes diretrizes de execução:

| Comando                |      Função                                                                                           |                     
| -----------------------| ------------------------------------------------------------------------------------------------- |
|  `python analisef1.py` | Realiza a filtragem dos dados necessários para análise                                            |
|  `python arvore.py`    |              Roda o código da parte 1 do trabalho                                                 |

## Autores

- Frank Leite Lemos Costa – Aluno do 6º período de Engenharia da Computação.
- Mateus Henrique Pereira – Aluno do 8º período de Engenharia da Computação.
