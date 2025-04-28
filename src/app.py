import pandas as pd
import streamlit as st

# Função para adicionar dados ao DataFrame do usuário
def adicionar_dado(tipo, categoria, valor):
<<<<<<< HEAD
=======
    # Verifica se o dicionário do usuário já existe
>>>>>>> 6706113b36fafe03b8c6d163f186b4e699ca734f
    if "dados" not in st.session_state:
        st.session_state.dados = pd.DataFrame(columns=["Tipo", "Categoria", "Valor"])

    nova_linha = {"Tipo": tipo, "Categoria": categoria, "Valor": valor}
    st.session_state.dados = pd.concat([st.session_state.dados, pd.DataFrame([nova_linha])], ignore_index=True)

# Função de login simples
def login():
    st.title("Bem-vindo ao Orçamento Pessoal")
    
    nome_usuario = st.text_input("Digite seu nome de usuário:")
    if nome_usuario:
        st.session_state.usuario = nome_usuario  # Salva o nome do usuário na sessão
        st.success(f"Bem-vindo, {nome_usuario}!")
    else:
        st.warning("Por favor, insira seu nome de usuário.")
    
    return nome_usuario

# Função para visualizar dados
def visualizar_dados():
    if "dados" in st.session_state:
        st.write("Dados do usuário:", st.session_state.dados)
    else:
        st.write("Nenhum dado registrado ainda.")

# Inicia a sessão com o nome do usuário
if "usuario" not in st.session_state:
    login()
else:
    st.write(f"Usuário logado: {st.session_state.usuario}")

    # Opções de inserir dados
    tipo = st.selectbox("Escolha o tipo de dado", ["Receita", "Despesa"])
    categoria = st.text_input("Digite a categoria (Ex: Salário, Alimentação, etc.):")
    valor = st.number_input("Digite o valor (R$):", min_value=0.0)

    if st.button("Adicionar Dado"):
        if categoria and valor > 0:
            adicionar_dado(tipo, categoria, valor)
            st.success(f"{tipo} de {categoria} de R$ {valor:.2f} foi adicionada com sucesso!")
        else:
            st.error("Preencha todos os campos corretamente.")

    # Mostrar dados registrados
    visualizar_dados()

    # Salvar os dados em um arquivo CSV
    if st.button("Salvar Dados"):
        if "dados" in st.session_state:
            nome_arquivo = f"dados_{st.session_state.usuario}.csv"
            st.session_state.dados.to_csv(nome_arquivo, index=False)
            st.success(f"Dados salvos para {st.session_state.usuario} como {nome_arquivo}")
        else:
            st.error("Nenhum dado registrado para salvar.")
