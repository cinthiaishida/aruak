import os

def get_db_path():
    """
    Retorna o caminho absoluto do arquivo SQLite incluído no pacote.
    """
    base_path = os.path.dirname(__file__)
    db_path = os.path.join(base_path, "_data", "aruak.db")
    return db_path
