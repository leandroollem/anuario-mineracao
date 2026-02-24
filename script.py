# %%
import pandas as pd
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
print("\n=== Tipos de Dados ===")
print("\nProdução Bruta:")
print(f"\n{df_bruta.dtypes}")
print("\nProdução Beneficiada:")
print(f"\n{df_benef.dtypes}")
# %%
df_bruta["Indicação Contido"] = df_bruta["Indicação Contido"].fillna("Sem informação")
df_bruta
# %%
df_bruta.isnull().sum()
# %%
