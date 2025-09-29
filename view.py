# view/app.py
import streamlit as st
from controller import ItemController

st.set_page_config(page_title="Cadastro de Itens", layout="centered")
st.title("Cadastro e Listagem de Itens")

st.header("Adicionar novo item")
with st.form(key="new_item_form", clear_on_submit=True):
    nome = st.text_input("Nome do item")
    descricao = st.text_area("Descrição do item")
    quantidade = st.number_input("Quantidade", min_value=0, step=1, format="%d")
    submit_button = st.form_submit_button(label="Adicionar")

if submit_button:
    ItemController.criarItem(nome, descricao, quantidade)
    st.rerun()

st.markdown("---")

st.header("Itens Cadastrados")

tds_itens = ItemController.obterTodosOsItens()

if not tds_itens:
    st.info("Nenhum item cadastrado ainda.")
else:
    for item in tds_itens:
        st.subheader(f"{item.nome}")
        st.write(f"Descrição: {item.descricao}")
        st.write(f"Quantidade: {item.quantidade}")
        st.caption(f"ID: {item.id}")
        st.markdown("---")
