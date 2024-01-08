""" Aplicação que explora diversas funcionalidades da classe Imagem

Não usa Filtro's nem Album's.
Possíveis funcionalidades (opções) a acrescentar no futuro:
-- guardar imagem em ficheiro
-- imprimir informação detalhada de uma Imagem:
    nome
    etiquetas
    descrição
    path onde se encontrava (só no caso de ter sido importada de ficheiro)
-- filtrar Imagem's com diferentes Filtro's
-- trabalhar com Album's e usar as suas capacidades (sobretudo ALnumPlus):
    carregar pastas inteiras
    fazer pesquisas complexas
"""

# O uso de eval() é inseguro.
# Competiria a esta aplicação, ou qualquer outra, garantir que as strings
# de input para o eval() não contêm código malicioso.

from imagem import *
from copy import deepcopy # para poder clonar Imagem's

def lerOpcao():
  """ Mostra o menu de opções e lê a opção escolhida """
  print("\nOpções disponíveis:")
  print("1 - criar Imagem a partir de ficheiro")
  print("2 - listar Imagem's existentes")
  print("3 - ver uma Imagem")
  print("4 - avaliar uma expressão com Imagem's")
  print("5 - terminar esta sessão")
  opcaoEscolhida = input("A sua opção: ")
  return opcaoEscolhida

def criarImagemDeFicheiro():
  """ Cria uma Imagem a partir de um ficheiro indicado pelo utilizador

  Side-effects: lê do input o nome do ficheiro e, eventualmente, da pasta.
  Ensures: um novo objecto Imagem.
  """
  print(" Indique nome e pasta do ficheiro, separados por vírgula.")
  print(" Pode omitir o nome da pasta. Será usada a pasta de trabalho.")
  strPath = input(" Nome(s): ")
  fichPasta = strPath.split(",")
  for i in range(len(fichPasta)):
    fichPasta[i] = fichPasta[i].strip()  # limpa espaços extra
  if len(fichPasta) == 1:   # utilizador só escreveu nome do ficheiro
    novaImagem = Imagem(fichPasta[0])
  else:   # len(fichPasta) == 2  utilizador também escreveu nome da pasta
    novaImagem = Imagem(fichPasta[0], fichPasta[1])  
  return novaImagem

def listarImagens():
  """ Imprime o conteúdo do dicionário de Imagem's usando repr para Imagem's """
  print(im)  # usa o repr() para cada Imagem, portanto funciona sem o str()

def listarImagens():
  """ Versão mais simpática para o utilizador

  Imprime info semi-detalhada (repr) de cada Imagem numa linha separada.
  """
  for imagem in im.values():
    print(repr(imagem))

def avaliarExpressao():
  """ Cria uma Imagem por avaliação de uma expressão do utilizador

  Side-effects: lê do input a expressão a avaliar.
  Ensures: um novo objecto Imagem.
  """  
  print(" Operações disponíveis: + & ")  # concretizadas no imagem.py fornecido
  print(" Exemplo: im[2] + im[1] & im[3]")
  expressao = input(" Expressão a avaliar: ")
  novaImagem = eval(expressao)
  return novaImagem
    
# dicionário onde vamos guardar as Imagem's criadas
# criamos um dicionário manualmente porque não usamos Album's nesta versão
# neste dicionário, a chave é o número da Imagem, e o valor é o objecto Imagem
im = {}  # dicionário de Imagem's

# CICLO PRINCIPAL DA APLICAÇÃO

print("Bem vind@ à appImagem")
terminar = False
while not terminar:
  
  opcao = lerOpcao()
  
  if opcao == "1":
    try:
      novaImagem = criarImagemDeFicheiro()
      im[novaImagem.getNumero()] = deepcopy(novaImagem) # para poder reusar nome
    except Exception:
      print(" IMAGEM NÃO CRIADA -- verifique o(s) nome(s)")
      
  elif opcao == "2":
    listarImagens()
    
  elif opcao == "3":
    numeroImagem = int(input(" Número da Imagem? "))
    im[numeroImagem].show()
    
  elif opcao == "4":
    try:
      novaImagem = avaliarExpressao()
      im[novaImagem.getNumero()] = deepcopy(novaImagem)
    except Exception:
      print(" OPERAÇÃO INVÁLIDA -- verifique a sintaxe e os operandos")
      
  elif opcao == "5":
    terminar = True
    Imagem.guardarNumeroDeImagens() # guarda em ficheiro o contador de Imagem's
    
  else: # opção inválida: fazemos aqui mais um pouco de programação defensiva
    print(" OPÇÃO INVÁLIDA")
