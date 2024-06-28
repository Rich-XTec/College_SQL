/* Lógico_1: */

CREATE TABLE Departamento (
    Cod_Dep serial PRIMARY KEY,
    Nome_Dep name NOT NULL,
);

alter table Departamento add constraint Nome_Dep unique (Nome_Dep);

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
    Cod_Prof serial PRIMARY KEY,
    fk_Cod_Dep int,
    Nome_Prof name NOT NULL,
    Sobrenome_Prof name NOT NULL,
    Status Boolean NOT NULL,
	Unique( Nome_Prof, Sobrenome_Prof)
);

CREATE TABLE Disciplina (
    Cod_Discp serial PRIMARY KEY,
    fk_Cod_Dep int NOT NULL,
    Nome_Discp name NOT NULL,
    Carga_Horaria NUMERIC NOT NULL,
    Descricao text,
    Pre_Requisito int NULL,
    Num_Alunos int NOT NULL,
Unique(Nome_Discp)
);

CREATE TABLE Curso (
    Cod_Curso serial PRIMARY KEY,
    fk_Cod_Dep int,
    Nome_Curso varchar NOT NULL,
Unique(Nome_Curso)
);

CREATE TABLE Turma (
    Cod_Turma serial PRIMARY KEY,
    fk_Cod_Curso int NOT NULL,
    Num_Alunos int,
    Data_Inicio TIMESTAMP NOT NULL,
    Data_Fim TIMESTAMP NOT NULL,
    Periodo varchar,
Unique(fk_Cod_Curso, Data_Inicio, Periodo)
);

CREATE TABLE Aluno (
    RA serial PRIMARY KEY,
    fk_Cod_Curso int NOT NULL,
    Nome_Aluno name NOT NULL,
    Sobrenome_Aluno name NOT NULL,
    CPF bigint NOT NULL,
    Status Boolean NOT NULL,
    Sexo char,
    Nome_Pai name NOT NULL,
    Nome_Mae name NOT NULL,
Unique(CPF),
Unique(Nome_Aluno,Sobrenome_Aluno)
);

CREATE TABLE Contato (
    Cod_Contato serial PRIMARY KEY,
    Tipo_Contato VARCHAR NOT NULL,
Unique(Tipo_Contato)
);

CREATE TABLE Prof_Disciplina (
    fk_Professor_Cod_Prof int NOT NULL,
    fk_Disciplina_Cod_Discp int NOT NULL,
    PRIMARY KEY (fk_Professor_Cod_Prof, fk_Disciplina_Cod_Discp)
);

CREATE TABLE Curso_Disciplina (
    fk_Disciplina_Cod_Discp int NOT NULL,
    fk_Curso_Cod_Curso int NOT NULL,
    PRIMARY KEY (fk_Disciplina_Cod_Discp, fk_Curso_Cod_Curso)
);

CREATE TABLE Aluno_Turma (
    fk_Aluno_RA int NOT NULL,
    fk_Turma_Cod_Turma int NOT NULL,
    PRIMARY KEY (fk_Turma_Cod_Turma, fk_Aluno_RA)
);

CREATE TABLE Aluno_Disciplina (
    fk_Aluno_RA int NOT NULL,
    fk_Disciplina_Cod_Discp int NOT NULL
);

CREATE TABLE Historico (
    Cod_Historico serial PRIMARY KEY,
    fk_aluno_ra int NOT NULL,
    Data_Inicio TIMESTAMP NOT NULL,
    Data_Fim TIMESTAMP
);

CREATE TABLE Historico_Disciplina (
    fk_Disciplina_Cod_Discp int,
    fk_Cod_Historico int,
    Frequencia NUMERIC,
    Nota NUMERIC
);

CREATE TABLE Contato_Aluno (
    fk_Aluno_RA int,
    fk_Cod_Contato int,
    Inf_Contato text NOT NULL,
 PRIMARY KEY (fk_Aluno_RA, fk_Cod_Contato),
Unique(Inf_Contato)
);

CREATE TABLE Tipo_Logradouro (
    Cod_Tipo_Logradouro smallserial PRIMARY KEY,    
    Tipo_Logradouro VARCHAR    
);

CREATE TABLE Endereco_Aluno (
    Cod_Endereco_Aluno serial PRIMARY KEY,
    fk_Cod_Tipo_Logradouro int NOT NULL,
    fk_Aluno_RA int NOT NULL,
    CEP int NOT NULL,
    Rua VARCHAR NOT NULL,
    Numero int NOT NULL,
    Complemento VARCHAR
);
 
ALTER TABLE Professor ADD CONSTRAINT FK_Professor_1
    FOREIGN KEY (fk_Cod_Dep)
    REFERENCES Departamento (Cod_Dep)
    ON DELETE RESTRICT;

ALTER TABLE Disciplina ADD CONSTRAINT FK_Disciplina_1
    FOREIGN KEY (Pre_Requisito)
    REFERENCES Disciplina (Cod_Discp)
    ON DELETE RESTRICT;

ALTER TABLE Disciplina ADD CONSTRAINT FK_Disciplina_2
    FOREIGN KEY (fk_Cod_Dep)
    REFERENCES Departamento (Cod_Dep)
    ON DELETE RESTRICT;
 
ALTER TABLE Curso ADD CONSTRAINT FK_Curso_1
    FOREIGN KEY (fk_Cod_Dep)
    REFERENCES Departamento (Cod_Dep)
    ON DELETE RESTRICT;
 
ALTER TABLE Turma ADD CONSTRAINT FK_Turma_1
    FOREIGN KEY (fk_Cod_Curso)
    REFERENCES Curso (Cod_Curso)
    ON DELETE CASCADE;
 
ALTER TABLE Aluno ADD CONSTRAINT FK_Aluno_1
    FOREIGN KEY (fk_Cod_Curso)
    REFERENCES Curso (Cod_Curso)
    ON DELETE CASCADE;
 
ALTER TABLE Prof_Disciplina ADD CONSTRAINT FK_Prof_Disciplina_1
    FOREIGN KEY (fk_Professor_Cod_Prof)
    REFERENCES Professor (Cod_Prof)
    ON DELETE RESTRICT;
 
ALTER TABLE Prof_Disciplina ADD CONSTRAINT FK_Prof_Disciplina_2
    FOREIGN KEY (fk_Disciplina_Cod_Discp)
    REFERENCES Disciplina (Cod_Discp)
    ON DELETE SET NULL;
 
ALTER TABLE Curso_Disciplina ADD CONSTRAINT FK_Curso_Disciplina_1
    FOREIGN KEY (fk_Disciplina_Cod_Discp)
    REFERENCES Disciplina (Cod_Discp)
    ON DELETE RESTRICT;
 
ALTER TABLE Curso_Disciplina ADD CONSTRAINT FK_Curso_Disciplina_2
    FOREIGN KEY (fk_Curso_Cod_Curso)
    REFERENCES Curso (Cod_Curso)
    ON DELETE RESTRICT;
 
ALTER TABLE Aluno_Turma ADD CONSTRAINT FK_Aluno_Turma_1
    FOREIGN KEY (fk_Aluno_RA)
    REFERENCES Aluno (RA)
    ON DELETE RESTRICT;
 
ALTER TABLE Aluno_Turma ADD CONSTRAINT FK_Aluno_Turma_2
    FOREIGN KEY (fk_Turma_Cod_Turma)
    REFERENCES Turma (Cod_Turma)
    ON DELETE RESTRICT;
 
ALTER TABLE Aluno_Disciplina ADD CONSTRAINT FK_Aluno_Disciplina_1
    FOREIGN KEY (fk_Aluno_RA)
    REFERENCES Aluno (RA)
    ON DELETE SET NULL;
 
ALTER TABLE Aluno_Disciplina ADD CONSTRAINT FK_Aluno_Disciplina_2
    FOREIGN KEY (fk_Disciplina_Cod_Discp)
    REFERENCES Disciplina (Cod_Discp)
    ON DELETE SET NULL;
 
ALTER TABLE Historico_Disciplina ADD CONSTRAINT FK_Historico_Disciplina_1
    FOREIGN KEY (fk_Disciplina_Cod_Discp)
    REFERENCES Disciplina (Cod_Discp)
    ON DELETE RESTRICT;
 
ALTER TABLE Historico_Disciplina ADD CONSTRAINT FK_Historico_Disciplina_2
    FOREIGN KEY (fk_Cod_Historico)
    REFERENCES Historico (Cod_Historico);
 
ALTER TABLE Contato_Aluno ADD CONSTRAINT FK_Contato_Aluno_1
    FOREIGN KEY (fk_Aluno_RA)
    REFERENCES Aluno (RA)
    ON DELETE RESTRICT;
 
ALTER TABLE Contato_Aluno ADD CONSTRAINT FK_Contato_Aluno_2
    FOREIGN KEY (fk_Cod_Contato)
    REFERENCES Contato (Cod_Contato)
    ON DELETE RESTRICT;
 
ALTER TABLE Endereco_Aluno ADD CONSTRAINT FK_Endereco_Aluno_1
    FOREIGN KEY (fk_Cod_Tipo_Logradouro)
    REFERENCES Tipo_Logradouro (Cod_Tipo_Logradouro)
    ON DELETE RESTRICT;
 
ALTER TABLE Endereco_Aluno ADD CONSTRAINT FK_Endereco_Aluno_2
    FOREIGN KEY (fk_Aluno_RA)
    REFERENCES Aluno (RA)
    ON DELETE RESTRICT;
 
ALTER TABLE Historico ADD CONSTRAINT FK_Historico_1
    FOREIGN KEY (fk_aluno_ra)
    REFERENCES Aluno (RA);