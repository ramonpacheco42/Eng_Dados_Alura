CREATE TABLE pacientes(
    id serial PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    endereco VARCHAR(100) NOT NULL
)