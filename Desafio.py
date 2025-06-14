import pandas as pd
import numpy as np

dados = pd.read_csv('/content/DF.csv', sep=';', encoding='utf-8', low_memory=False)
dados.columns = dados.columns.str.strip().str.lower()

filtro_bairros = (
    (dados['dsc_localidade'].str.contains('Asa Norte', case=False, na=False)) |
    (dados['dsc_localidade'].str.contains('Riacho Fundo I', case=False, na=False))
)

filtro_nicho = dados['dsc_estabelecimento'].str.contains('Pet Shop', case=False, na=False)

dados_filtrados = dados[filtro_bairros & filtro_nicho]

dados_filtrados = dados_filtrados.drop_duplicates()
dados_filtrados = dados_filtrados.dropna(subset=['nom_seglogr', 'dsc_estabelecimento'])

agrupamento_bairro = dados_filtrados.groupby('dsc_localidade').size().reset_index(name='quantidade')
print(agrupamento_bairro)

agrupamento_logradouro = dados_filtrados.groupby('nom_seglogr').size().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)
print(agrupamento_logradouro.head(10))

agrupamento_setor = dados_filtrados.groupby('cod_setor').size().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)
print(agrupamento_setor)
