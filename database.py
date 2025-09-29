# database/item_dao.py
import sqlite3
from typing import List
from model import Item

class ItemDAO:
    def __init__(self, db_name: str = "itens.db"):
        self.DB_NAME = db_name
        self._criar_tabela()

    def get_connection(self):
        conn = sqlite3.connect(self.DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn

    def _criar_tabela(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def adicionar(self, item: Item):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO itens (nome, descricao, quantidade) VALUES (?, ?, ?)",
            (item.nome, item.descricao, item.quantidade)
        )
        conn.commit()
        conn.close()

    def listarTodos(self) -> List[Item]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM itens ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()

        return [
            Item(
                id=row["id"],
                nome=row["nome"],
                descricao=row["descricao"],
                quantidade=row["quantidade"]
            ) for row in rows
        ]