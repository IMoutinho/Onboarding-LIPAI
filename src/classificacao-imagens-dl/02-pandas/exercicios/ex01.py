# Análise exploratória do csv de classificação

import pandas as pd

df = pd.read_csv(
    './src/classificacao-imagens-dl/02-pandas/dataset/classification_results_trial_0001.csv')

# 1. Quais imagens são "benign" e "malign"?
distribuicao_real = df['real_class'].value_counts()
print("1. Distribuição das classes reais: \n", distribuicao_real)

# 2. Identifique quais são as imagens o modelo errou a predição
erro_predicao = df[df['real_class'] != df['predicted_class']]
print("\n2. Imagens com erro de predição: \n", erro_predicao)

# 3. Verifique se o erro estava confiante mesmo quando errou.
prob_erros = erro_predicao[['prob_benign', 'prob_malign']].max(axis=1)
erro_confiante = erro_predicao[prob_erros > 0.7]
print("\n 3. Confiança do modelo em predições erradas: ")
print(erro_confiante[['image_path', 'real_class',
      'predicted_class', 'prob_benign', 'prob_malign']])

# 4. Calcule:
# a.)TP
tp = len(df[(df['real_class'] == 'malign') &
         (df['predicted_class'] == 'malign')])
# b)TN
tn = len(df[(df['real_class'] == 'benign') &
         (df['predicted_class'] == 'benign')])
# c)FP
fp = len(df[(df['real_class'] == 'benign') &
         (df['predicted_class'] == 'malign')])
# d)FN
fn = len(df[(df['real_class'] == 'malign') &
         (df['predicted_class'] == 'benign')])
print("\n4. Cálculo de TP, TN, FP, FN:")
print(f"TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}")


# 5. Calcule:
# a) acurácia
acuracia = (tp+tn)/(tp+tn+fp+fn)
print(f"\n5. a) Acurácia: {acuracia:.2f}")
# b) precisão
precisao = tp/(tp+fp)
print(f"5. b) Precisão: {precisao:.2f}")
# c) recall
recall = tp/(tp+fn)
print(f"5. c) Recall: {recall:.2f}")
#d) especificidade
especificidade = tn/(tn+fp)
print(f"5. d) Especificidade: {especificidade:.2f}")

#6. Encontre as 5 imagens com benign com menor prob_benign. O que isso pode indicar? 
menor_benign = df[df['real_class'] == 'benign'].sort_values(by='prob_benign').head()
print("\n6. Imagens benign com menor probabilidade de benign: \n", menor_benign[['image_path', 'prob_benign']])
#O que isso pode indicar:
#Pode indicar que o modelo está com dificuldades em identificar as caracteristicas que diferenciem os dois modelos e, dado
#a porcentagem das ultimas imagens, pode indicar que o modelo com mais facilidade classifica imagens como malignas. O que é 
#validado pela proxima questão.

#7. Encontre as 5 imagens com malign com maior probabilidade de benigno. O que isso pode indicar? 
maior_benign_malign = df[df['real_class'] == 'malign'].sort_values(by='prob_benign', ascending=False).head()
print("\n7. Imagens malign com maior probabilidade de benigno: \n", maior_benign_malign[['image_path', 'prob_benign']])
#O que isso pode indicar:
#Pode indicar que o modelo não está refinando bem o suficiente as caracteristicas que distinguem os dois. 
#Se classifica imagens malignas como benignas é um erro mais grave, levando a um falso negativo.