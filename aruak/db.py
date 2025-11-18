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
            (c for c in unicodedata.normalize('NFD', letra) if unicodedata.category(c) != 'Mn')
        )

    def buscar_traducao_por_conceito(self, palavra):
        palavra_original = palavra.lower()
        
        conn = self._connect()
        c = conn.cursor()
        
        query = '''SELECT doculect, concept, transcription, fonte FROM dados WHERE concept LIKE ?'''
        c.execute(query, ('%' + palavra_original + '%',))
        resultados = c.fetchall()
        conn.close()

        return resultados

    def buscar_por_transcricao(self, trecho):
        trecho_original = trecho.lower()
        
        conn = self._connect()
        c = conn.cursor()
        
        query = '''SELECT doculect, concept, transcription, fonte FROM dados WHERE transcription LIKE ?'''
        c.execute(query, ('%' + trecho_original + '%',))
        resultados = c.fetchall()
        conn.close()

        return resultados

    def dicionario_completo(self):
        conn = self._connect()
        c = conn.cursor()
        
        query = '''SELECT doculect, concept, transcription, fonte FROM dados'''
        c.execute(query)
        resultados = c.fetchall()
        conn.close()

        return resultados
