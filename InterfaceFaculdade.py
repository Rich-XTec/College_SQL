import mysql.connector
from mysql.connector import errorcode

# Variáveis
# Valores para criação de tabelas do Banco de Dados
tables = {'Departamento': (
    """CREATE TABLE `departamento` (
        `cod_dep` integer PRIMARY KEY AUTO_INCREMENT,
        `nome_dep` varchar(25) NOT NULL,
        UNIQUE(`nome_dep`)
        ) ENGINE=InnoDB"""),
    'Tecnico': (
        """CREATE TABLE `tecnico` (
        `cod_tec` integer PRIMARY KEY AUTO_INCREMENT,
        `fk_cod_dep` integer,
        `nome_tec` varchar(50) NOT NULL,
        `area_formacao` varchar(25),
        `data_inicio` TIMESTAMP NOT NULL,
	`salario` integer,
	`observacao` varchar(100),
        FOREIGN KEY(`fk_cod_dep`) REFERENCES `departamento` (`cod_dep`)
        ) ENGINE=InnoDB"""),
    'Professor': (
        """CREATE TABLE `professor` (
        `cod_prof` integer PRIMARY KEY AUTO_INCREMENT,
        `fk_cod_dep` integer,
        `nome_prof` varchar(25) NOT NULL,
        `sobrenome_prof` varchar(25) NOT NULL,
        `status` boolean NOT NULL,
	    UNIQUE( `nome_prof`, `sobrenome_prof`),
        FOREIGN KEY(`fk_cod_dep`) REFERENCES `departamento` (`cod_dep`)
        ) ENGINE=InnoDB"""),
    'Disciplina': (
        """CREATE TABLE `disciplina` (
        `cod_discp` integer PRIMARY KEY AUTO_INCREMENT,
        `fk_cod_dep` integer NOT NULL,
        `nome_discp` varchar(25) NOT NULL,
        `carga_horaria` NUMERIC NOT NULL,
        `descricao` text,
        `pre_requisito` integer NULL,
        `num_alunos` integer NOT NULL,
        UNIQUE(`nome_discp`),
        FOREIGN KEY(`pre_requisito`) REFERENCES `disciplina` (`cod_discp`),
        FOREIGN KEY(`fk_cod_dep`) REFERENCES `departamento` (`cod_dep`)
        ) ENGINE=InnoDB"""),
    'Curso': (
        """CREATE TABLE `curso` (
        `cod_curso` integer PRIMARY KEY AUTO_INCREMENT,
        `fk_cod_dep` integer,
        `nome_curso` varchar(25) NOT NULL,
UNIQUE(`nome_curso`),
FOREIGN KEY(`fk_cod_dep`) REFERENCES `departamento` (`cod_dep`)
        ) ENGINE=InnoDB"""),
    'Turma': (
        """CREATE TABLE `turma` (
        `cod_turma` integer PRIMARY KEY AUTO_INCREMENT,
    `fk_cod_curso` integer NOT NULL,
    `num_alunos` integer,
    `data_inicio` TIMESTAMP NOT NULL,
    `data_fim` TIMESTAMP NOT NULL,
    `periodo` varchar(25),
UNIQUE(`fk_cod_curso`, `data_inicio`, `periodo`),
FOREIGN KEY(`fk_cod_curso`) REFERENCES `curso` (`cod_curso`)
        ) ENGINE=InnoDB"""),
    'Aluno': (
        """CREATE TABLE `aluno` (
        `ra` integer PRIMARY KEY AUTO_INCREMENT,
    `fk_cod_curso` integer NOT NULL,
    `nome_aluno` varchar(25) NOT NULL,
    `sobrenome_aluno` varchar(25) NOT NULL,
    `cpf` bigint NOT NULL,
    `status` boolean NOT NULL,
    `sexo` char,
    `nome_pai` varchar(35) NOT NULL,
    `nome_mae` varchar(35) NOT NULL,
UNIQUE(`cpf`),
FOREIGN KEY(`fk_cod_curso`) REFERENCES `curso` (`cod_curso`)
        ) ENGINE=InnoDB"""),
    'Contato': (
        """CREATE TABLE `contato` (
         `cod_contato` integer PRIMARY KEY AUTO_INCREMENT,
    `tipo_contato` varchar(25) NOT NULL,
UNIQUE(`tipo_contato`)
        ) ENGINE=InnoDB"""),
    'Prof_Disciplina': (
        """CREATE TABLE `prof_disciplina` (
        `fk_professor_cod_prof` integer NOT NULL,
    `fk_disciplina_cod_discp` integer NOT NULL,
PRIMARY KEY(`fk_professor_cod_prof`, `fk_disciplina_cod_discp`),
FOREIGN KEY(`fk_professor_cod_prof`) REFERENCES `professor` (`cod_prof`),
FOREIGN KEY(`fk_disciplina_cod_discp`) REFERENCES `disciplina` (`cod_discp`)
        ) ENGINE=InnoDB"""),
    'Curso_Disciplina': (
        """CREATE TABLE `curso_disciplina` (
        `fk_disciplina_cod_discp` integer NOT NULL,
    `fk_curso_cod_curso` integer NOT NULL,
PRIMARY KEY(`fk_disciplina_cod_discp`, `fk_curso_cod_curso`),
FOREIGN KEY(`fk_disciplina_cod_discp`) REFERENCES `disciplina` (`cod_discp`),
FOREIGN KEY(`fk_curso_cod_curso`) REFERENCES `curso` (`cod_curso`)
        ) ENGINE=InnoDB"""),
    'Aluno_Turma': (
        """CREATE TABLE `aluno_turma` (
        `fk_aluno_ra` integer NOT NULL,
    `fk_turma_cod_turma` integer NOT NULL,
PRIMARY KEY(`fk_turma_cod_turma`, `fk_aluno_ra`),
FOREIGN KEY(`fk_aluno_ra`) REFERENCES `aluno` (`ra`),
FOREIGN KEY(`fk_turma_cod_turma`) REFERENCES `turma` (`cod_turma`)
        ) ENGINE=InnoDB"""),
    'Aluno_Disciplina': (
        """CREATE TABLE `aluno_disciplina` (
        `fk_aluno_ra` integer NOT NULL,
    `fk_disciplina_cod_discp` integer NOT NULL,
FOREIGN KEY(`fk_aluno_ra`) REFERENCES `aluno` (`ra`),
FOREIGN KEY(`fk_disciplina_cod_discp`) REFERENCES `disciplina` (`cod_discp`)
        ) ENGINE=InnoDB"""),
    'Historico': (
        """CREATE TABLE `historico` (
        `cod_historico` integer PRIMARY KEY AUTO_INCREMENT,
    `fk_aluno_ra` integer NOT NULL,
    `data_inicio` TIMESTAMP NOT NULL,
    `data_fim` TIMESTAMP,
FOREIGN KEY(`fk_aluno_ra`) REFERENCES `aluno` (`ra`)
        ) ENGINE=InnoDB"""),
    'Historico_Disciplina': (
        """CREATE TABLE `historico_disciplina` (
        `fk_disciplina_cod_discp` integer,
    `fk_cod_historico` integer,
    `frequencia` NUMERIC,
    `nota` NUMERIC,
FOREIGN KEY(`fk_disciplina_cod_discp`) REFERENCES `disciplina` (`cod_discp`),
FOREIGN KEY(`fk_cod_historico`) REFERENCES `historico` (`cod_historico`)
        ) ENGINE=InnoDB"""),
    'Contato_Aluno': (
        """CREATE TABLE `contato_aluno` (
        `fk_aluno_ra` integer,
    `fk_cod_contato` integer,
    `inf_contato` varchar(50) NOT NULL,
 PRIMARY KEY (`fk_aluno_ra`, `fk_cod_contato`),
UNIQUE(`inf_contato`),
FOREIGN KEY(`fk_aluno_ra`) REFERENCES `aluno` (`ra`),
FOREIGN KEY(`fk_cod_contato`) REFERENCES `contato` (`cod_contato`)
        ) ENGINE=InnoDB"""),
    'Tipo_Logradouro': (
        """CREATE TABLE `tipo_logradouro` (
         `cod_tipo_logradouro` integer PRIMARY KEY AUTO_INCREMENT,    
    `tipo_logradouro` varchar(25) NOT NULL    
        ) ENGINE=InnoDB"""),
    'Endereco_Aluno': (
        """CREATE TABLE `endereco_aluno` (
        `cod_endereco_aluno` integer PRIMARY KEY AUTO_INCREMENT,
    `fk_cod_tipo_logradouro` integer NOT NULL,
    `fk_aluno_ra` integer NOT NULL,
    `cep` integer NOT NULL,
    `rua` varchar(25) NOT NULL,
    `numero` integer NOT NULL,
    `complemento` varchar(25),
FOREIGN KEY(`fk_cod_tipo_logradouro`) REFERENCES `tipo_logradouro` (`cod_tipo_logradouro`),
FOREIGN KEY(`fk_aluno_ra`) REFERENCES `aluno` (`ra`)
        ) ENGINE=InnoDB"""),
}

# Valores para serem inseridos no Banco de Dados
inserts = {'Departamento': (
    """insert into departamento (nome_dep) values 
        ('Ciencias Humanas'),
        ('Matematica'),
        ('Biologicas'),
        ('Computacao')"""),
    'Tecnico': (
        """insert into tecnico (fk_cod_dep, nome_tec, area_formacao, data_inicio, salario, observacao) values
        (1, 'Mario Bro', 'Hidraulica', '2022-03-15', 1500, NULL),
        (2, 'Duarte Dutra', 'Programação', '2022-03-15', 3000, 'Demitido'),
	(3, 'Luigo Bro', 'Hidraulica', '2022-03-15', 1500, 'Esforçado')"""),
    'Professor': (
        """insert into professor (fk_cod_dep, nome_prof, sobrenome_prof, status) values
        (2, 'Fabio', 'Faroldo', '1'),
        (1, 'Mingau', 'Cinza', '1'),
        (3, 'Monica', 'Barroso', '0')"""),
    'Curso': (
        """insert into curso (fk_cod_dep, nome_curso) values
        (2, 'Matemática'),
        (1, 'Psicologia'),
        (2, 'Análise de Sistemas'),
        (3, 'Biologia'),
        (1, 'História'),
        (4, 'Engenharia')"""),
    'Turma': (
        """insert into turma (fk_cod_curso, num_alunos, data_inicio, data_fim, periodo) values 
        (2, 20,'2016-05-12', '2017-10-15','Matutino'),
(1, 10, '2014-05-12', '2020-03-05', 'Vespertino'),
(3, 15, '2012-05-12', '2014-05-10', 'Noturno')"""),
    'Disciplina': (
        """insert into disciplina (fk_cod_dep, nome_discp, carga_horaria, descricao, pre_requisito, num_alunos) values 
        (3,'Introducao a Biologia', 1200, 'Apresentar conceitos gerais das Ciencias Biologicas', NULL, 50),
(1,'Psicologia Cognitiva', 1400, 'Entender o funcionamento do aprendizado', NULL, 30),
(4,'Programação em C', 1200, 'Aprender uma linguagem de programação', NULL, 20),
(2,'Calculo', 300, 'Fundamentos do calculo', NULL, 30),
(4,'Programação em C++', 1500, 'Aprender a linguagem de programação C++ com arduino', 3 , 30)"""),
    'Contato': (
        """insert into contato (tipo_contato) values
        ('Telefone'),
('Email'),
('Whatsapp')"""),
    'Aluno': (
        """insert into aluno (fk_cod_curso, nome_aluno, sobrenome_aluno, cpf, status, sexo, nome_pai, nome_mae) values
        (3, 'Marcos', 'Aurelio Martins', 14278914536, '1', 'M', 'Marcio Aurelio', 'Maria Aparecida'),
(1, 'Gabriel', 'Fernando de Almeida', 14470954536, '1', 'M', 'Adão Almeida', 'Fernanda Almeida'),
(3, 'Beatriz', 'Sonia Meneguel', 1520984537, '1', 'F', 'Samuel Meneguel', 'Gabriella Meneguel'),
(4, 'Jorge', 'Soares', 14223651562, '1', 'M', 'João Soares', 'Maria Richter'),
(5, 'Ana Paula', 'Ferretti', 32968914522, '1', 'F', 'Marcio Ferretti', 'Ana Hoffbahn'),
(6, 'Mônica', 'Yamaguti', 32988914510, '1', 'F', 'Wilson Oliveira', 'Fernanda Yamaguti')"""),
    'Aluno_Turma': (
        """insert into aluno_turma (fk_aluno_ra, fk_turma_cod_turma) values
        (3, 1),
(1, 2),
(2, 3),
(4, 3),
(6, 2),
(5, 1)"""),
    'Aluno_Disciplina': (
        """insert into aluno_disciplina (fk_aluno_ra, fk_disciplina_cod_discp) values
        (3, 1),
(1, 2),
(2, 3),
(4, 3),
(5, 4),
(6, 1)"""),
    'Curso_Disciplina': (
        """insert into curso_disciplina (fk_disciplina_cod_discp, fk_curso_cod_curso) values
        (1, 1),
(2, 2),
(3, 3),	
(4, 6)"""),
    'Prof_Disciplina': (
        """insert into prof_disciplina (fk_professor_cod_prof, fk_disciplina_cod_discp) values
        (2, 2),
(1, 1),
(3, 3),
(2, 4)"""),
    'historico': (
        """insert into historico (fk_aluno_ra, data_inicio, data_fim) values
        (2, '2016-05-12', '2017-10-15'),
(3, '2014-05-12', '2020-03-05'),
(1, '2010-05-12', '2012-05-10')"""),
    'historico_disciplina': (
        """insert into historico_disciplina (fk_disciplina_cod_discp, fk_cod_historico, frequencia, nota) values
        (2, 1, 75, 8),
(1, 2, 100, 10),
(4, 2, 50, 0),
(3, 3, 80, 9)"""),
    'contato_aluno': (
        """insert into contato_aluno (fk_aluno_ra, fk_cod_contato, inf_contato) values
        (1, 2, 'marcosaurelio@gmail.com'),
(1, 1, 48946231249),
(2, 1, 48941741247),
(2, 2, 'gabrielalmeida@yahoo.com'),
(3, 1,  945781412),
(3, 2, 'batrizmene@hotmail.com'),
(4, 3, 41999575022),
(4, 2, 'jorgesoares@gmail.com'),
(5, 1, 41974267423),
(5, 2, 'anapaulaferretti@hotmail.com'),
(6, 2, 'monyamaguti@outlook.com')"""),
    'Tipo_Logradouro': (
        """insert into tipo_logradouro (tipo_logradouro) values
        ('Rua'),
('Avenida'),
('Alameda'),
('Travessa')"""),
    'endereco_aluno': (
        """insert into endereco_aluno (fk_cod_tipo_logradouro, fk_aluno_ra, cep, rua, numero, complemento) values
        (2, 1,02854000, 'das Giestas', 255, 'Casa 02'),
(3, 2,02945000, 'Lorena', 10, 'Apto 15'),
(2, 3,00851040, 'do Cursino', 1248, ''),
(1, 4,03563142, 'das Heras', 495, ''),
(2, 5,04523963, 'Santos', 1856, ''),
(4, 6,04213650, 'Matão', 206, '')""")
}

# Valores para deletar as tabelas
drop = {'Endereco_Aluno': (
    "drop table endereco_aluno"),
    'Tipo_Logradouro': (
        "drop table tipo_logradouro"),
    'Contato_Aluno': (
        "drop table contato_aluno"),
    'Historico_Disciplina': (
        "drop table historico_disciplina"),
    'Historico': (
        "drop table historico"),
    'Prof_Disciplina': (
        "drop table prof_disciplina"),
    'Curso_Disciplina': (
        "drop table curso_disciplina"),
    'Aluno_Disciplina': (
        "drop table aluno_disciplina"),
    'Aluno_Turma': (
        "drop table aluno_turma"),
    'Aluno': (
        "drop table aluno"),
    'Disciplina': (
        "drop table disciplina"),
    'Turma': (
        "drop table turma"),
    'Curso': (
        "drop table curso"),
    'Professor': (
        "drop table professor"),
    'Contato': (
        "drop table contato"),
    'Tecnico': (
        "drop table tecnico"),
    'Departamento': (
        "drop table departamento")
}

# Valores para teste de update
update = {'Contato_Aluno': (
    """update contato_aluno
        SET fk_cod_contato = 3
        where fk_cod_contato = 1"""),
    'Disciplina': (
        """update disciplina
        SET pre_requisito = 4
        where cod_discp = 3"""),
    'Aluno_Disciplina': (
        """update aluno_disciplina 
        SET fk_disciplina_cod_discp = 5
        where fk_aluno_ra = 6 """),
    'Endereco_Aluno': (
        """update endereco_aluno
        SET complemento = 2
        where fk_aluno_ra = 5"""),
}

# Valores para teste de delete
delete = {'Aluno_Disciplina': (
    """delete from aluno_disciplina
        where fk_disciplina_cod_discp = 1 or fk_disciplina_cod_discp = 2"""),
    'Prof_Disciplina': (
        """delete from prof_disciplina
        where fk_disciplina_cod_discp = 1 or fk_disciplina_cod_discp = 2"""),
    'Curso_Disciplina': (
        """delete from curso_disciplina
        where fk_disciplina_cod_discp = 1 or fk_disciplina_cod_discp = 2""")
}


# Funções
def connect_bdfinal():
    cnx = mysql.connector.connect(host='localhost', database='bd_final_ufsc', user='root', password='123asd')
    if cnx.is_connected():
        db_info = cnx.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = cnx.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)
        cursor.close()
    return cnx


def drop_all_tables(connect):
    print("\n---DROP DB---")
    # Esvazia o Banco de Dados
    cursor = connect.cursor()
    for drop_name in drop:
        drop_description = drop[drop_name]
        try:
            print("Deletando {}: ".format(drop_name), end='')
            cursor.execute(drop_description)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("OK")
    connect.commit()
    cursor.close()


def create_all_tables(connect):
    print("\n---CREATE ALL TABLES---")
    # Criação das tabelas
    cursor = connect.cursor()
    for table_name in tables:
        table_description = tables[table_name]
        try:
            print("Criando tabela {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Tabela já existe.")
            else:
                print(err.msg)
        else:
            print("OK")
    connect.commit()
    cursor.close()


def show_table(connect):
    print("\n---SELECIONAR TABELA---")
    # Criação das tabelas
    cursor = connect.cursor()
    for table_name in tables:
        print("Nome: {}".format(table_name))
    try:
        name = input(str("\nDigite o nome da tabela que deseja consultar-> ")).upper()
        select = "select * from " + name
        cursor.execute(select)
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("TABELA {}".format(name))
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    cursor.close()


def update_value(connect):
    print("\n---SELECIONAR TABELA PARA ATUALIZAÇÃO---")
    # Criação das tabelas
    cursor = connect.cursor()
    for table_name in tables:
        print("Nome: {}".format(table_name))
    try:
        name = input(str("\nDigite o nome da tabela que deseja consultar-> ")).upper()
        for table_name in tables:
            table_description = tables[table_name]
            if table_name == name:
                print("Para criar a tabela: {}, foi utilizado o seguinte código {}".format(table_name,
                                                                                           table_description))
        coluna = input("Digite a coluna a ser alterada: ")
        valor = input("Digite o valor a ser atribuido: ")
        codigo_f = input("Digite a variavel primaria: ")
        codigo = input("Digite o codigo numerico: ")
        query = ['UPDATE ', name, ' SET ', coluna, ' = ', valor, ' WHERE ', codigo_f, '= ', codigo]
        sql = ''.join(query)
        cursor.execute(sql)
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("Coluna atualizada")
    connect.commit()
    cursor.close()


def insert_test(connect):
    print("\n---INSERT TEST---")
    # Inesrsão dos valores nas tabelas
    cursor = connect.cursor()
    for insert_name in inserts:
        insert_description = inserts[insert_name]
        try:
            print("Inserindo valores para {}: ".format(insert_name), end='')
            cursor.execute(insert_description)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("OK")
    connect.commit()
    cursor.close()


def update_test(connect):
    print("\n---UPDATE TEST---")
    # Inesrsão dos valores nas tabelas
    cursor = connect.cursor()
    for update_name in update:
        update_description = update[update_name]
        try:
            print("Teste de atualização de valores para {}: ".format(update_name), end='')
            cursor.execute(update_description)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("OK")
    connect.commit()
    cursor.close()


def delete_test(connect):
    print("\n---DELETE TEST---")
    # Inesrsão dos valores nas tabelas
    cursor = connect.cursor()
    for delete_name in delete:
        delete_description = delete[delete_name]
        try:
            print("Teste de atualização de valores para {}: ".format(delete_name), end='')
            cursor.execute(delete_description)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("OK")
    connect.commit()
    cursor.close()


def consulta1(connect):
    select_query = """
    select  aluno.ra, aluno.nome_aluno, count(hd.fk_disciplina_cod_discp) as Disciplinas_Concluidas, avg(hd.nota) as IAA, avg(hd.frequencia) as Freq_Media
from aluno, historico as h, historico_disciplina as hd, disciplina as d
where aluno.ra = h.fk_aluno_ra and h.cod_historico = hd.fk_cod_historico and hd.fk_disciplina_cod_discp = d.cod_discp
group by aluno.ra, aluno.nome_aluno
having avg(hd.frequencia)>=75 and avg(hd.nota)>=6;
    """
    print("Primeira Consulta: Mostrar o RA do aluno, seu nome,a data de inicio do historico, a quantidade de disciplinas concluidas,"
	  "a media das notas,IAA, e a frequencia média do historico dos alunos."
	  "Considerar somente as notas e frequencias no minimo suficientes para aprovação dos alunos.")
    cursor = connect.cursor()
    cursor.execute(select_query)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


def consulta2(connect):
    select_query = """
    select  d.cod_discp, d.nome_discp ,count(ad.fk_aluno_ra), de.nome_dep, d.pre_requisito
from aluno_disciplina as ad, disciplina as d, departamento as de
where ad.fk_disciplina_cod_discp = d.cod_discp and de.cod_dep = d.fk_cod_dep
group by d.cod_discp, d.nome_discp, de.nome_dep
    """
    print("\nSegunda Consulta: Mostrar o codigo da disciplina, o nome e a quantidade de alunos por disciplina com os departamentos e pré-requisitos.")
    cursor = connect.cursor()
    cursor.execute(select_query)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


def consulta3(connect):
    select_query = """
    select distinct ca.fk_cod_contato, c.tipo_contato , count(ca.fk_aluno_ra) as soma
from contato_aluno as ca , contato as c
where ca.fk_cod_contato = c.cod_contato
group by ca.fk_cod_contato, c.tipo_contato
order by soma desc
    """
    print("\nTerceira Consulta: Mostrar o codigo do contato, o tipo de contato e a quantidade de alunos que utilizaram cada tipo de contato em seu cadastro.")
    cursor = connect.cursor()
    cursor.execute(select_query)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


def consulta_extra(connect):
    select_query = """
    select  aluno.ra, aluno.nome_aluno, count(hd.fk_disciplina_cod_discp) as Disciplinas_Concluidas, avg(hd.nota) as IAA
from aluno, historico as h, historico_disciplina as hd
where aluno.ra = 2 and aluno.ra = h.fk_aluno_ra and h.cod_historico = hd.fk_cod_historico
group by aluno.ra, aluno.nome_aluno
    """
    print("\nConsulta Extra: Mostrar a quantidade de disciplinas concluidas no historico do aluno ra=2 e a media das notas,IAA.")
    cursor = connect.cursor()
    cursor.execute(select_query)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


def exit_db(connect):
    print("\n---EXIT DB---")
    connect.close()
    print("Conexão ao MySQL encerrada")


def crud_bdfinal(connect):
    drop_all_tables(connect)
    create_all_tables(connect)
    insert_test(connect)

    print("\n---CONSULTAS BEFORE---")
    consulta1(connect)
    consulta2(connect)
    consulta3(connect)
    consulta_extra(connect)

    update_test(connect)
    delete_test(connect)

    print("\n---CONSULTAS AFTER---")
    consulta1(connect)
    consulta2(connect)
    consulta3(connect)
    consulta_extra(connect)


# Main
try:
    # Estabelece Conexão com o DB
    con = connect_bdfinal()

    power_up = 1
    while power_up == 1:
        interface = """\n       ---MENU---
        1.  CRUD bdfinal
        2.  TEST - Create all tables
        3.  TEST - Insert all values
        4.  TEST - Update
        5.  TEST - Delete
        6.  CONSULTA 01
        7.  CONSULTA 02
        8.  CONSULTA 03
        9.  CONSULTA EXTRA
        10. Show Table
        11. Update Value
        12. CLEAR ALL bdfinal
        0.  Disconnect DB\n """
        print(interface)

        choice = int(input("Opção: "))
        if choice < 0 or choice > 12:
            print("Erro tente novamente")
            choice = int(input())

        if choice == 0:
            if con.is_connected():
                exit_db(con)
                print("Muito obrigado.")
                break
            else:
                break

        if choice == 1:
            crud_bdfinal(con)

        if choice == 2:
            create_all_tables(con)

        if choice == 3:
            insert_test(con)

        if choice == 4:
            update_test(con)

        if choice == 5:
            delete_test(con)

        if choice == 6:
            consulta1(con)

        if choice == 7:
            consulta2(con)

        if choice == 8:
            consulta3(con)

        if choice == 9:
            consulta_extra(con)

        if choice == 10:
            show_table(con)

        if choice == 11:
            update_value(con)

        if choice == 12:
            drop_all_tables(con)

except mysql.connector.Error as err:
    print("Erro na conexão com o sqlite", err.msg)
