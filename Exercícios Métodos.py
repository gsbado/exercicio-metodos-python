import time

def SomaPositivos (x,y):
  if (x < 0 or y < 0):
    return -1
  else:
    return x+y

def Divide (x,y):
  if (y == 0):
    print ("Erro: Y não pode ser 0")
    return 0
  else:
    return x/y

def VerificaTriangulo (x,y,z):
  if (x==y) and (x==z):
    return "Equilátero"
  elif x==y or x==z or y==z:
    return "Isósceles" 
  else:
    return "Escaleno"

def VerificaIdade (i):
  if (i<0):
    return "Erro, menor que zero"
  if (0<i<=12):
    return "Criança"
  if (13<=i<=18):
    return "Adolescente"
  if (19<=i<=120):
    return "Adulto"
  if (i > 120):
    return "Erro, maior que 120"

def Sinaleira (cor):
  if (cor=="verde"):
    print ("Aberta")
  elif (cor=="amarela"):
    print ("Atenção")
  elif (cor=="vermelha"):
    print ("Fechada")
  else:
    print ("Erro")

def Contador (x):
  for i in range (x+1,301):
      print (i)

def achaMaior (x,y,z):
  if x>y and x>z:
    print (x)
  elif z>y and z>x:
    print (z)
  else:
    print (y)

def imprimePares (x):
  for i in range (0,x+1):
    if i%2 ==0:
     print (i)
    

while True:
  print ("\nSeja bem-vindo ao MENU")
  print ("\nMENU")
  
  print ("1. Soma positivos")
  print ("2. Divide")
  print ("3. Verifica triângulo")
  print ("4. Verifica idade")
  print ("5. Sinaleira")
  print ("6. Conta até 300")
  print ("7. Acha maior")
  print ("8. Imprime pares")
  print ("9. Sair")

  opcao = int(input("Digite o número da opção desejada: "))
  
  if opcao == 9:
    break
    
  elif opcao == 1:
    print ("Você escolheu somar dois números positivos")
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    print ("A soma dos positivos é:" ,SomaPositivos (x,y))
    time.sleep (1)

  elif opcao == 2:
    print ("Você escolheu dividir dois números positivos")
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    print ("A divisão dos positivos é:" ,Divide (x,y))

  elif opcao == 3:
    print ("Você escolheu verificar o tipo de triângulo")
    x = int(input("Digite o valor de um lado do triângulo: "))
    y = int(input("Digite o valor de outro lado do triângulo: "))
    z = int(input("Digite o valor do último lado do triângulo: "))
    print ("O triângulo é:" ,VerificaTriangulo (x,y,z))

  elif opcao == 4:
    print ("Você escolheu identificar a faixa etária")
    x = int(input("Digite a idade: "))
    print ("A faixa etária é:" ,VerificaIdade (x))

  elif opcao == 5:
    print ("Você escolheu a opção de sinaleira")
    cor = input("Digite a cor da sinaleira: ")
    print ("A situação da sinaleira é:",end=" ")
    Sinaleira (cor)
    
  elif opcao == 6:
    print ("Você escolheu contar até 300")
    x = int(input("Digite o valor de x: "))
    print ("Contagem:",end=" ")
    Contador(x)

  elif opcao == 7:
    print ("Você escolheu verificar qual o número maior")
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    z = int(input("Digite o valor de z: "))
    print ("O maior número é:",end=" ")
    achaMaior(x,y,z)
    
  elif opcao == 8:
    print ("Você escolheu imprimir pares")
    x = int(input("Digite o valor de x: "))
    print ("Listagem com todos os números pares até X:",end=" ")
    imprimePares(x)