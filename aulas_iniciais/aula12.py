time = []
while True:    
   print("--- Time ---")
   print("Opcao 1: Adicionar Jogador")
   print("Opcao 2: Ver Time")
   print("Opcao 3: Remover Jogador")
   print("Opcao 0: Sair")

   opcao = int(input("Selecione a Opcao:"))
   print("")
   if opcao == 1:
      nome = input("Digite o nome do Jogador:")
      time.append(nome)
      print("")
   elif opcao == 2:
      print("--- Time Atual ---")
      for pessoa in time:
        print(pessoa)

   elif opcao == 3:
    if len(time) == 0:
        print("Time esta Vazio")
    else:
        demitido = time.pop(0)
        print(f"{demitido} foi demitido")

   elif opcao == 4: 
     break
else:
    print("Opcao invalida")