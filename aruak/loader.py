from importlib import resources
import os

def get_db_path():
    """
    Retorna o caminho absoluto do arquivo SQLite incluído no pacote.
    Ex.: para usar com sqlite3.connect(get_db_path())
    """
    # resources.files existe para Python 3.9+
    path = resources.files("aruak._data") / "aruak.db"
    return str(path)