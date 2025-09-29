# controller/item_controller.py
from typing import List
import streamlit as st
from model import Item
from database import ItemDAO

class ItemController:
    dao = ItemDAO()

    @staticmethod
    @st.cache_data
    def obterTodosOsItens() -> List[Item]:
        return ItemController.dao.listarTodos()

    @staticmethod
    def criarItem(nome: str, descricao: str, quantidade: int):
        if not nome or not nome.strip():
            st.error("O nome do item não pode ficar vazio.")
            return

        if not descricao or not descricao.strip():
            st.error("A descrição não pode ficar vazia.")
            return

        try:
            quantidade_int = int(quantidade)
        except (ValueError, TypeError):
            st.error("Quantidade deve ser um número inteiro.")
            return

        if quantidade_int < 0:
            st.error("A quantidade não pode ser negativa.")
            return

        novo = Item(id=None, nome=nome.strip(), descricao=descricao.strip(), quantidade=quantidade_int)
        ItemController.dao.adicionar(novo)
        # Limpa cache para atualizar a lista
        st.cache_data.clear()
        st.success("Item adicionado com sucesso.")