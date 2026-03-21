def retornar_data_atual():
    """Função que retorna a data atual no formato "YYYY-MM-DD"."""
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d")
