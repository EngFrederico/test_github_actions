from src.calcular_soma import somar_numero


def test_somar_dois_numeros_positivos():
    """Testa a soma de dois números positivos."""
    resultado = somar_numero(2, 3)
    assert resultado == 5


def test_somar_numero_positivo_e_negativo():
    """Testa a soma de um número positivo e um número negativo."""
    resultado = somar_numero(5, -2)
    assert resultado == 3


def test_somar_dois_numeros_negativos():
    """Testa a soma de dois números negativos."""
    resultado = somar_numero(-4, -6)
    assert resultado == -10
