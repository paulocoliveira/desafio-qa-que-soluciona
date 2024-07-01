# Desafio 01: Escadaria

## Desafio
Este é um desafio de programação cujo objetivo é criar uma escadaria de tamanho n utilizando símbolos # e espaços. A base e a altura da escadaria são iguais ao valor de n, e a última linha não é precedida por espaços.

## Detalhamento do Desafio:
1. Crie uma função "escadaria" que recebe por parâmetro um inteiro n que representa o tamanho da escadaria
2. Imprima uma escadaria conforme descrito e demonstrado abaixo

## Exemplo
Esta é uma escadaria de tamanho 4:
```
   #
  ##
 ###
####
```

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Loops: Aprenda a utilizar loops em Python (pode usar o loop for-range)
- Manipulação de Strings: Aprenda a imprimir uma quantidade repetida de um mesmo caractere na mesma linha
- Concatenação de Strings: Aprenda a concatenar strings diferentes numa mesma linha usando Python
- Funções: Aprenda como criar uma função em Python que recebe um parâmetro e como chamar esta função no seu código para poder executá-la e testá-la

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1: 
- Entrada: n=2
- Saída Esperada:
```
   #
  ##
```
### Teste 2: 
- Entrada: n=7
- Saída Esperada:
```
      #
     ##
    ###
   ####
  #####
 ######
#######
```
### Teste 3: 
- Entrada: n=20
- Saída Esperada:
```
                   #
                  ##
                 ###
                ####
               #####
              ######
             #######
            ########
           #########
          ##########
         ###########
        ############
       #############
      ##############
     ###############
    ################
   #################
  ##################
 ###################
####################
```

## Dicas Extras:
- A última linha deve ter 0 espaços à sua frente.
- A escadaria está alinhada à direita, composta por símbolos # e espaços, e tem uma altura e largura de n.