import pandas as pd
import numpy as np

class File_Manipuling:
    def __init__(self, File):
        self.LOCAL_FILE = File
        self.read_file()
    
    def read_file(self) -> None:
        """Cria um dataframe com os dados do arquivo"""
        self.__df = pd.read_csv(self.LOCAL_FILE, sep = ";", header = 0, encoding = "utf-8")
    
    def transform_columns_value_br(self, columns) -> None:
        """transforma em valor brasileiro novamente"""
        self.__df[columns] = self.__df[columns].applymap(lambda x: f"{x:.2f}")
        self.__df[columns] = self.__df[columns].applymap(lambda x : self.__acrescentar_number(self.acrescentar_br_caractere(x)))
    
    def __acrescentar_number(self, value):
        """Acrescenta um 0 aos valores que falta"""
        if value[len(value) - 1] == ",":
            value += "0"
        return value
        
    def acrescentar_br_caractere(self, value):
        """Acrescenta o R$ e a ,"""
        if value != "NaN" and value != "nan":
            value = f"R${value.replace('.', ',')}"
        return value
    
    def replace_columns(self, columns, data, new_data):
        """Subistitui dados de mais de uma coluna"""
        self.__df[columns] = self.__df[columns].applymap(lambda x : x.replace(data, new_data))
        
    def line_mean(self, Linha, Columns, Printar = False):
        """retorna a media da linha"""
        mean = float(f"{self.__df.loc[Linha, Columns].mean():.2f}")
        mean = self.acrescentar_br_caractere(self.__acrescentar_number(f"{mean:.2f}"))
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
    
        
    def convert_columns_float32(self, Columns):
        """Converte uma coluna para float32"""
        self.__df[Columns] = self.__df[Columns].astype(np.float32)
        
    @property
    def df(self):
        """Retorna o DataFrame"""
        return self.__df  