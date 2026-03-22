import pandas as pd


def calcular_informacoes_df(df: pd.DataFrame, colunas: list) -> dict:
    """
    Essa função calcula a média, o valor máximo e o valor mínimo de uma coluna específica em um DataFrame.

    Args:
        df (pandas.DataFrame): O DataFrame de entrada que contém a coluna a ser analisada.
        colunas (list): A lista de nomes das colunas a serem analisadas.

    Returns
    -------
        dict: Um dicionário contendo a média, o valor máximo e o valor mínimo da coluna especificada,
        com as chaves 'media', 'maximo' e 'minimo'.

    """
    informacoes = {}
    for coluna in colunas:
        informacoes[coluna] = {"media": df[coluna].mean(), "maximo": df[coluna].max(), "minimo": df[coluna].min()}
    return informacoes
