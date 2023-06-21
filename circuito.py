class Circuito:

  import sqlite3

  def __init__(self, conn):
    self.nomeCircuito = ""
    self.paisCircuito = ""
    self.descricaoCircuito = ""
    self.categoria_id = 0
    self.conn = conn
    self.cursor = self.conn.cursor()

  def circuito_exists(self, idCircuito):
    self.cursor.execute("SELECT * FROM circuito WHERE (idCircuito) = (?);", (idCircuito, ))
    resposta = self.cursor.fetchall()
    if len(resposta) == 0 or resposta == "" or resposta == None:
      return False
    else:
      return True

#------------------------------------------------------------------------------------------

  def adicionar_circuito(self, nameCircuito, countryCircuito, descCircuito, categoria_id):
    from categoria import Categoria as cate

    if cate.categoria_exists(self, categoria_id) == False:
      return print("\n\033[31mA categoria indicada não existe!\033[m")
    else:
      self.cursor.execute("INSERT INTO circuito (nomeCircuito, paisCircuito, descricaoCircuito, categoria_id) VALUES (?, ?, ?, ?);", (nameCircuito, countryCircuito, descCircuito, categoria_id))
      self.conn.commit()

      return print("\033[32mCircuito Adicionado!\033[m")

#------------------------------------------------------------------------------------------

  def consultar_circuito(self):
    from prettytable import PrettyTable
    
    self.cursor.execute("SELECT * FROM circuito;")
    resultado = self.cursor.fetchall()

    if resultado:
      # Criando a tabela
      tabela = PrettyTable()
      tabela.field_names = ["ID", "Nome", "País", "Descrição", "ID categoria"]

      # Preenchendo a tabela com os dados da consulta
      for item in resultado:
        tabela.add_row(item)

      # Exibindo a tabela formatada
      print(tabela)
      print("\n\033[32mConsulta realizada!\033[m")
    else:
      print("Nenhum resultado encontrado.")

    input("Pressione <ENTER> para continuar...")

#------------------------------------------------------------------------------------------

  def atualizar_circuito(self, idCircuito, newCircuito, newPaisCircuito, newDescCircuito, newCategoria_id):
    from categoria import Categoria as cate
    
    if self.circuito_exists(idCircuito) == False:
      return print("\n\033[31mCircuito não escontrado!\033[m")
    elif cate.categoria_exists(self, newCategoria_id) == False:
      return print("\n\033[31mA categoria indicada não existe!\033[m")
    else:
      self.cursor.execute("UPDATE circuito SET (nomeCircuito) = (?) WHERE (idCircuito) = (?);", (newCircuito, idCircuito))
      self.cursor.execute("UPDATE circuito SET (paisCircuito) = (?) WHERE (idCircuito) = (?);", (newPaisCircuito, idCircuito))
      self.cursor.execute("UPDATE circuito SET (descricaoCircuito) = (?) WHERE (idCircuito) = (?);", (newDescCircuito, idCircuito))
      self.cursor.execute("UPDATE circuito SET (categoria_id) = (?) WHERE (idCircuito) = (?);", (newCategoria_id, idCircuito))
      self.conn.commit()

      return print("\033[32mCircuito Atualizado!\033[m")


#------------------------------------------------------------------------------------------

  def excluir_circuito(self, idCircuito):
    if self.circuito_exists(idCircuito) == False:
      return print("\n\033[31mCircuito não escontrado!\033[m")
    else:
      self.conn.execute("DELETE FROM circuito WHERE (idCircuito) = (?);", (idCircuito, ))
      self.conn.commit()

      return print("\033[32mCircuito Excluído!\033[m")
