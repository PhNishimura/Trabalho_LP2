#PROJETO LP2
#LUCA VIANNA MARTINS SILVEIRA 
#PEDRO HENRIQUE NISHIMURA BACHAALANI 


from time import sleep
import schema 
import categoria
import escuderia
import circuito
import piloto
import mecanico
import carro

#DEFININDO CORES:
cores = {
  'LIMPA': "\033[m",
  'WHITE': "\033[30m",
  'RED' : "\033[31m",
  'GREEN' : "\033[32m",
  'YELLOW' : "\033[33m",
  'BLUE' : "\033[34m",
  'PURPLE': "\033[35m",
  'CIANO': "\033[36m",
  'GREY': "\033[37m"
}

#FUNÇÃO MENU (ESCOLHA DA CLASSE)
def menu():
  
  try:
    print("""
    {}+------------------------------+
    |  🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁     |                       
    |🟢🟡🔴 MENU DAS CORRIDAS 🟢🟡🔴|
    |  🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁     |
    +------------------------------+{}
    """.format(cores["GREEN"], cores["LIMPA"]))
    
    print("{}0. Categorias\n1. Escuderias\n2. Circuitos\n3. Pilotos\n4. Mecânicos\n5. Carros\n6. Sair{}".format(cores["WHITE"], cores["LIMPA"])) 
    selecao = int(input("Selecione uma opção: "))
    return selecao
    
  except ValueError:
    print("{}\nDigite um caractere válido!{}".format(cores["RED"], cores["LIMPA"]))
  except KeyboardInterrupt:
    print("{}\nNão use este comando aqui!{}".format(cores["RED"], cores["LIMPA"]))
  except:
    print("\n{}Erro desconhecido...{}".format(cores["RED"], cores["LIMPA"]))
  finally:
    print("\nVerificando...")
    sleep(0.5)



   
#FUNÇÃO SUBMENU (ESCOLHA CRUD OBEJTOS DA CLASSE)
def submenu(tabela):
  try: 
    if tabela == "Carro":
      print(f"""
      +------------------------------+
      |  🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁                         
      |🟢🟡🔴 Menu do {tabela} 🟢🟡🔴      
      |  🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁    
      +------------------------------+
      """)
      print(f"1. Adicionar {tabela}\n2. Consultar {tabela}\n3. Atualizar {tabela}\n4. Excluir {tabela}\n5. Gráfico comparacao Jogos de Pneu\n6. Voltar ao menu principal")
      selecao2 = int(input("Selecione uma opção: ")) 
      return selecao2
      
    else: 
      print(f"""
      +--------------------------------+
      |  🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁                           
      |🟢🟡🔴 Menu do/a {tabela} 🟢🟡🔴  
      |  🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁     
      +--------------------------------+
      """)
      print(f"1. Adicionar {tabela}\n2. Consultar {tabela}\n3. Atualizar {tabela}\n4. Excluir {tabela}\n5. Voltar ao menu principal")
      selecao2 = int(input("Selecione uma opção: ")) 
      return selecao2
      
  except ValueError:
      print("{}\nDigite um caractere válido!{}".format(cores["RED"], cores["LIMPA"]))
  except KeyboardInterrupt:
    print("{}\nNão use este comando aqui!{}".format(cores["RED"], cores["LIMPA"]))
  except:
    print("{}\nErro desconhecido...{}".format(cores["RED"], cores["LIMPA"]))
  finally:
    print("\nVerificando...")
    sleep(0.5)

    

    

#FUNÇÕES (ADD, ATU, EX OBJETOS DAS CLASSES)
def adicionar(tabela):
  
  try:
    if tabela == "Categoria":
      nameCategoria = input("Qual o nome da Categoria: ")
      descCategoria = input("Qual a descrição da categoria: ")
      cat.adicionar_categoria(nameCategoria, descCategoria)
    elif tabela == "Escuderia":
      nameEscuderia = input("Qual o nome da Escuderia: ")
      sponsorEscuderia = input("Qual o nome do patriocionio da escuderia: ")
      victoryEscuderia = int(input("Quantas vitorias a escuderia possui: "))
      categoria_id = int(input("Qual o ID da Categoria: "))
      esc.adicionar_escuderia(nameEscuderia, sponsorEscuderia, victoryEscuderia, categoria_id)
    elif tabela == "Circuito":
      nameCircuito = input("Qual o nome do Circuito: ")
      countryCircuito = input("Qual o país do Circuito: ")
      descCircuito = input("Qual a descrição do Circuito: ")
      categoria_id = int(input("Qual o ID da categoria do circuito: "))
      circuit.adicionar_circuito(nameCircuito, countryCircuito, descCircuito, categoria_id)
    elif tabela == "Piloto":
      idEscuderia = int(input("Qual o ID da Escuderia do piloto: "))
      namePiloto = input("Qual o nome do Piloto: ")
      agePiloto = int(input("Qual a idade do Piloto: "))
      victoryPiloto = int(input("Quantas vitorias o Piloto tem: "))
      pi.adicionar_piloto(idEscuderia, namePiloto, agePiloto, victoryPiloto)
    elif tabela == "Mecanico":
      idEscuderia = int(input("Qual o ID da Escuderia do mecanico: "))
      nameMecanico = input("Qual o nome do mecanico: ")
      ageMecanico = int(input("Qual a idade do mecanico: "))
      functionMecanico = input("qual a funcao do mecanico: ")
      mec.adicionar_mecanico(idEscuderia, nameMecanico, ageMecanico, functionMecanico)
    elif tabela == "Carro":
      idEscuderia = int(input("Qual o ID da Escuderia do carro: "))
      idPiloto = int(input("Qual o ID do piloto: "))
      jPneu = input("Qual o tipo de Pneu do carro: ")
      speedCarro = int(input("Qual a velocidade do carro: "))
      lifeCarro = input("qual a integriadade do carro: ")
      car.adicionar_carro(idEscuderia, idPiloto, jPneu, speedCarro, lifeCarro)

  except ValueError:
      print("{}\nDigite um caractere válido!{}".format(cores["RED"], cores["LIMPA"]))
  except KeyboardInterrupt:
    print("{}\nNão use este comando aqui!{}".format(cores["RED"], cores["LIMPA"]))
  except:
    print("{}\nErro desconhecido...{}".format(cores["RED"], cores["LIMPA"]))



def atualizar(tabela):
  
  try:
    if tabela == "Categoria":
      idCategoria = int(input("Qual o ID da Categoria que deseja atualizar: "))
      newCategoria = input("Qual o novo nome da Categoria: ")
      newDescCategoria = input("Qual a nova descrição da Categoria: ")
      cat.atualizar_categoria(idCategoria, newCategoria, newDescCategoria)
    elif tabela == "Escuderia":
      idEscuderia = int(input("Qual o ID da Escuderia que deseja atualizar: "))
      newEscuderia = input("Qual o novo nome da escuderia: ")
      newSponsorEscuderia = input("Nome do novo patrocinador da da Escuderia: ")
      newVictoryEscuderia = int(input("Quantas vitorias a Escuderia tem: "))
      newCategoriaId = int(input("Qual o novo ID categoria da Escuderia: "))
      esc.atualizar_escuderia(idEscuderia, newEscuderia, newSponsorEscuderia, newVictoryEscuderia,newCategoriaId)
    elif tabela == "Circuito":
      idCircuito = int(input("Qual o ID do Circuito que deseja atualizar: "))
      newCircuito = input("Qual o novo nome do Circuito: ")
      newPaisCircuito = input("Qual o novo país do Circuito: ")
      newDescCircuito = input("Qual a nova descrição do circuito: ")
      categoria_id = int(input("Qual o novo ID categoria do circuito: "))
      circuit.atualizar_circuito(idCircuito, newCircuito, newPaisCircuito, newDescCircuito, categoria_id)
    elif tabela == "Piloto":
      idPiloto = int(input("Qual o ID do Piloto que deseja atualizar: "))
      newPilotoEscuderia = int(input("Qual a nova escuderia: "))
      newNamePiloto = input("Nome do piloto: ")
      newAgePiloto = int(input("Qual a nova idade do piloto: "))
      newVitoryPiloto = int(input("Qual a nova vitoria do piloto: "))
      pi.atualizar_piloto(idPiloto, newPilotoEscuderia, newNamePiloto, newAgePiloto,newVitoryPiloto)
    elif tabela == "Mecanico":
      idMecanico = int(input("Qual o ID do mecanico que deseja atualizar: "))
      newMecanicoEscuderia = int(input("Qual a nova escuderia: "))
      newNameMecanico = input("Nome do mecanico: ")
      newAgeMecanico = int(input("Qual a nova idade do mecanico: "))
      newfunctionMecanico = input("Qual a nova funcao do mecanico: ")
      mec.atualizar_mecanico(idMecanico, newMecanicoEscuderia, newNameMecanico, newAgeMecanico,newfunctionMecanico)
    elif tabela == "Carro": 
      idCarro = int(input("Qual o ID do carro que deseja atualizar: "))
      newEscuderia = int(input("Qual a nova escuderia: "))
      newPiloto = int(input("Qual o ID do novo piloto: "))
      newJPneu = input("Qual o novo jogo de Pneu do carro: ")
      newSpeedCarro = input("Qual a nova velocidade do carro: ")
      newLifeCarro = input("qual a nova integriadade do carro: ")
      car.atualizar_carro(idCarro, newEscuderia, newPiloto, newJPneu, newSpeedCarro, newLifeCarro)

  except ValueError:
      print("{}\nDigite um caractere válido!{}".format(cores["RED"], cores["LIMPA"]))
  except KeyboardInterrupt:
    print("{}\nNão use este comando aqui!{}".format(cores["RED"], cores["LIMPA"]))
  except:
    print("{}\nErro desconhecido...{}".format(cores["RED"], cores["LIMPA"]))


  
def excluir(tabela):
  
  try:
    if tabela == "Categoria":
      idCategoria = int(input("Informe o ID: "))
      cat.excluir_categoria(idCategoria)  
    elif tabela == "Escuderia": 
      idEscuderia = int(input("Informe o ID: "))
      esc.excluir_escuderia(idEscuderia)  
    elif tabela == "Circuito": 
      idCircuito = int(input("Informe o ID: "))
      circuit.excluir_circuito(idCircuito) 
    elif tabela == "Piloto":
      idPiloto = int(input("Informe o ID: "))
      pi.excluir_piloto(idPiloto) 
    elif tabela == "Mecanico":
      idMecanico = int(input("Informe o ID: "))
      mec.excluir_mecanico(idMecanico) 
    elif tabela == "Carro":
      idCarro = int(input("Informe o ID: "))
      car.excluir_carro(idCarro)

  except ValueError:
      print("{}\nDigite um caractere válido!{}".format(cores["RED"], cores["LIMPA"]))
  except KeyboardInterrupt:
    print("{}\nNão use este comando aqui!{}".format(cores["RED"], cores["LIMPA"]))
  except:
    print("{}\nErro desconhecido...{}".format(cores["RED"], cores["LIMPA"]))



def limpar():
    # Importar o módulo os do sistema operacional
    import os
    # Importar um módulo par aguardar um tempo em segundos passados como parametro

    def screen_clear():
        #Linux ou Mac
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # Windows
            _ = os.system('cls')
            
    sleep(1)
    screen_clear()



if __name__ == '__main__':
    limpar()
    print("Iniciando Projeto de LP2...")
    banco = 'teste'
    conn = schema.criar_banco(banco)

    limpar()
    opcao = menu()
    limpar()

    while opcao != 6:
#----------CASO A OPÇÃO SEJA CATEGORIAS---------------------------------------
      if opcao == 0:
        cat = categoria.Categoria(conn)
        tabela = "Categoria"
        opcaosub = submenu(tabela)
        limpar()
        while opcaosub != 5:
          if opcaosub == 1:
            addCat = adicionar(tabela)
          elif opcaosub == 2:
            cat.consultar_categoria()
          elif opcaosub == 3:
            atuCat = atualizar(tabela)
          elif opcaosub == 4:
            exCat = excluir(tabela)
          else:
            print("{}Opção inválida{}".format(cores["RED"], cores["LIMPA"]))
            
          limpar()
          opcaosub = submenu(tabela)
          limpar()

#----------CASO A OPÇÃO SEJA ESCUDERIAS---------------------------------------
      elif opcao == 1:
        esc = escuderia.Escuderia(conn)
        tabela = "Escuderia"
        opcaosub = submenu(tabela)
        limpar()
        while opcaosub != 5:
          if opcaosub == 1: 
            addEsc = adicionar(tabela)
          elif opcaosub == 2: 
            esc.consultar_escuderia()
          elif opcaosub == 3:
            atuEsc = atualizar(tabela)
          elif opcaosub == 4:
            exEsc = excluir(tabela) 
          else:
            print("{}Opção inválida{}".format(cores["RED"], cores["LIMPA"]))

          limpar()
          opcaosub = submenu(tabela)
          limpar()

#----------CASO A OPÇÃO SEJA CIRCUITOS---------------------------------------
      elif opcao == 2:
        circuit = circuito.Circuito(conn)
        tabela = "Circuito"
        opcaosub = submenu(tabela)
        limpar()        
        while opcaosub != 5:
          if opcaosub == 1:
            addCir = adicionar(tabela)
          elif opcaosub == 2:
            circuit.consultar_circuito() 
          elif opcaosub == 3:
            atuCir = atualizar(tabela)
          elif opcaosub == 4:
            exCir = excluir(tabela)
          else:
            print("{}Opção inválida{}".format(cores["RED"], cores["LIMPA"]))

          limpar()
          opcaosub = submenu(tabela)
          limpar()

#----------CASO A OPÇÃO SEJA PILOTOS---------------------------------------
      elif opcao == 3:
        pi = piloto.Piloto(conn)
        tabela = "Piloto"
        opcaosub = submenu(tabela)
        limpar() 
        while opcaosub != 5:
          if opcaosub == 1: 
            addPi = adicionar(tabela)
          elif opcaosub == 2: 
            pi.consultar_piloto()
          elif opcaosub == 3:
            atuPi = atualizar(tabela)
          elif opcaosub == 4:
            exPi = excluir(tabela)
          else:
            print("{}Opção inválida{}".format(cores["RED"], cores["LIMPA"]))

          limpar()
          opcaosub = submenu(tabela)
          limpar()

#----------CASO A OPÇÃO SEJA MECANICOS---------------------------------------
      elif opcao == 4:
        mec = mecanico.Mecanico(conn)
        tabela = "Mecanico"
        opcaosub = submenu(tabela)
        limpar() 
        while opcaosub != 5:
          if opcaosub == 1:
            addMec = adicionar(tabela)
          elif opcaosub == 2: 
            mec.consultar_mecanico()
          elif opcaosub == 3:
            atuMec = atualizar(tabela)
          elif opcaosub == 4:
            exMec = excluir(tabela)  
          else:
            print("{}Opção inválida{}".format(cores["RED"], cores["LIMPA"]))
            
          limpar()
          opcaosub = submenu(tabela)
          limpar()

#----------CASO A OPÇÃO SEJA CARROS---------------------------------------
      elif opcao == 5:
        car = carro.Carro(conn)
        tabela = "Carro"
        opcaosub = submenu(tabela)
        limpar()
        while opcaosub != 6:
          if opcaosub == 1:
            addCar = adicionar(tabela)
          elif opcaosub == 2: 
            car.consultar_carro()
          elif opcaosub == 3:
            atuCar = atualizar(tabela)
          elif opcaosub == 4:
            exCar = excluir(tabela)  
          elif opcaosub == 5:
            car.comparar_jogosPneu()
          else:
            print("{}Opção inválida{}".format(cores["RED"], cores["LIMPA"]))
            
          limpar() 
          opcaosub = submenu(tabela)
          limpar()  

#----------CASO A OPÇÃO SEJA INVÁLIDA---------------------------------------
      else:
        print("{}Opção inválida{}".format(cores["RED"], cores["LIMPA"]))
             
      limpar()
      opcao = menu()
      limpar()

    print("{}Até mais!{}".format(cores["BLUE"], cores["LIMPA"]))
      
      
      
      





      
        
        
       
      
     
          
        
        
        
        
        
        
        
        
        

        

