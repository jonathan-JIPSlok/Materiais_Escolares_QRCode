from Manipulador import *
from QRCode import *

Manipulador = File_Manipuling("Planilha_Precos_Material_Escolar.csv")

#Arrumando os valores numericos
Manipulador.replace_columns(Manipulador.df.columns[1:], "R$ ", "")
Manipulador.replace_columns(Manipulador.df.columns[1:], ",", ".")
Manipulador.replace_columns(Manipulador.df.columns[1:], "-", "NaN")

Manipulador.convert_columns_float32(Manipulador.df.columns[1:])#Convertendo os valores para float, para mexer com valores

Medias = Manipulador.lines_mean(Manipulador.df.columns[1:]) #Pega a media dos produtos

imagens = list(map(QR, [f"{k} \t {v}" for k, v in Medias.items()])) #Montando as Imagens

list(map(Salvar, imagens, [f"./Imagens/{N.replace(' ', '_').replace('/', '.')}.png" for N in Medias.keys()])) # Salvando as imagens

Medias_Save = "MEDIA DE VALORES DOS PRODUTOS\n"
for k, v in Medias.items():
    Medias_Save += f"{k:>47} \t\t{v}\n"

Salvar(QR(Medias_Save), "Imagens/Media_Produtos.png") # Salva o Arquivo Compelto