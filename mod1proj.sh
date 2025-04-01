#!/bin/bash

# Solicita o nome do aluno
read -p "Nome do Aluno: " nome

# Solicita as notas e converte para números inteiros
read -p "Nota da Prova 1: " nota_prova_1
read -p "Nota da Prova 2: " nota_prova_2
read -p "Nota das Atividades Extras: " nota_atividades

# Calcula a média (usa "bc" para operações com números decimais)
nota_final=$(echo "scale=2; ($nota_prova_1 + $nota_prova_2 + $nota_atividades) / 3" | bc)

# Exibe a nota final
echo "A nota final de $nome é $nota_final"

# Verifica se passou ou não (usa `bc` para comparação)
if (( $(echo "$nota_final >= 7" | bc -l) )); then
    echo "Parabéns, você passou!"
else
    echo "Não foi dessa vez, tente novamente."
fi


