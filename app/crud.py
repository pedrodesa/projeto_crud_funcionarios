import psycopg2


def criar_tabela():
    """
    Cria tabela no postgreSQL.
    """
    conn = psycopg2.connect(
        database = 'meu_bd',
        user = 'meu_usuario',
        host = 'localhost',
        password = 'minha_senha',
        port = 5432
    )

    cur = conn.cursor()

    cur.execute('''CREATE_TABLE IF NOT EXISTS funcionarios (
                   id INTEGER PRIMARY KEY,
                   nome VARCHAR(20) NOT NULL,
                   idade INTEGER,
                   profissao VARCHAR(30) NOT NULL,
                   area VARCHAR(30) NOT NULL);''')
    
    conn.commit()
    cur.close()
    conn.close()

def adicionar_funcionario(nome, idade, profissao, area):
    """
    Adiciona um usuário no banco de dados.
    """
    conn = psycopg2.connect(
        database = 'meu_bd',
        user = 'meu_usuario',
        host = 'localhost',
        password = 'minha_senha',
        port = 5432
    )

    cur = conn.cursor()

    cur.execute('''INSERT INTO funcionarios (nome, idade, profissao, area) VALUES (?, ?, ?, ?)''',
                (nome, idade, profissao, area))
    
    conn.commit()
    conn.close()

def listar_usuarios():
    """
    Lista todos os funcionários registrados no banco de dados.
    """
    conn = psycopg2.connect(
        database = 'meu_bd',
        user = 'meu_usuario',
        host = 'localhost',
        password = 'minha_senha',
        port = 5432
    )

    cur = conn.cursor()
    cur.execute('''SELECT * FROM funcionarios''')
    funcionarios = cur.fetchall()

    for funcionario in funcionarios:
        print(funcionario)

    conn.close()

def atualizar_funcionario(id, nome, idade, profissao, area):
     """
     Atualiza os funcionários no banco de dados.
     """
     conn = psycopg2.connect(
        database = 'meu_bd',
        user = 'meu_usuario',
        host = 'localhost',
        password = 'minha_senha',
        port = 5432
    )
     
     cur = conn.cursor()
     cur.execute('''UPDATE funcionarios SET nome = ?, idade = ?, profissao = ?, area = ? WHERE id = ?''', (nome, idade, profissao, area, id))
     conn.commit()
     conn.close()

def deletar_funcionario(id):
    """
    Deleta funcionário da base de dados.
    """
    conn = psycopg2.connect(
        database = 'meu_bd',
        user = 'meu_usuario',
        host = 'localhost',
        password = 'minha_senha',
        port = 5432
    )

    cur = conn.cursor()
    cur.execute('''DELETE FROM funcionarios WHERE id = ?''', (id,))
    conn.commit()
    conn.close()

def menu():
    """
    Menu da interface.
    """
    print('\n1. Adicionar funcionário')
    print('2. Listar funcionários')
    print('3. Atualizar funcionário')
    print('4. Deletar funcionário')
    print('5. Sair')

