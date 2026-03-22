import math

import pandas as pd
import pytest

from src.calcular_informacoes_df import calcular_informacoes_df


def test_calcular_informacoes_df_valores_simples():
    """Testa a função com um DataFrame simples contendo valores numéricos."""
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4.0, 5.0, 6.0]})
    resultado = calcular_informacoes_df(df, ["a", "b"])

    assert resultado["a"]["media"] == 2
    assert resultado["a"]["maximo"] == 3
    assert resultado["a"]["minimo"] == 1

    assert resultado["b"]["media"] == 5.0
    assert resultado["b"]["maximo"] == 6.0
    assert resultado["b"]["minimo"] == 4.0


def test_calcular_informacoes_df_com_nan():
    """Testa a função com um DataFrame que contém valores NaN para verificar se eles são ignorados corretamente."""
    df = pd.DataFrame({"a": [1, None, 3]})
    resultado = calcular_informacoes_df(df, ["a"])

    # mean should ignore NaN and be (1 + 3) / 2
    assert resultado["a"]["media"] == 2.0
    assert resultado["a"]["maximo"] == 3.0
    assert resultado["a"]["minimo"] == 1.0


def test_calcular_informacoes_df_empty_dataframe():
    """Testa a função com um DataFrame vazio para verificar se ela lida corretamente com a ausência de dados."""
    df = pd.DataFrame({"a": [], "b": []})
    resultado = calcular_informacoes_df(df, ["a", "b"])

    # For empty columns, pandas returns NaN for mean/max/min
    assert math.isnan(resultado["a"]["media"])
    assert math.isnan(resultado["a"]["maximo"])
    assert math.isnan(resultado["a"]["minimo"])

    assert math.isnan(resultado["b"]["media"])
    assert math.isnan(resultado["b"]["maximo"])
    assert math.isnan(resultado["b"]["minimo"])


def test_calcular_informacoes_df_coluna_inexistente_levanta_keyerror():
    """Testa se a função levanta um KeyError quando uma coluna inexistente é solicitada."""
    df = pd.DataFrame({"a": [1, 2, 3]})
    with pytest.raises(KeyError):
        calcular_informacoes_df(df, ["nao_existe"])
