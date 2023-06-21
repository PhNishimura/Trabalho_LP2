class Escuderia:

  import sqlite3

  def __init__(self, conn):
    self.nomeEscuderia = ""
    self.patrocinioEscuderia = ""
    self.vitoriasEscuderia = 0
    self.categoria_id = 0
    self.conn = conn
    self.cursor = self.conn.cursor()

  def escuderia_exists(self, idEscuderia):
    self.cursor.execute("SELECT * FROM escuderia WHERE (idEscuderia) = (?);", (idEscuderia, ))
    resposta = self.cursor.fetchall()
    if len(resposta) == 0 or resposta == "" or resposta == None:
      return False
    else:
      return True

#------------------------------------------------------------------------------------------

  def adicionar_escuderia(self, nameEscuderia, sponsorEscuderia, victoryEscuderia, categoria_id):
    from categoria import Categoria as cate
    
    if cate.categoria_exists(self, categoria_id) == False:
      return print("\n\033[31mA categoria indicada não existe!\033[m")
    else:
      self.cursor.execute("INSERT INTO escuderia (nomeEscuderia, patrocinioEscuderia, vitoriasEscuderia, categoria_id ) VALUES (?, ?, ?, ?);", (nameEscuderia, sponsorEscuderia, victoryEscuderia, categoria_id))
      self.conn.commit()
  
      return print("\n\033[32mEscuderia Adicionada\033[m")

#------------------------------------------------------------------------------------------

  def consultar_escuderia(self):
    from prettytable import PrettyTable
    
    self.cursor.execute("SELECT * FROM escuderia;")
    resultado = self.cursor.fetchall()
    if resultado:
      # Criando a tabela
      tabela = PrettyTable()
      tabela.field_names = ["ID", "Nome", "Patrocínio", "Vitórias", "ID-Categoria"]

      # Adicionando os dados à tabela
      for item in resultado:
        tabela.add_row(item)

      # Exibindo a tabela formatada
      print(tabela)
      print("\n\033[32mConsulta realizada!\033[m")
    else:
      print("Nenhum resultado encontrado.")

    input("Pressione <ENTER> para continuar...")

#------------------------------------------------------------------------------------------

  def atualizar_escuderia(self, idEscuderia, newEscuderia, newSponsorEscuderia, newVictoryEscuderia, newCategoria_id):
    from categoria import Categoria as cate
    
    if self.escuderia_exists(idEscuderia) == False:
      return print("\n\033[31mEscuderia não escontrada!\033[m")
    elif cate.categoria_exists(self, newCategoria_id) == False:
      return print("\n\033[31mA categoria indicada não existe!\033[m")
    else:
      self.cursor.execute("UPDATE escuderia SET (nomeEscuderia) = (?) WHERE (idEscuderia) = (?);", (newEscuderia, idEscuderia))
      self.cursor.execute("UPDATE escuderia SET (patrocinioEscuderia) = (?) WHERE (idEscuderia) = (?);", (newSponsorEscuderia, idEscuderia))
      self.cursor.execute("UPDATE escuderia SET (vitoriasEscuderia) = (?) WHERE (idEscuderia) = (?);", (newVictoryEscuderia, idEscuderia))
      self.cursor.execute("UPDATE escuderia SET (categoria_id) = (?) WHERE (idEscuderia) = (?);", (newCategoria_id, idEscuderia))
      self.conn.commit()

      return print("\033[32mEscuderia Atualizada!\033[m")


#------------------------------------------------------------------------------------------

  def excluir_escuderia(self, idEscuderia):
    if self.escuderia_exists(idEscuderia) == False:
      return print("\n\033[31mEscuderia não escontrada!\033[m")
    else:
      self.conn.execute("DELETE FROM escuderia WHERE (idEscuderia) = (?);", (idEscuderia, ))
      self.conn.commit()

      return print("\033[32mEscuderia Excluída!\033[m")
