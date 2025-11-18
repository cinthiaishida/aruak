import sqlite3
import unicodedata
from .loader import get_db_path

class AruakDB:
    def __init__(self):
        self.path = get_db_path()

    def _connect(self):
        return sqlite3.connect(self.path)

    def remover_acentos_letra(self, letra):
        return ''.join(
            c for c in unicodedata.normalize('NFD', letra)
            if unicodedata.category(c) != 'Mn'
        )

    def buscar_traducao_por_conceito(self, palavra):
        palavra_original = palavra.lower()

        conn = self._connect()
        cur = conn.cursor()
        cur.execute(
            "SELECT doculect, concept, transcription, fonte FROM dados WHERE concept LIKE ?",
            (f"%{palavra_original}%",)
        )
        res = cur.fetchall()
        conn.close()
        return res

    def buscar_por_transcricao(self, trecho):
        trecho_original = trecho.lower()

        conn = self._connect()
        cur = conn.cursor()
        cur.execute(
            "SELECT doculect, concept, transcription, fonte FROM dados WHERE transcription LIKE ?",
            (f"%{trecho_original}%",)
        )
        res = cur.fetchall()
        conn.close()
        return res

    def dicionario_completo(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(
            "SELECT doculect, concept, transcription, fonte FROM dados"
        )
        res = cur.fetchall()
        conn.close()
        return res
