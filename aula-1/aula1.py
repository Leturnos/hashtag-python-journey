import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3 # tempo de espera entre cada comando do pyautogui

# abrir o navegador 
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(1)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# fazer login
pyautogui.click(x=827, y=370)
pyautogui.write("python@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("senha123")
pyautogui.click(x=969, y=552) # clique no botao de login
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

# Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=808, y=253)
    
    # pegar da tabela o valor do campo que a gente quer preencher
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
