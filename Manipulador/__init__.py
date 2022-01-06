import pandas as pd
import numpy as np

class File_Manipuling:
    def __init__(self):
        self.__LOCAL_FILE = "Planilha_Precos_Material_Escolar.csv"
    
    def read_file(self):
        """Retorna um dataframe com os dados do arquivo"""
        self.__df = pd.read_csv(self.__LOCAL_FILE, sep = ";", header = 0, encoding = "utf-8")
    
    def transform_columns_value_br(self, columns):
        """Acrescenta o R$ e virgula para virar valor brasileiro novamente"""
        self.__df[columns] = self.__df[columns].applymap(lambda x : self.__acrescentar_number(f"R${x.replace('.', ',')}"))
    def __acrescentar_number(self, value):
        """Acrescenta um 0 aos valores que falta"""
         if value[len(value) - 1] == ",":
            value = value += "0"
        print(value)
        return value
    
    def replace_columns(self, columns, data, new_data):
        """Subistitui dados de mais de uma coluna"""
        self.__df[columns] = self.__df[columns].applymap(lambda x : x.replace(data, new_data))
        
    def line_mean(self, Linha, Columns, Printar = False):
        """retorna a media da linha"""
        mean = float(f"{self.__df.loc[Linha, Columns].mean():.2f}")
        if Printar == True:
            print(f"{self.__df.iloc[Linha, 0]} \t Media:\t      {mean}")
            
        return mean
        
    def lines_mean(self, Columns, Printar = False):
        """Retorna a media de valor dos produtos"""
        Products = {}
        cont = 0
        for Column in range(18):
            mean = self.line_mean(cont, Columns)
            Products[self.__df.iloc[cont, 0]] = mean
            cont += 1
            
        if Printar == True:
            print("Media".center(110))
            [print("{:>47} \t\t{}".format(k, v)) for k, v in Products.items()]
        return Products
    
    def line_max(self, Linha, Columns, Printar = False):
        """retorna a media da linha"""
        max = float(f"{self.__df.loc[Linha, Columns].max():.2f}")
        if Printar == True:
            print(f"{self.__df.iloc[Linha, 0]} \t Maior Valor: {max}")
            
        return max
    
    def line_min(self, Linha, Columns, Printar = False):
        """retorna a media da linha"""
        min = float(f"{self.__df.loc[Linha, Columns].min():.2f}")
        if Printar == True:
            print(f"{self.__df.iloc[Linha, 0]} \t Menor Valor: {min}")
            
        return min
        
    def convert_columns_float32(self, Columns):
        """Converte uma coluna para float32"""
        self.__df[Columns] = self.__df[Columns].astype(np.float32)
        
    @property
    def df(self):
        """Retorna a tabela"""
        return self.__df
        
    @property
    def LOCAL_FILE(self):
        return self.__LOCAL_FILE
        
    @LOCAL_FILE.setter
    def LOCAL_FILE(self, local):
        self.__LOCAL_FILE = local
        
if __name__ == "__main__":
    Manipulador = File_Manipuling() #Objeto de manipulação
    Manipulador.LOCAL_FILE = "../" + Manipulador.LOCAL_FILE # Muda o endereço do arquivo
    Manipulador.read_file() # le o arquivo
    
    #Arrumando os valores numericos
    Manipulador.replace_columns(Manipulador.df.columns[1:], "R$ ", "")
    Manipulador.replace_columns(Manipulador.df.columns[1:], ",", ".")
    Manipulador.replace_columns(Manipulador.df.columns[1:], "-", "NaN")
    
    Manipulador.convert_columns_float32(Manipulador.df.columns[1:])#Convertendo os valores para float,        para mexer com valores
    Manipulador.line_mean(0, Manipulador.df.columns[1:], True) # Pegando a media de uma Linha
    Manipulador.line_max(0, Manipulador.df.columns[1:], True) # Pegando o maior valor de uma Linha
    Manipulador.line_min(0, Manipulador.df.columns[1:], True) # Pegando o menor valor de uma Linha
    
    Manipulador.lines_mean(Manipulador.df.columns[1:], True) #Mostra a media das linhas