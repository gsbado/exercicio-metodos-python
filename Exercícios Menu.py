nome = input("\n***SEJA BEM-VINDO AO MENU MULTIUSO***" + "\nDigite seu nome, por favor: ")

while True:

  print ("\nOlá",nome)
  
  print ("Digite a opção desejada: ")
  
  print ("1) Verificar triângulo")
  print ("2) Calcular equação do segundo grau")
  print ("3) Conferir data")
  print ("4) Verificar tamanho do texto")
  print ("5) Analisar CPF")
  print ("6) Contar caracteres")
  print ("7) Sair")

  opcao = int(input())

  if opcao == 7:
    print("Obrigado por utilizar nosso sistema")
    break
    
  elif opcao == 1:
    print ("Você escolheu verificar triângulo")
    a = int(input("Digite o valor do lado A do triângulo: "))
    b = int(input("Digite o valor do lado B do triângulo: "))
    c = int(input("Digite o valor do lado C do triângulo: "))

    conferencia1 = abs(b - c) < a and a < (b + c)
    conferencia2 = abs(a - b) < c and c < (a + b)
    conferencia3  = abs(a - c) < b and b < (a + c)
    triangulo = ""
    if conferencia1 and conferencia2 and conferencia3:
      if (a==b) and (b==c):
        triangulo = "equilátero"
      elif (a==b) or (a==c) or (b==c):
        triangulo = "isósceles" 
      elif (a != b) and (b != c):
        triangulo = "escaleno"
      print ("Esse triângulo é",triangulo) 
    else:
      print ("Esse não é um triângulo válido")
    
  elif opcao == 2:
    print ("Você escolheu calcular uma equação do segundo grau")
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    delta = ((b**2) - (4*a*c))
    x1 = 0
    x1 = 0

    if a == 0:
      print("O valor de 'a' não pode ser zero pois assim, não se trata de uma equação do segundo grau")
    elif delta < 0:
      print("O resultado de delta foi negativo. Nesse caso, a equação não possui raízes reais")
    elif delta == 0:
      x1 = (b*-1)/(2*a)
      print("O resultado de delta foi zero. Nesse caso, a equação possui apenas uma raiz real: %.2f" %x1)
    else:
      x1 = ((b*-1) + (delta**(1/2))) / (2*a)
      x2 = ((b*-1) - (delta**(1/2))) / (2*a)
      print("As raízes são x(1)= %.2f"%x1,"e x(2)= %.2f"%x1)

  elif opcao == 3:
    print ("Você escolheu conferir data")
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o número do mês: "))
    ano = int(input("Digite o ano: "))
    
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
      if dia <= 31 and dia >=1:
          print ("Essa data é válida")
      else:
          print ("Essa data é inválida. Tente novamente.")
    elif mes==4 or mes==6 or mes==9 or mes==11:
        if dia <= 30 and dia >=1:
          print ("Essa data é válida")
        else:
          print ("Essa data é inválida. Tente novamente.")
    elif mes==2:
      if dia <= 29 and dia >=1:
        print ("Essa data é válida")
      else:
        print ("Essa data é inválida. Tente novamente.")
    
  elif opcao == 4:
    print ("Você escolheu verificar o tamanho de um texto")
    texto = input("Digite o seu texto: ")
    x = len(texto)
    if x<5:
      print ("Esse texto é muito pequeno")
    elif x >=5 and x<15:
      print ("Esse texto é de tamanho médio")
    elif x >=15 and x<=20:
      print ("Esse texto é de tamanho grande")
    else:
      print ("Esse texto é inválido")

  elif opcao == 5:
    print ("Você escolheu analisar CPF")
    cpf = input("Digite o CPF (apenas com números): ")
    x = len(cpf)
    y = cpf.isdigit() 
    if x==11 and y==True:
      print ("CPF válido")
    else:
      print ("CPF inválido")
      
  elif opcao == 6:
    print ("Você escolheu contar caracteres de um texto")
    texto = input("Digite a frase desejada: ")
    
    lista_vogais = ["a", "e", "i", "o", "u"]
    vogais = sum(texto.lower().count(v) for v in lista_vogais)
    espacos = texto.count (" ")
    outros = len(texto) - (vogais + espacos)

    print (f"Quantidade de vogais: {vogais}")
    print (f"Quantidade de espaços: {espacos}")
    print (f"Quantidade de outros caracteres (consoantes ou caracteres especiais): {outros}")
      
  else:
    print ("Erro: a opção digitada para esse menu deve ser entre 1 e 7")