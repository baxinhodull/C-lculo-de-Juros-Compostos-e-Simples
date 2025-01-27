# Calculo-de-Juros-Compostos-e-Simples

Este programa permite calcular o montante final de um investimento utilizando duas fórmulas diferentes: juros compostos e juros simples. O usuário pode inserir o valor do capital, a taxa de juros anual, e o tempo de investimento em meses. O programa calculará o montante final com ambas as abordagens e exibirá o resultado.

Funcionalidades
Juros Compostos: A fórmula para calcular o montante final é:

# 𝑀=𝐶×(1+𝑖)𝑡

Onde:

M é o montante final.

C é o capital inicial.

i é a taxa de juros anual (em decimal).

t é o tempo de investimento em anos.

Juros Simples: A fórmula para calcular o montante final é:


# 𝑀=𝐶×(1+𝑖×𝑡)

Onde:


M é o montante final.

C é o capital inicial.

i é a taxa de juros anual (em decimal).

t é o tempo de investimento em anos.

# Como Rodar o Código
Pré-requisitos: Este código requer Python 3.x instalado no seu computador.

Executando o Código:

Abra um terminal ou prompt de comando.
Navegue até o diretório onde o arquivo Python (juros.py) está localizado.

Execute o comando:

python juros.py

Entrada de Dados:

O programa solicita que você insira:

O capital inicial do investimento.

A taxa de juros anual em porcentagem.

O tempo de investimento em meses.

Saída de Dados:

O programa calculará e exibirá:

O montante final com juros compostos e juros simples.

Os juros acumulados com juros compostos.

Exemplo de Execução:


Qual o capital do investimento? R$ 1000

Qual o juros anual em porcentagem (%)? 10

Quantos meses será o investimento? 24

Montante final com juros compostos após 24 meses: R$ 1219.00

Juros acumulados com juros compostos: R$ 219.00

Montante final com juros simples após 24 meses: R$ 1200.00

Detalhes do Código

Entrada de Dados: O usuário fornece os seguintes dados:

Capital inicial do investimento (R$).

Taxa de juros anual em porcentagem (%).

Tempo de investimento em meses.

Cálculos:

O código realiza dois cálculos: um utilizando juros compostos e outro utilizando juros simples.

Para os juros compostos, o valor final é calculado com a fórmula:
𝑀=𝐶×(1+𝑖)𝑡

 
Para os juros simples, o valor final é calculado com a fórmula:
𝑀=𝐶×(1+𝑖×𝑡)

Exibição dos Resultados:

O código exibe o montante final de ambos os cálculos, além dos juros acumulados com juros compostos.

Tecnologias Usadas

Python 3.x

Biblioteca math (para cálculos exponenciais, usando pow)

Licença

Este projeto é de código aberto. Sinta-se livre para usar, modificar e distribuir conforme desejar.
