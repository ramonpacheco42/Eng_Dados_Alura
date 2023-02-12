# Importando as bibliotecas utilizadas no projeto.
import io
import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd

# carregando variáveis de ambiente.
load_dotenv()
host = os.environ['host']
port= os.environ['port']
database= os.environ['database']
user= os.environ['user']
password= os.environ['password']

# carregando datasets.
cobranca_de_pacientes = pd.read_csv(r'csv/inpatientCharges.csv')
# Fazendo ETL no datset mudando as colunas que estão em string para float.
cobranca_de_pacientes[' Average Covered Charges '] = cobranca_de_pacientes[' Average Covered Charges '].str.replace('$', '')
cobranca_de_pacientes[' Average Total Payments '] = cobranca_de_pacientes[' Average Total Payments '].str.replace('$', '')
cobranca_de_pacientes['Average Medicare Payments'] = cobranca_de_pacientes['Average Medicare Payments'].str.replace('$', '')

diagnosticos = pd.read_csv(r'csv/datasets_180_408_data.csv')
# ETL
# Removendo colunas indesejadas no dataset.
diagnosticos.drop(diagnosticos.columns[len(diagnosticos.columns)-1], axis=1, inplace=True)

# Criando uma função para carregar dados
def carregar_dados(conn, df, table , columns):
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    try:
        print(df)
        print(f'\nDados carregados com sucesso!!')
        cur.copy_from(output, table, null='', columns=columns)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)


# chamando a função carregar dados e persistindo os dados no banco de dados.

carregar_dados(conn, cobranca_de_pacientes, 'cobranca_paciente', ('definicao', 
                                                            'identificacao',
                                                            'nome', 
                                                            'endereco',
                                                            'cidade',
                                                            'estado',
                                                            'codigo_postal',
                                                            'regiao',
                                                            'total_cobrancas',
                                                            'media_custos_cobertos',
                                                            'media_pagamento_total',
                                                            'media_gastos_cuidados'))

carregar_dados(conn, diagnosticos, 'dados_analises', ('id',
                                                    'diagnostico',
                                                    'media_raio',
                                                    'media_textura',
                                                    'media_perimetro',
                                                    'media_area',
                                                    'media_suavidade',
                                                    'media_compactacao',
                                                    'media_concavidade',
                                                    'media_concavidade_pontos',
                                                    'media_simetria',
                                                    'media_dimensao_fractal',
                                                    'se_raio',
                                                    'se_textura',
                                                    'se_perimetro',
                                                    'se_area',
                                                    'se_suavidade',
                                                    'se_compactacao',
                                                    'se_concavidade',
                                                    'se_concavidade_pontos',
                                                    'se_simetria',
                                                    'se_dimensao_fractal',
                                                    'pior_raio',
                                                    'pior_textura',
                                                    'pior_perimetro',
                                                    'pior_area',
                                                    'pior_suavidade',
                                                    'pior_compactacao',
                                                    'pior_concavidade',
                                                    'pior_concavidade_pontos',
                                                    'pior_simetria',
                                                    'pior_dimensao_fractal'))