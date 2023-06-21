class Categoria:

  import sqlite3

  def __init__(self, conn):
    self.nomeCategoria = ""
    self.descricaoCategoria = ""
    self.conn = conn
    self.cursor = self.conn.cursor()

  def categoria_exists(self, idCategoria):
    self.cursor.execute("SELECT * FROM categoria WHERE (idCategoria) = (?);", (idCategoria, ))
    resposta = self.cursor.fetchall()
    if len(resposta) == 0 or resposta == "" or resposta == None:
      return False
    else:
      return True

#------------------------------------------------------------------------------------------

  def adicionar_categoria(self, nameCategoria, descCategoria):
    self.cursor.execute("INSERT INTO categoria (nomeCategoria, descricaoCategoria) VALUES (?, ?);", (nameCategoria, descCategoria))
    self.conn.commit()

    return print("\033[32mCategoria Adicionada\033[m")

#------------------------------------------------------------------------------------------

  def consultar_categoria(self):
    from prettytable import PrettyTable
    self.cursor.execute("SELECT * FROM categoria;")
    resultado = self.cursor.fetchall()

    if resultado:
      # Criando a tabela
      tabela = PrettyTable()
      tabela.field_names = ["ID", "Nome", "Descrição"]

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

  def atualizar_categoria(self, idCategoria, newCategoria, newDescCategoria):
    if self.categoria_exists(idCategoria) == False:
      return print("\n\033[31mCategoria não escontrada!\033[m")
    else:
      self.cursor.execute("UPDATE categoria SET (nomeCategoria) = (?) WHERE (idCategoria) = (?);", (newCategoria, idCategoria))
      self.cursor.execute("UPDATE categoria SET (descricaoCategoria) = (?) WHERE (idCategoria) = (?);", (newDescCategoria, idCategoria))
      self.conn.commit()

      return print("\033[32mCategoria Atualizada!\033[m")


#------------------------------------------------------------------------------------------

  def excluir_categoria(self, idCategoria):
    if self.categoria_exists(idCategoria) == False:
      return print("\n\033[31mCategoria não escontrada!\033[m")
    else:
      self.conn.execute("DELETE FROM categoria WHERE (idCategoria) = (?);", (idCategoria, ))
      self.conn.commit()

      return print("\033[32mCategoria Excluída!\033[m")
