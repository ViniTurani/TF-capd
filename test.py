import pandas as pd

# Load data
dados_votos = pd.read_csv("data_cleaned_extrato-bancario.csv")
dados_partidos = pd.read_csv("historico_presidentes_cleaned.csv")

# Sum transactions for each party
# Assuming the first column is the party and the second column is the transaction amount
dados_votos_summed = (
    dados_votos.groupby("SG_PARTIDO")["VR_LANCAMENTO"].sum().reset_index()
)

# Sum votes for each party in the historico_presidentes dataset
# We assume that the columns to sum are the ones you listed
columns_to_sum = [
    "QT_APTOS_TOT",
    "QT_VOTOS_TOTAL",
    "CIRO_GOMES_QT_VOTOS_TOT",
    "LULA_QT_VOTOS_TOT",
    "PADRE_KELMON_QT_VOTOS_TOT",
    "SIMONE_TEBET_QT_VOTOS_TOT",
    "VERA_QT_VOTOS_TOT",
    "SOFIA_MANZANO_QT_VOTOS_TOT",
    "JAIR_BOLSONARO_QT_VOTOS_TOT",
    "CONSTITUINTE_EYMAEL_QT_VOTOS_TOT",
    "FELIPE_DAVILA_QT_VOTOS_TOT",
    "SORAYA_THRONICKE_QT_VOTOS_TOT",
    "LEO_PERICLES_QT_VOTOS_TOT",
    "BRANCO_QT_VOTOS_TOT",
    "NULO_QT_VOTOS_TOT",
]

dados_partidos_summed = (
    dados_votos.groupby("SG_PARTIDO")[columns_to_sum].sum().reset_index()
)

df_integrado = pd.merge(dados_votos_summed, dados_partidos_summed, on="SG_PARTIDO")

print(df_integrado.head())


df_integrado.to_csv("final_integrated_data.csv", index=False)
