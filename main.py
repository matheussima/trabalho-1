# aluno: Matheus Klering Sima

#ENUNCIADO
#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
#linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de
#operações que serão realizadas entre dois conjuntos de dados.
#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas
#seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da
#operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:

with open("calculo.txt", "r", encoding="UTF-8") as arquivo:
    mensagem = arquivo.read()
print(mensagem, "\n")

with open("arquivo.txt", "r", encoding="UTF-8") as calculo:
    y = calculo.read()
print(y, "\n")

with open("maiscalculo.txt", "r", encoding="UTF-8") as tentativa:
    x = tentativa.read()
print(x, "\n")