import streamlit as st
from db import get_db
from bson import ObjectId

st.title("E-Shop Brasil - CRUD de Clientes")

db = get_db()
collection = db["clientes"]

menu = ["Criar", "Ler", "Atualizar", "Deletar"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Criar":
    st.subheader("Cadastrar Cliente")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    if st.button("Cadastrar"):
        collection.insert_one({"nome": nome, "email": email})
        st.success("Cliente cadastrado com sucesso!")

elif choice == "Ler":
    st.subheader("Lista de Clientes")
    docs = list(collection.find())
    for doc in docs:
        st.write(f"ID: {doc['_id']} | Nome: {doc['nome']} | Email: {doc['email']}")

elif choice == "Atualizar":
    st.subheader("Atualizar Cliente")
    id_cliente = st.text_input("ID do Cliente")
    novo_nome = st.text_input("Novo Nome")
    novo_email = st.text_input("Novo Email")
    if st.button("Atualizar"):
        collection.update_one({"_id": ObjectId(id_cliente)}, {"$set": {"nome": novo_nome, "email": novo_email}})
        st.success("Cliente atualizado.")

elif choice == "Deletar":
    st.subheader("Deletar Cliente")
    id_cliente = st.text_input("ID do Cliente")
    if st.button("Deletar"):
        collection.delete_one({"_id": ObjectId(id_cliente)})
        st.warning("Cliente deletado.")
