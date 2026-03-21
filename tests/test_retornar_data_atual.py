import re
from datetime import date

from src.retornar_data_atual import retornar_data_atual


def test_retornar_data_igual_data_atual():
    """Verifica que a função retorna a data atual no formato YYYY-MM-DD."""
    assert retornar_data_atual() == date.today().strftime("%Y-%m-%d")


def test_formato_da_data():
    """Valida o formato (quatro dígitos-2 dígitos-2 dígitos) e comprimento."""
    s = retornar_data_atual()
    assert isinstance(s, str)
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", s)
    assert len(s) == 10
