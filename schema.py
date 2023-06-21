import sqlite3
from sqlite3 import Error


def criar_banco(corrida):
    # Conexão com o BD
    conn = sqlite3.connect(corrida)
    # Cursor para manipular os dados do BD
    c = conn.cursor()

    try:
        c.execute("""
          CREATE TABLE IF NOT EXISTS "categoria"(
          idCategoria INTEGER NOT NULL,
          nomeCategoria TEXT NOT NULL,
          descricaoCategoria INTEGER NOT NULL,
          PRIMARY KEY("idCategoria" AUTOINCREMENT)
          );
        """)

        c.execute("""
          CREATE TABLE IF NOT EXISTS "escuderia"(
          idEscuderia INTEGER NOT NULL,
          nomeEscuderia TEXT NOT NULL,
          patrocinioEscuderia TEXT NOT NULL,
          vitoriasEscuderia INTEGER NOT NULL,
          categoria_id INTEGER NOT NULL,
          PRIMARY KEY("idEscuderia" AUTOINCREMENT),
          FOREIGN KEY("categoria_id") REFERENCES "categoria"("idCategoria") ON DELETE CASCADE
          );
        """)

        c.execute("""
          CREATE TABLE IF NOT EXISTS "circuito"(
          idCircuito INTEGER NOT NULL,
          nomeCircuito TEXT NOT NULL,
          paisCircuito TEXT NOT NULL,
          descricaoCircuito TEXT NOT NULL,
          categoria_id INTEGER NOT NULL,
          PRIMARY KEY("idCircuito" AUTOINCREMENT),
          FOREIGN KEY("categoria_id") REFERENCES "categoria"("idCategoria") ON DELETE CASCADE
          );
        """)

        c.execute("""
          CREATE TABLE IF NOT EXISTS "piloto"(
          idPiloto INTEGER NOT NULL,
          nomePiloto TEXT NOT NULL,
          idadePiloto INTEGER NOT NULL,
          vitoriasPiloto INTEGER NOT NULL,
          escuderia_id INTEGER NOT NULL,
          PRIMARY KEY("idPiloto" AUTOINCREMENT),
          FOREIGN KEY("escuderia_id") REFERENCES "escuderia"("idEscuderia") ON DELETE CASCADE
          );
        """)

        c.execute("""
          CREATE TABLE IF NOT EXISTS "mecanico"(
          idMecanico INTEGER NOT NULL,
          nomeMecanico TEXT NOT NULL,
          idadeMecanico INTEGER NOT NULL,
          funcaoMecanico TEXT NOT NULL,
          escuderia_id INTEGER NOT NULL,
          PRIMARY KEY("idMecanico" AUTOINCREMENT),
          FOREIGN KEY("escuderia_id") REFERENCES "escuderia"("idEscuderia") ON DELETE CASCADE
          );
        """)

        c.execute("""
          CREATE TABLE IF NOT EXISTS "carro"(
          idCarro INTEGER NOT NULL,
          jogoPneu TEXT NOT NULL,
          velocidadeCarro INTEGER NOT NULL,
          integridadeCarro TEXT NOT NULL,
          piloto_id INTEGER NOT NULL,
          escuderia_id INTEGER NOT NULL,
          PRIMARY KEY("idCarro" AUTOINCREMENT),
          FOREIGN KEY("piloto_id") REFERENCES "piloto"("idPiloto") ON DELETE CASCADE,
          FOREIGN KEY("escuderia_id") REFERENCES "escuderia"("idEscuderia") ON DELETE CASCADE
          );
        """)

        # Criar gatilho para exclusão em cascata da tabela "escuderia" quando a categoria correspondente for excluída
        c.execute("""
          CREATE TRIGGER IF NOT EXISTS delete_escuderia_on_categoria_delete
          AFTER DELETE ON categoria
          FOR EACH ROW
          BEGIN
            DELETE FROM escuderia WHERE categoria_id = OLD.idCategoria;
          END;
        """)

        # Criar gatilho para exclusão em cascata da tabela "circuito" quando a categoria correspondente for excluída
        c.execute("""
          CREATE TRIGGER IF NOT EXISTS delete_circuito_on_categoria_delete
          AFTER DELETE ON categoria
          FOR EACH ROW
          BEGIN
            DELETE FROM circuito WHERE categoria_id = OLD.idCategoria;
          END;
        """)

        # Criar gatilho para exclusão em cascata da tabela "piloto" quando a escuderia correspondente for excluída
        c.execute("""
          CREATE TRIGGER IF NOT EXISTS delete_piloto_on_escuderia_delete
          AFTER DELETE ON escuderia
          FOR EACH ROW
          BEGIN
            DELETE FROM piloto WHERE escuderia_id = OLD.idEscuderia;
          END;
        """)

        # Criar gatilho para exclusão em cascata da tabela "mecanico" quando a escuderia correspondente for excluída
        c.execute("""
          CREATE TRIGGER IF NOT EXISTS delete_mecanico_on_escuderia_delete
          AFTER DELETE ON escuderia
          FOR EACH ROW
          BEGIN
            DELETE FROM mecanico WHERE escuderia_id = OLD.idEscuderia;
          END;
        """)

        # Criar gatilho para exclusão em cascata da tabela "carro" quando o piloto correspondente for excluído
        c.execute("""
          CREATE TRIGGER IF NOT EXISTS delete_carro_on_piloto_delete
          AFTER DELETE ON piloto
          FOR EACH ROW
          BEGIN
            DELETE FROM carro WHERE piloto_id = OLD.idPiloto;
          END;
        """)

        print("\n🏁-VAMOS LÁ!-🏁")
        return conn

    except Error as e:
        print(e)
