import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv(
    './src/classificacao-imagens-dl/02-pandas/dataset/classification_results_trial_0001.csv')

plt.style.use("ggplot")

df['acerto'] = df['real_class'] == df['predicted_class']


def verificar_erro(row):
    if row['real_class'] == 'benign' and row['predicted_class'] == 'malign':
        return 'Falso Positivo'
    elif row['real_class'] == 'malign' and row['predicted_class'] == 'benign':
        return 'Falso Negativo'
    else:
        return 'Acerto'


df['tipo_erro'] = df.apply(verificar_erro, axis=1)

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 16))
fig.suptitle("Visualização do CSV de Classificação",
             fontsize=18, color="#E727F8")
plt.subplots_adjust(
    left=0.1,
    right=0.9,
    top=0.9,
    bottom=0.1,
    wspace=0.3,
    hspace=0.4
)

# 1
contagem = df['real_class'].value_counts()
axes[0, 0].bar(contagem.index, contagem.values, color=['salmon', 'lightblue'])
axes[0, 0].set_title("Distribuição das Classes Reais",
                     fontsize=14, color="#20B2AA")
axes[0, 0].set_xlabel("Classe", fontsize=12, color="#20B2AA")
axes[0, 0].set_ylabel("Contagem", fontsize=12, color="#20B2AA")

# 2
contagem_pred = df['predicted_class'].value_counts()
axes[0, 1].bar(contagem_pred.index, contagem_pred.values,
               color=['lightblue', 'salmon'])
axes[0, 1].set_title("Distribuição das Classes Preditas",
                     fontsize=14, color="#20B2AA")
axes[0, 1].set_xlabel("Classe", fontsize=12, color="#20B2AA")
axes[0, 1].set_ylabel("Contagem", fontsize=12, color="#20B2AA")

# 3
axes[1, 0].hist(df['prob_benign'], bins=20, color='lightblue',
                edgecolor='black', alpha=0.7)
axes[1, 0].set_title(
    "Histograma da Probabilidade de Benignidade", fontsize=14, color="#20B2AA")
axes[1, 0].set_xlabel("Probabilidade de Benignidade",
                      fontsize=12, color="#20B2AA")
axes[1, 0].set_ylabel("Frequência", fontsize=12, color="#20B2AA")
# 4
axes[1, 1].hist(df['prob_malign'], bins=20, color='salmon',
                edgecolor='black', alpha=0.7)
axes[1, 1].set_title(
    "Histograma da Probabilidade de Malignidade", fontsize=14, color="#20B2AA")
axes[1, 1].set_xlabel("Probabilidade de Malignidade",
                      fontsize=12, color="#20B2AA")
axes[1, 1].set_ylabel("Frequência", fontsize=12, color="#20B2AA")

# 5
acertos = df[df['acerto'] == True]
erros = df[df['acerto'] == False]
axes[2, 0].scatter(acertos['prob_benign'], acertos['prob_malign'],
                   color='green', label='Acertos', alpha=0.6)
axes[2, 0].scatter(erros['prob_benign'], erros['prob_malign'],
                   color='red', label='Erros', alpha=0.6)
axes[2, 0].set_title(
    "Dispersão das Probabilidades por Acertos e Erros", fontsize=14, color="#20B2AA")
axes[2, 0].set_xlabel("Probabilidade de Benignidade",
                      fontsize=12, color="#20B2AA")
axes[2, 0].set_ylabel("Probabilidade de Malignidade",
                      fontsize=12, color="#20B2AA")
axes[2, 0].legend()

# 6
erros_tipo = df[df['tipo_erro'] != 'Acerto']['tipo_erro'].value_counts()

if not erros_tipo.empty:
    axes[2, 1].bar(erros_tipo.index, erros_tipo.values,
                   color=['orange', 'purple'])
    axes[2, 1].set_title("Contagem dos Tipos de Erros",
                         fontsize=14, color="#20B2AA")
    axes[2, 1].set_xlabel("Tipo de Erro", fontsize=12, color="#20B2AA")
    axes[2, 1].set_ylabel("Contagem", fontsize=12, color="#20B2AA")
else:
    axes[2, 1].text(0.5, 0.5, "Nenhum erro encontrado", fontsize=12, color="#20B2AA",
                    ha='center', va='center')


plt.show()
