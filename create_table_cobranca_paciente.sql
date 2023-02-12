CREATE TABLE cobranca_paciente(
    id serial PRIMARY KEY,
    definicao VARCHAR(100) NOT NULL,
    identificacao INT NOT NULL,
    nome  VARCHAR(100) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    codigo_postal INT NOT NULL,
    regiao VARCHAR(50) NOT NULL,
    total_cobrancas INT NOT NULL,
    media_custos_cobertos NUMERIC NOT NULL,
    media_pagamento_total NUMERIC NOT NULL,
    media_gastos_cuidados NUMERIC NOT NULL
)