import os
import psycopg2

try:
    # Parâmetros de conexão
    conn = psycopg2.connect(
        dbname="nome_do_banco",
        user="seu_usuario",
        password="sua_senha",
        host="localhost",
        port="5432"
    )

    print("Conexão estabelecida com sucesso!")

    # Crie um objeto cursor
    cursor = conn.cursor()

    # Execute comandos SQL (exemplo: selecionar dados)
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Versão do PostgreSQL: {db_version}")

    # Feche a conexão
    cursor.close()
    conn.close()

except psycopg2.OperationalError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
