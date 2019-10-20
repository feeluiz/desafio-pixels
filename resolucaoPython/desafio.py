#Ler cada pixel da imagem e contar todos pixels vermelhos e cortonar pixels pretos

from pathlib import Path #bibliotecado diretorios
from PIL import Image #biblioteca para tratar imagens
import numpy as np #biblioteca para trabalhar com bitdata arrays grandes

#! Variaveis Globais
imagePath = str(Path(__file__).cwd()) + '/img/img.png' #passa caminho inteiro
contador = 0

# abre a imagem
img = Image.open(imagePath)

#pega o tamanho da imagem
size = w, h= img.size

#carrega os bytes da imagem como cores RGB
data = img.load()

#le todos os pixels de por linha em cada coluna
for y in range(h):
    for x in range(w):
        ponto = data[x, y] # define o pixel desejado
        red, green, blue = ponto # desestrutura para ficar mais verboo
        if(red == 255 and green == 0 and blue == 0): # quando encontra pixel red
            data[x,y] = (51, 0, 204) #altera pixel para cor azul 
            contador += 1 #conta
            print(f' Munando ponto x:{x}, ponto y:{y} para azul.')
        elif(red == 0 and green == 0 and blue == 0): #caso seja totalmente preto
            data[x,y] = (0, 255, 0) #transforma em verde
            print(f' Munando ponto x:{x}, ponto y:{y} para verde.')

data = np.array(img) #cria um array do numpy 
newImage = Image.fromarray(data) # faz o parse do array
newImage.show() # exibe a nova imagem 
# !print o numero de pixels vermelhos encontrados
print('###### Total de pontos: ', contador,'######') 