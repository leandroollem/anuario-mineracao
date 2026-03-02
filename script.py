# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_bruta = pd.read_csv("data/Producao_Bruta.csv", encoding="latin1")
df_benef = pd.read_csv("data/Producao_Beneficiada.csv", encoding="latin1")

print("=== VISÃO GERAL DO DATASET == ")
print(f"\nFormato da Produção Bruta: {df_bruta.shape[0]} linhas e {df_bruta.shape[1]} colunas")
print(f"Formato da Produção Beneficiada: {df_benef.shape[0]} linhas e {df_benef.shape[1]} colunas")
print("\n=== Nomes das Colunas ===")
print("\nProdução Bruta:")
print(f"\n{df_bruta.columns.to_list()}")
print("\nProdução Beneficiada:")
print(f"\n{df_benef.columns.to_list()}")
# %%
print("=== Tipos de Dados ===")
print("\n| ANTES DA PADRONIZAÇÃO |")
print("\nProdução Bruta:")
print(f"\n{df_bruta.dtypes}")
print("\nProdução Beneficiada:")
print(f"\n{df_benef.dtypes}")

def str_to_float(x:str):
    x = (x.replace(" ", "")
          .replace(",", ".")
          .replace("\xa0","")
        )
    return float(x)

df_bruta["Quantidade Produção - Minério ROM (t)"] = df_bruta["Quantidade Produção - Minério ROM (t)"].apply(str_to_float)
df_bruta["Quantidade Contido"] = df_bruta["Quantidade Contido"].apply(str_to_float)
df_bruta["Quantidade Venda (t)"] = df_bruta["Quantidade Venda (t)"].apply(str_to_float)
df_bruta["Valor Venda (R$)"] = df_bruta["Valor Venda (R$)"].apply(str_to_float)
df_bruta["Quantidade Transformação / Consumo / Utilização (t)"] = df_bruta["Quantidade Transformação / Consumo / Utilização (t)"].apply(str_to_float)
df_bruta["Valor Transformação / Consumo / Utilização nesta mina (R$)"] = df_bruta["Valor Transformação / Consumo / Utilização nesta mina (R$)"].apply(str_to_float)
df_bruta["Quantidade Transferência para Transformação / Utilização / Consumo (t)"] = df_bruta["Quantidade Transferência para Transformação / Utilização / Consumo (t)"].apply(str_to_float)
df_bruta["Valor Transferência para Transformação / Utilização / Consumo (R$)"] = df_bruta["Valor Transferência para Transformação / Utilização / Consumo (R$)"].apply(str_to_float)

df_benef["Quantidade Produção"] = df_benef["Quantidade Produção"].apply(str_to_float)
df_benef["Quantidade Consumo/Utilização na Usina"] = df_benef["Quantidade Consumo/Utilização na Usina"].apply(str_to_float)
df_benef["Valor Consumo / Utilização na Usina (R$)"] = df_benef["Valor Consumo / Utilização na Usina (R$)"].apply(str_to_float)
df_benef["Quantidade Contido"] = df_benef["Quantidade Contido"].apply(str_to_float)
df_benef["Quantidade Venda"] = df_benef["Quantidade Venda"].apply(str_to_float)
df_benef["Valor Venda (R$)"] = df_benef["Valor Venda (R$)"].apply(str_to_float)
df_benef["Quantidade Transferência para Transformação / Utilização / Consumo"] = df_benef["Quantidade Transferência para Transformação / Utilização / Consumo"].apply(str_to_float)
df_benef["Valor Transferência para Transformação / Utilização / Consumo (R$)"] = df_benef["Valor Transferência para Transformação / Utilização / Consumo (R$)"].apply(str_to_float)

print("\n| DEPOIS DA PADRONIZAÇÃO |")
print("\nProdução Bruta:")
print(f"\n{df_bruta.dtypes}")
print("\nProdução Beneficiada:")
print(f"\n{df_benef.dtypes}")
# %%
print("=== Check de Valores Nulos ===")
print("\n| ANTES DA LIMPEZA |")
print(f"\nTotal de valores não informados na Produção Bruta: {df_bruta.isnull().sum().sum()} | Porcentagem: {round(df_bruta.isnull().mean()*100,2)}")
print(f"Total de valores não informados na Produção Beneficiada: {df_benef.isnull().sum().sum()} | Porcentagem: {round(df_benef.isnull().mean()*100,2)}")
df_bruta["Indicação Contido"] = df_bruta["Indicação Contido"].fillna("Sem informação")
df_benef["Indicação Contido"] = df_benef["Indicação Contido"].fillna("Sem Informação")
print("\n| DEPOIS DA LIMPEZA |")
print(f"\nTotal de valores não informados na Produção Bruta: {df_bruta.isnull().sum().sum()} | Porcentagem: {round(df_bruta.isnull().mean()*100,2)}")
print(f"Total de valores não informados na Produção Beneficiada: {df_benef.isnull().sum().sum()} | Porcentagem: {round(df_benef.isnull().mean()*100,2)}")
# %%
print("=== Check de Duplicatas ===")
print(f"\n| PRODUÇÃO BRUTA |")
print(f"Número de linhas duplicadas: {df_bruta.duplicated().sum()}")
print(f"\n| PRODUÇÃO BENEFICIADA |")
print(f"Número de linhas duplicadas: {df_benef.duplicated().sum()}")

# %%
print ("=== Substâncias por Unidade de Medida ===")

unidades_de_medida = ['t', 'ct', 'kg']

print("\n| PRODUÇÃO BRUTA |")
filtro1 = df_bruta[df_bruta["Unidade de Medida - Contido"].isin(unidades_de_medida)]
substancias_por_unidade1 = filtro1.groupby(["Unidade de Medida - Contido", "Substância Mineral"]).size().reset_index()

for unidade in unidades_de_medida:
    lista = substancias_por_unidade1[substancias_por_unidade1["Unidade de Medida - Contido"] == unidade]["Substância Mineral"].unique()
    print(f"\nSubstâncias em {unidade}: {len(lista)} encontradas")
    print(f"\nAs substãncias são: {lista}")

print("\n| PRODUÇÃO BENEFICIADA |")

filtro2 = df_benef[df_benef["Unidade de Medida - Produção"].isin(unidades_de_medida)]
substancias_por_unidade2 = filtro2.groupby(["Unidade de Medida - Produção", "Substância Mineral"]).size().reset_index()

for unidade in unidades_de_medida:
    lista = substancias_por_unidade2[substancias_por_unidade2["Unidade de Medida - Produção"] == unidade]["Substância Mineral"].unique()
    print(f"\nSubstâncias em {unidade}: {len(lista)} encontradas")
    print(f"\nAs substãncias são: {lista}")

# %%
print("=== Check de Outliers ===")
print("\n| PRODUÇÃO BRUTA |")
estatisticas = df_bruta["Valor Venda (R$)"].describe()
print(f"\n{estatisticas}")
top10 = df_bruta.nlargest(10, 'Valor Venda (R$)')[['Ano base', 'UF', 'Substância Mineral', 'Valor Venda (R$)']]
print("\nMaiores Valores Registrados")
print(top10)

print("\n| PRODUÇÃO BENEFICIADA |")
estatisticas = df_benef["Valor Venda (R$)"].describe()
print(f"\n{estatisticas}")
top10 = df_benef.nlargest(10, 'Valor Venda (R$)')[['Ano base', 'UF', 'Substância Mineral', 'Valor Venda (R$)']]
print("\nMaiores Valores Registrados")
print(top10)
# %%
