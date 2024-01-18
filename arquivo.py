import pandas as pd
import time
import os
import random
import blib

# Leitura do arquivo de dados
arquivo1 = "Planilhas/relatorios-Teste2.xlsx"
arquivo_dados_1 = pd.read_excel(arquivo1)

# Inicializando DataFrames
Dados_Treino = pd.DataFrame()
D_Ent_Teste = pd.DataFrame()
D_Sai_Teste = pd.DataFrame()

total_linhas = quantidade_linhas = len(arquivo_dados_1)
por_30 = int(total_linhas * 0.3)
por_50 = int(total_linhas * 0.5)

x = 0
while x < total_linhas:
    os.system('cls') 
    linha_aleatoria = random.randint(0, quantidade_linhas - 1)
    porcento = blib.Calculo_Percentual(total_linhas, x)
    
    if x < por_30:
   
        linha_excluida = arquivo_dados_1.iloc[linha_aleatoria].to_frame().T
        Dados_Treino = pd.concat([Dados_Treino, linha_excluida], ignore_index=True)
        arquivo_dados_1 = arquivo_dados_1.drop(arquivo_dados_1.index[linha_aleatoria])
        quantidade_linhas -= 1
        print("DELETADO <1> ===== Porcentagem: ", porcento, "%")

    elif x < por_50:
        linha_excluida = arquivo_dados_1.iloc[linha_aleatoria].to_frame().T
        linha_para_adicionar_entrada = pd.DataFrame([linha_excluida.iloc[0, :9].tolist()], columns=linha_excluida.columns[:9])
        D_Ent_Teste = pd.concat([D_Ent_Teste, linha_para_adicionar_entrada], ignore_index=True)

        linha_para_adicionar_saida = pd.DataFrame([linha_excluida.iloc[0, -1].tolist()], columns=[linha_excluida.columns[-1]])
        D_Sai_Teste = pd.concat([D_Sai_Teste, linha_para_adicionar_saida], ignore_index=True)

        arquivo_dados_1 = arquivo_dados_1.drop(arquivo_dados_1.index[linha_aleatoria])
        quantidade_linhas -= 1
        print("DELETADO <2> ===== Porcentagem: ", porcento, "%")

    else:
        break

    x += 1

# Salvando os arquivos finais
arquivo_dados_1.to_excel("Planilhas/Metade.xlsx", index=False)
Dados_Treino.to_excel("Planilhas/Dados_Treino.xlsx", index=False)
D_Ent_Teste.to_excel("Planilhas/D_Ent_Teste.xlsx", index=False)
D_Sai_Teste.to_excel("Planilhas/D_Sai_Teste.xlsx", index=False)

blib.Finalizado()
