class Mecanico:

  import sqlite3

  def __init__(self, conn):
    self.escuderia_id = 0
    self.nomeMecanico = ""
    self.idadeMecanico = 0
    self.funcaoMecanico = ""
    self.conn = conn
    self.cursor = self.conn.cursor()

  def mecanico_exists(self, idMecanico):
    self.cursor.execute("SELECT * FROM mecanico WHERE (idMecanico) = (?);", (idMecanico, ))
    resposta = self.cursor.fetchall()
    if len(resposta) == 0 or resposta == "" or resposta == None:
      return False
    else:
      return True

#-------------------------------------------------------------------------------------

  def adicionar_mecanico(self, escuderia_id, nameMecanico, ageMecanico, functionMecanico):
    from escuderia import Escuderia as escu
    
    if escu.escuderia_exists(self,escuderia_id) == False:
      return print("\n\033[31mA escuderia indicada não existe!\033[m")
    else:
      self.cursor.execute("INSERT INTO mecanico (escuderia_id, nomeMecanico, idadeMecanico, funcaoMecanico) VALUES (?, ?, ?, ?);", (escuderia_id, nameMecanico, ageMecanico, functionMecanico))
      self.conn.commit()
  
      return print("\033[32mMecanico Adicionado!\033[m")

#-------------------------------------------------------------------------------------

  def consultar_mecanico(self):
    from prettytable import PrettyTable
    
    self.cursor.execute("SELECT * FROM mecanico;")
    resultado = self.cursor.fetchall()

    if resultado:
      # Criando a tabela
      tabela = PrettyTable()
      tabela.field_names = ["ID", "Nome", "Idade", "Função", "ID Escuderia"]

      for item in resultado:
        tabela.add_row(item)

      # Exibindo a tabela formatada
      print(tabela)
      print("\n\033[32mConsulta realizada!\033[m")
    else:
      print("Nenhum resultado encontrado.")

    input("Pressione <ENTER> para continuar...")

#-------------------------------------------------------------------------------------

  def atualizar_mecanico(self, idMecanico, newEscuderia_id, newMecanico, newIdadeMecanico, newFuncaoMecanico):
    from escuderia import Escuderia as escu
    
    if self.mecanico_exists(idMecanico) == False:
      return print("\n\033[31mMecanico não encontrado\033[m")
    elif escu.escuderia_exists(self, newEscuderia_id) == False:
      return print("\n\033[31mA escuderia indicada não existe!\033[m")
    else:
      self.cursor.execute("UPDATE mecanico SET (escuderia_id) = (?) WHERE (idMecanico) = (?);", (newEscuderia_id, idMecanico))
      self.cursor.execute("UPDATE mecanico SET (nomeMecanico) = (?) WHERE (idMecanico) = (?);", (newMecanico, idMecanico))
      self.cursor.execute("UPDATE mecanico SET (idadeMecanico) = (?) WHERE (idMecanico) = (?);", (newIdadeMecanico, idMecanico))
      self.cursor.execute("UPDATE mecanico SET (funcaoMecanico) = (?) WHERE (idMecanico) = (?);", (newFuncaoMecanico, idMecanico))
      self.conn.commit()

      return print("\033[32mMecanico Atualizado!\033[m")


#-------------------------------------------------------------------------------------

  def excluir_mecanico(self, idMecanico):
    if self.mecanico_exists(idMecanico) == False:
      return print("\n\033[31mMecanico não econtrado!\033[m")
    else:
      self.cursor.execute("DELETE FROM mecanico WHERE idMecanico = ?;", (idMecanico, ))
      self.conn.commit()

      return print("\033[32mMecanico Excluído!\033[m")
