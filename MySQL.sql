
CREATE TABLE Departamento (
    Cod_Dep int PRIMARY KEY AUTO_INCREMENT,
    Nome_Dep varchar(25) NOT NULL,
    Unique(Nome_Dep)
);

CREATE TABLE Tecnico (
 Cod_Tec int PRIMARY KEY AUTO_INCREMENT,
 fk_Cod_Dep int,
 Nome_Tec varchar(50) NOT NULL,
 Area_Formacao varchar(25),
 Data_Inicio TIMESTAMP NOT NULL,
 Salario integer NOT NUL,
 Observacao varchar(100),
FOREIGN KEY(fk_Cod_Dep) REFERENCES Departamento (Cod_Dep) 
);

CREATE TABLE Professor (
    Cod_Prof int PRIMARY KEY AUTO_INCREMENT,
    fk_Cod_Dep int,
    Nome_Prof varchar(25) NOT NULL,
    Sobrenome_Prof varchar(25) NOT NULL,
    Status Boolean NOT NULL,
	Unique( Nome_Prof, Sobrenome_Prof),
    FOREIGN KEY(fk_Cod_Dep) REFERENCES Departamento (Cod_Dep)
);

CREATE TABLE Disciplina (
    Cod_Discp int PRIMARY KEY AUTO_INCREMENT,
    fk_Cod_Dep int NOT NULL,
    Nome_Discp varchar(25) NOT NULL,
    Carga_Horaria NUMERIC NOT NULL,
    Descricao text,
    Pre_Requisito int NULL,
    Num_Alunos int NOT NULL,
Unique(Nome_Discp),
FOREIGN KEY(Pre_Requisito) REFERENCES Disciplina (Cod_Discp),
FOREIGN KEY(fk_Cod_Dep) REFERENCES Departamento (Cod_Dep)
);

CREATE TABLE Curso (
    Cod_Curso int PRIMARY KEY AUTO_INCREMENT,
    fk_Cod_Dep int,
    Nome_Curso varchar(25) NOT NULL,
Unique(Nome_Curso),
FOREIGN KEY(fk_Cod_Dep) REFERENCES Departamento (Cod_Dep)
);

CREATE TABLE Turma (
    Cod_Turma int PRIMARY KEY AUTO_INCREMENT,
    fk_Cod_Curso int NOT NULL,
    Num_Alunos int,
    Data_Inicio TIMESTAMP NOT NULL,
    Data_Fim TIMESTAMP NOT NULL,
    Periodo varchar(25),
Unique(fk_Cod_Curso, Data_Inicio, Periodo),
FOREIGN KEY(fk_Cod_Curso) REFERENCES Curso (Cod_Curso)
);

CREATE TABLE Aluno (
    RA int PRIMARY KEY AUTO_INCREMENT,
    fk_Cod_Curso int NOT NULL,
    Nome_Aluno varchar(25) NOT NULL,
    Sobrenome_Aluno varchar(25) NOT NULL,
    CPF bigint NOT NULL,
    Status Boolean NOT NULL,
    Sexo char,
    Nome_Pai varchar(35) NOT NULL,
    Nome_Mae varchar(35) NOT NULL,
Unique(CPF),
FOREIGN KEY(fk_Cod_Curso) REFERENCES Curso (Cod_Curso)
);

CREATE TABLE Contato (
    Cod_Contato int PRIMARY KEY AUTO_INCREMENT,
    Tipo_Contato varchar(25) NOT NULL,
Unique(Tipo_Contato)
);

CREATE TABLE Prof_Disciplina (
    fk_Professor_Cod_Prof int NOT NULL,
    fk_Disciplina_Cod_Discp int NOT NULL,
PRIMARY KEY(fk_Professor_Cod_Prof, fk_Disciplina_Cod_Discp),
FOREIGN KEY(fk_Professor_Cod_Prof) REFERENCES Professor (Cod_Prof),
FOREIGN KEY(fk_Disciplina_Cod_Discp) REFERENCES Disciplina (Cod_Discp)
);

CREATE TABLE Curso_Disciplina (
    fk_Disciplina_Cod_Discp int NOT NULL,
    fk_Curso_Cod_Curso int NOT NULL,
PRIMARY KEY(fk_Disciplina_Cod_Discp, fk_Curso_Cod_Curso),
FOREIGN KEY(fk_Disciplina_Cod_Discp) REFERENCES Disciplina (Cod_Discp),
FOREIGN KEY(fk_Curso_Cod_Curso) REFERENCES Curso (Cod_Curso)
);

CREATE TABLE Aluno_Turma (
    fk_Aluno_RA int NOT NULL,
    fk_Turma_Cod_Turma int NOT NULL,
PRIMARY KEY(fk_Turma_Cod_Turma, fk_Aluno_RA),
FOREIGN KEY(fk_Aluno_RA) REFERENCES Aluno (RA),
FOREIGN KEY(fk_Turma_Cod_Turma) REFERENCES Turma (Cod_Turma)
);

CREATE TABLE Aluno_Disciplina (
    fk_Aluno_RA int NOT NULL,
    fk_Disciplina_Cod_Discp int NOT NULL,
FOREIGN KEY(fk_Aluno_RA) REFERENCES Aluno (RA),
FOREIGN KEY(fk_Disciplina_Cod_Discp) REFERENCES Disciplina (Cod_Discp)
);

CREATE TABLE Historico (
    Cod_Historico int PRIMARY KEY AUTO_INCREMENT,
    fk_aluno_ra int NOT NULL,
    Data_Inicio TIMESTAMP NOT NULL,
    Data_Fim TIMESTAMP,
FOREIGN KEY(fk_aluno_ra) REFERENCES Aluno (RA)
);

CREATE TABLE Historico_Disciplina (
    fk_Disciplina_Cod_Discp int,
    fk_Cod_Historico int,
    Frequencia NUMERIC,
    Nota NUMERIC,
FOREIGN KEY(fk_Disciplina_Cod_Discp) REFERENCES Disciplina (Cod_Discp),
FOREIGN KEY(fk_Cod_Historico) REFERENCES Historico (Cod_Historico)
);

CREATE TABLE Contato_Aluno (
    fk_Aluno_RA int,
    fk_Cod_Contato int,
    Inf_Contato varchar(50) NOT NULL,
 PRIMARY KEY (fk_Aluno_RA, fk_Cod_Contato),
Unique(Inf_Contato),
FOREIGN KEY(fk_Aluno_RA) REFERENCES Aluno (RA),
FOREIGN KEY(fk_Cod_Contato) REFERENCES Contato (Cod_Contato)
);

CREATE TABLE Tipo_Logradouro (
    Cod_Tipo_Logradouro int PRIMARY KEY AUTO_INCREMENT,    
    Tipo_Logradouro varchar(25) NOT NULL   
);

CREATE TABLE Endereco_Aluno (
    Cod_Endereco_Aluno int PRIMARY KEY AUTO_INCREMENT,
    fk_Cod_Tipo_Logradouro int NOT NULL,
    fk_Aluno_RA int NOT NULL,
    CEP int NOT NULL,
    Rua varchar(25) NOT NULL,
    Numero int NOT NULL,
    Complemento varchar(25),
FOREIGN KEY(fk_Cod_Tipo_Logradouro) REFERENCES Tipo_Logradouro (Cod_Tipo_Logradouro),
FOREIGN KEY(fk_Aluno_RA) REFERENCES Aluno (RA)
);