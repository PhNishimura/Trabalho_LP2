class Piloto:

  import sqlite3

  def __init__(self, conn):
    self.escuderia_id = 0
    self.nomePiloto = ""
    self.idadePiloto = 0
    self.vitoriasPiloto = 0
    self.conn = conn
    self.cursor = self.conn.cursor()

  def piloto_exists(self, idPiloto):
    self.cursor.execute("SELECT * FROM piloto WHERE (idPiloto) = (?);", (idPiloto, ))
    resposta = self.cursor.fetchall()
    if len(resposta) == 0 or resposta == "" or resposta == None:
      return False
    else:
      return True

#------------------------------------------------------------------------------------------

  def adicionar_piloto(self, escuderia_id, namePiloto, agePiloto, victoryPiloto):
    from escuderia import Escuderia as escu
    
    if escu.escuderia_exists(self, escuderia_id ) == False:
      return print("\n\033[31mA escuderia indicada não existe!\033[m")
    else:
      self.cursor.execute("INSERT INTO piloto (escuderia_id, nomePiloto, idadePiloto, vitoriasPiloto) VALUES (?, ?, ?, ?);", (escuderia_id, namePiloto, agePiloto, victoryPiloto))
      self.conn.commit()

      return print("\033[32mPiloto adicionado!\033[m")

#------------------------------------------------------------------------------------------

  def consultar_piloto(self):
    from prettytable import PrettyTable
    
    self.cursor.execute("SELECT * FROM piloto;")
    resultado = self.cursor.fetchall()

    if resultado:
      tabela = PrettyTable()
      tabela.field_names = ["ID Piloto", "Nome", "Idade", "Vitorias", "ID Escuderia"]

      for item in resultado:
        tabela.add_row(item)

      print(tabela)
      print("\n\033[32mConsulta realizada!\033[m")
    else:
      print("Nenhum resultado encontrado.")

    input("Pressione <ENTER> para continuar...")

#------------------------------------------------------------------------------------------

  def atualizar_piloto(self, idPiloto, newEscuderia_id, newPiloto, newAgePiloto, newVictoryPiloto):
    from escuderia import Escuderia as escu
    
    if self.piloto_exists(idPiloto) == False:
      return print("\n\033[31mPiloto não escontrado!\033[m")
    elif escu.escuderia_exists(self, newEscuderia_id) == False:
      return print("\n\033[31mA escuderia indicada não existe!\033[m")
    else:
      self.cursor.execute("UPDATE piloto SET (escuderia_id) = (?) WHERE (idPiloto) = (?);", (newEscuderia_id, idPiloto))
      self.cursor.execute("UPDATE piloto SET (nomePiloto) = (?) WHERE (idPiloto) = (?);", (newPiloto, idPiloto))
      self.cursor.execute("UPDATE piloto SET (idadePIloto) = (?) WHERE (idPiloto) = (?);", (newAgePiloto, idPiloto))
      self.cursor.execute("UPDATE piloto SET (vitoriasPiloto) = (?) WHERE (idPiloto) = (?);", (newVictoryPiloto, idPiloto))
      self.conn.commit()

      return print("\033[32mPiloto Atualizado!\033[m")


#------------------------------------------------------------------------------------------

  def excluir_piloto(self, idPiloto):
    if self.piloto_exists(idPiloto) == False:
      return print("\n\033[31mPiloto não econtrado!\033[m")
    else:
      self.conn.execute("DELETE FROM piloto WHERE (idPiloto) = (?);", (idPiloto, ))
      self.conn.commit()

      return print("\033[32mPiloto Excluído!\033[m")
