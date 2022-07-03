# Tese Mestrado - Caracterização de Rocha Digital Utilizando Inteligência Artificial

## Sobre

Este repositório representa o projeto de dissertação desenvolvida no LENEP/CCT/UENF, como parte das exigências para obtenção do título de Mestre em Engenharia de Reservatório e de Exploração. 

O objetivo geral deste trabalho foi desenvolver métodos de inteligência artificial capazes de reconhecer padrões relevantes para a análise das propriedades petrofísicas em imagens de rochas reservatórios.

## Descrição dos Diretórios 

Os arquivos fontes deste trabalho se encontram no diretório `Projeto` e foi desenvolvido utilizando o [Lyx](https://www.lyx.org/Home).

No diretório `imagens` são encontradas todas as imagens utilizadas no trabalho.

No diretório `listagens` estão os códigos fontes dos *softwares* desenvolvidos para a obtenção dos resultados. Esses códigos também podem ser encontrados em seus respectivos repositórios `git`:
    
- [Scrips Python para Treinamento e Aplicação da Rede Neural](https://github.com/hereisjohnny2/project-mestrado)

- [Rock Image Annotation Tool: Aplicação GUI para adicionar *labels* à regiões de interesse em imagens de rochas reservatório](https://github.com/hereisjohnny2/rock-image-annotation)

Nesses diretórios é possível encontrar instruções para execução de local de cada um deles.

Por fim, no diretório `resultados` estão os valores obtidos na aplicação da rede neural sobre às amostras de rocha digital junto com o resultado da binarização de cada um delas.

## ToDo - Ajustes para Versão Final

### Sugestões Prof. Basílio

[] Trazer Fluxograma de **Coleta de Resultado** para inicio

[] Resumo, apresentar as melhorias que o trabalho trouxe

[] Ultrapassar limites de bordas (corrigido na versão final)

[] Inverter capítulos 2 e 3

[] Explicar o que é **Conjunto de Treino**

[] Tirar parte de disciplinas realizadas para o trabalho ter um alcance maior

[] Em 3.3.2 corrigir Algorítimos -> Algoritmos

[] Explicar as flags e comandos utilizados na CLI em python em um apêndice

[] Retirar Figura do `makefile` e mover para apêndice

[] Mover **descrição das classes** para apêndice

[] Quando fala da classe referenciar o diagrama de classes e o código listado no apêndice, assim leitor poderá verificar o que você esta falando

[] Maior destaque para o que foi feito e mover parte do como para apêndices

[] Mostrar Figura do software de **Anotação de Regiões de Interesse** e explicar como funciona

[] Figura 47 (exemplo de arquivo `.ui`) só manter se for explicar o que esta na Figura


### Sugestões Prof. Slava

[] Corrigir idioma, deixar em português

[] Evitar palavras em inglês como em estocástica/stochastic

[] Trocar a expressão "Representada pela letra" por "Representada pela variável" quando uma nova variável for introduzida

[] Rever a citação da Equação 3.1

[] Rever referencia de Jr (2017) na pg. 22, já que **Jr** não é sobrenome

[] Verificar pg molhanteSw

[] Introduzir as Equações imediatamente após falar sobre a mesma no texto. As Equações devem fazer parte do texto e não serem tratadas como Figuras 

[] Colocar dimensões no texto e não diretamente na Equação

[] Ver com **Slava** melhor grafia para *"Um filtro L : S → S é considerado linear se as operações naturais de adição e multiplicação por um escalar de um sinal forem preservadas, ou seja,"*

[] Sempre em maiúsculo: equação -> Equação, figura ->Figura, tabela->Tabela

[] Corrigir a Equação 3.25, removendo o desenvolvimento e deixando apenas a final

[] Cada Equação deve ter uma numeração diferente

[] Corrigir Equação 3.35 (tangente hiperbólica)

[] Na Equação 3.42, definir o operador (*Hadamard*) utilizado pois não é tão comum

[] Na Figura 56, corrigir pra -> PARA

[] Tirar ponto final do título

[] Trocar bibliografia para ABNT2

[] Adicionar um apêndice manual do usuário

[] Índice remissivo padronizar maiúscula/minuscula

### Sugestões Prof. Fernando

[] Em apêndice manual desenvolvedor, que seria diagrama de classes, sequência, descrição das classes e códigos

[] Verificar a fonte da Figura 12

[] Discutir o fato da informação de porosidade variar de acordo com o método experimental aplicado

[] Discutir a heterogeneidade das amostras