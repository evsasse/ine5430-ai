# Trabalho 1 - Jogo de palitos

Aluno: Evandro Sasse - 13100743

## Andamento do jogo

- O jogo é dividido em rodadas.
  Cada rodada pode ou não ter um vencedor da rodada.

- Se um jogador vence a rodada ele perde um palito.
  O primeiro jogador a perder todos os palitos vence o jogo.
  
## Como funciona uma rodada
  
1. Uma rodada começa com cada jogador segurando, secretamente, um número de palitos.
   Caso seja a primeira rodada, cada jogador segura pelo menos 1 palito.
   Os jogadores utilizarão de sua própria quantidade segurada, e o número mínimo, para tomar decisões de aposta nessa rodada.
   
2. Os jogadores fazem apostas um após o outro, de quantos palitos foram segurados no total.
   Os jogadores usam das apostas feitas anteriormente nessa mesma rodada para tomar decisões de aposta nessa rodada.

3. a. Caso um jogador acerte o número total, ele é o vencedor da rodada e perde um palito.
   Caso ele só tivesse um palito, ele vence o jogo.

   b. Caso um jogador acerte o número total, ele é o vencedor da rodada e perde um palito.
   Os outros jogadores anotam esse fato para tomar decisões de aposta em rodadas futuras.
   E o vencedor da rodada é o primeiro a ter que fazer sua aposta na próxima rodada.
   
   c. Caso ninguém vença a rodada, a roda de apostas é mudada por uma posição.
   O jogador que apostou por segundo nessa rodada será o primeiro a apostar na próxima.
   
 

## Como um jogador escolhe quanto segurar em uma rodada:

1. Uma simples escolha aleatória de 0 ao número de palitos disponível ao jogador.

## Como um jogador escolhe quanto apostar em uma rodada:

-  Um jogador usará das seguintes informações que ele possui:

    - quantos palitos ele mesmo está segurando nessa rodada;
    
    - se há um número mínimo de palitos que cada jogador precisa jogar na rodada,
    por exemplo na primeira é necessário segurar pelo menos 1 palito;
    
    - quais foram as apostas anteriores dessa mesma rodada;
    
    - quantas vezes cada outro jogador venceu alguma rodada anterior,
    portanto quantos palitos cada outro jogador possui.
    
1. É decidido o número mínimo de palitos que foram segurados na rodada:

    - pelo menos o número de palitos que ele mesmo está segurando.
    
    - mais, se há, um número mínimo que tem que ser jogado na rodada vezes a quantidade de outros jogadores.
    
   Por exemplo, ele está segurando 2 palitos, e é a primeira rodada, portanto cada outro jogador tem que
   estar segurando pelo menos 1 palito, e há 4 outros jogadores. **2 + (1 * 4) = 6**
    
2. As apostas já feitas são comparadas à quantidade de palitos do apostador respectivo:
    
    - como **não há senso de blefe** entre os jogadores, se um jogador aposta um número menor que sua quantidade de palitos
    ele certamente está segurando aquela quantidade ou menor.
    
    - o mínimo entre a aposta de um jogador e a sua quantidade de palitos é calculado, e será tomada como a quantidade
    máxima que aquele jogador apostou.
    
   Por exemplo, um jogador que possui 3 palitos e apostou a quantidade 2,
   esse jogador certamente está segurando 2 palitos ou menos, apesar de possuir 3.
   
3. É decidido o número máximo de palitos que foram segurados na rodada:

    - é tomada a soma dos máximos que cada outro jogador pode ter apostado, mais a quantidade segurada pelo próprio jogador.
    
   Por exemplo, é calculado que cada outro jogador pode ter jogado no máximo 1, 2, 2, e 3 palitos respectivamente, mais
   1 palito que o próprio jogador está segurando. **(1 + 2 + 2 + 3) + 1 = 9**
   
4. É escolhido um número, entre o mínimo e máximo, para ser apostado:

    - É feita a escolha de um número aleatório entre o mínimo e o máximo que podem ter sido apostados.
    
    - Leva-se em consideração que o jogador não pode apostar um número que já tenha sido apostado na rodada.
    
    - Caso não haja número, entre o mínimo e máximo, que não tenha sido apostado, o jogador faz uma aposta desesperada,
    apostando um número acima do máximo já apostado. Que no nosso caso, não tem chance de estar correto.
    
   Por exemplo, o mínimo calculado é 6 e o máximo 9, e 2 outros jogadores já apostaram os números 6 e 8;
   é feita uma decisão aleatória entre 7 e 9. Caso 4 outros jogadores já tenham apostado os números 6, 7, 8 e 9;
   seria feita uma decisão desesperada pelo número 10, que certamente está errado.
