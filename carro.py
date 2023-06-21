class Carro:

  import sqlite3


  def __init__(self, conn):
    self.escuderia_id = 0
    self.piloto_id = 0
    self.jogoPneu = ""
    self.velocidadeCarro = 0
    self.integridadeCarro = ""
    self.conn = conn
    self.cursor = self.conn.cursor()

  def carro_exists(self, idCarro):
    self.cursor.execute("SELECT * FROM carro WHERE (idCarro) = (?);", (idCarro, ))
    resposta = self.cursor.fetchall()
    if len(resposta) == 0 or resposta == "" or resposta == None:
      return False
    else:
      return True

#-------------------------------------------------------------------------------------

  def piloto_pertence_escuderia(self, piloto_id, escuderia_id):
    self.cursor.execute("SELECT COUNT(*) FROM piloto WHERE idPiloto = (?) AND escuderia_id = (?);", (piloto_id, escuderia_id))
    result = self.cursor.fetchone()

    if result[0] == 1:
      return True
    else:
      return False

  #-------------------------------------------------------------------------------------
  
  def comparar_jogosPneu(self):
    import matplotlib.pyplot as plt
    # Consultar os jogos de pneu usados
    self.cursor.execute("SELECT jogoPneu, COUNT(jogoPneu) as quantidade FROM carro GROUP BY jogoPneu;")
    resultado = self.cursor.fetchall()

    if resultado:
        # Separar os dados em listas separadas
        jogos = [item[0] for item in resultado]
        quantidades = [item[1] for item in resultado]

        # Criar o gráfico de barras
        plt.bar(jogos, quantidades)
        plt.xlabel('Tipo de Pneu')
        plt.ylabel('Quantidade')
        plt.title('Comparação de Jogos de Pneu')
        plt.show()
    else:
        print("Nenhum resultado encontrado.")
  
#-------------------------------------------------------------------------------------

  def adicionar_carro(self, escuderia_id, piloto_id, jPneu, speedCarro, lifeCarro):
    from escuderia import Escuderia as escu
    from piloto import Piloto as pilo

    if escu.escuderia_exists(self,escuderia_id) == False:
      return print("\n\033[31mA escuderia indicada não existe!\033[m")
    elif pilo.piloto_exists(self, piloto_id) == False:
      return print("\n\033[31mO piloto indicado não existe!\033[m")
    elif self.piloto_pertence_escuderia(piloto_id, escuderia_id) == False:
      return print("\n\033[31mO piloto indicado não pertence à escuderia indicada!\033[m")
    else:
      self.cursor.execute("INSERT INTO carro (escuderia_id, piloto_id, jogoPneu, velocidadeCarro, integridadeCarro) VALUES (?, ?, ?, ?, ?);", (escuderia_id, piloto_id, jPneu, speedCarro, lifeCarro))
      self.conn.commit()
      return print("\033[32mCarro Adicionado!\033[m")
    
#-------------------------------------------------------------------------------------

  def consultar_carro(self):
    from prettytable import PrettyTable
    
    self.cursor.execute("SELECT * FROM carro;")
    resultado = self.cursor.fetchall()

    if resultado:
      # Criando a tabela
      tabela = PrettyTable()
      tabela.field_names = ["ID Carro", "Jogo de pneu", "Velocidade", "Integriadade", "ID Piloto", "ID Escuderia"]

      # Adicionando os dados à tabela
      for item in resultado:
        tabela.add_row(item)

      # Exibindo a tabela formatada
      print(tabela)
      print("\n\033[32mConsulta realizada!\033[m")
    else:
      print("Nenhum resultado encontrado.")

    input("Precione <ENTER> para continuar...")

#-------------------------------------------------------------------------------------

  def atualizar_carro(self, idCarro, newEscuderia, newPiloto, jPneu, newSpeedCarro, newLifeCarro):
    from escuderia import Escuderia as escu
    from piloto import Piloto as pilo
    
    if self.carro_exists(idCarro) == False:
      return print("\n\033[31mCarro não escontrado!\033[m")
    elif escu.escuderia_exists(self, newEscuderia) == False:
      return print("\n\033[31mA escuderia indicada não existe!\033[m")
    elif pilo.piloto_exists(self, newPiloto) == False:
      return print("\n\033[31mO piloto indicado não existe!\033[m")  
    elif  self.piloto_pertence_escuderia(newPiloto, newEscuderia) == False:
      return print("\n\033[31mO piloto indicado não pertence à escuderia indicada!\033[m")
    else:
      self.cursor.execute("UPDATE carro SET (escuderia_id) = (?) WHERE (idCarro) = (?);", (newEscuderia, idCarro))
      self.cursor.execute("UPDATE carro SET (piloto_id) = (?) WHERE (idCarro) = (?);", (newPiloto, idCarro))
      self.cursor.execute("UPDATE carro SET (jogoPneu) = (?) WHERE (idCarro) = (?);", (jPneu, idCarro))
      self.cursor.execute("UPDATE carro SET (velocidadeCarro) = (?) WHERE (idCarro) = (?);", (newSpeedCarro, idCarro))
      self.cursor.execute("UPDATE carro SET (integridadeCarro) = (?) WHERE (idCarro) = (?);", (newLifeCarro, idCarro))
      self.conn.commit()

      return print("\033[32mCarro Atualizado!\033[m")


#-------------------------------------------------------------------------------------

  def excluir_carro(self, idCarro):
    if self.carro_exists(idCarro) == False:
      return print("\n\033[31mCarro não econtrado!\033[m")
    else:
      self.conn.execute("DELETE FROM carro WHERE (idCarro) = (?);", (idCarro, ))
      self.conn.commit()

      return print("\033[32mCarro Excluído!\033[m")
