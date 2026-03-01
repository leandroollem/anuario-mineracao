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
df_bruta
# %%
df_benef
# %%
df_bruta["Indicação Contido"] = df_bruta["Indicação Contido"].fillna("Sem informação")
df_bruta

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

df_benef["Quannidade Produção"] = df_benef["Quanntidade Produção"].apply(str_to_float)
df_benef["Quantidade Contido"] = df_benef["Quantidade Contido"].apply(str_to_float)
df_benef["Quantidade Venda"] = df_benef["Quantidade Venda"].apply(str_to_float)
df_benef["Valor Venda (R$)"] = df_benef["Valor Venda (R$)"].apply(str_to_float)
df_benef["Quantidade Transferência para Transformação / Utilização / Consumo"] = df_benef["Quantidade Transferência para Transformação / Utilização / Consumo"].apply(str_to_float)
df_benef["Valor Transferência para Transformação / Utilização / Consumo (R$)"] = df_benef["Valor Transferência para Transformação / Utilização / Consumo (R$)"].apply(str_to_float)


# %%
df_bruta.isnull().sum()
# %%
