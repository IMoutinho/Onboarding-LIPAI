# Análise exploratória do csv de classificação

import pandas as pd

df = pd.read_csv('./02-pandas/dataset/classification_results_trial_0001.csv')

print(df.head())

distribuicao_real  = df['real_class'].value_counts()
print("1. Distribuição das classes reais: \n", distribuicao_real)

