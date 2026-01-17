# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend

# pip install openai streamlit python-dotenv 

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # carregar variáveis de ambiente do arquivo .env

my_api_key = os.getenv("my_api_key")

modelo = OpenAI(api_key=my_api_key)

st.write("### ChatBot com IA") # markdown

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem (igual lista): st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> usuário
    # assistant -> IA
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    try:
        resposta_ia = modelo.chat.completions.create(
            messages=st.session_state["lista_mensagens"],
            model="gpt-4o"
        )
    except Exception as e:
        st.error(f"Erro ao conectar com a API da OpenAI: {e}")
        resposta_ia = None

    if resposta_ia:
        try:
            resposta_ia = resposta_ia.choices[0].message.content
        except:
            resposta_ia = "Desculpe, não consegui processar sua solicitação no momento."

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


