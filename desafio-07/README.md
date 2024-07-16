# Desafio 07: Verificador de Senhas

## Desafio
Há n usuários registrados no site CuteKittens.com. Cada um deles tem uma senha única representada por pass[1], pass[2], ..., pass[N]. Como este é um site muito adorável, muitas pessoas querem acessar as fotos fofas dos gatinhos. Mas o administrador não quer que o site esteja disponível para o público em geral, então apenas aqueles que têm senhas podem acessá-lo.

Yu, sendo um hacker fabuloso, encontra uma brecha no sistema de verificação de senhas. Uma string que é uma concatenação de uma ou mais senhas, em qualquer ordem, também é aceita pelo sistema de verificação de senhas. Qualquer senha pode aparecer uma ou mais vezes nessa string. Dado o acesso a cada uma das senhas, e também a uma string de tentativa de login, determine se essa string será aceita pelo sistema de verificação de senhas do site. Se toda a string puder ser criada concatenando senhas, ela é aceita. Nesse caso, retorne as senhas na ordem em que devem ser concatenadas, separadas por um espaço em uma linha. Se a tentativa de senha não for aceita, retorne 'WRONG PASSWORD'.

## Detalhamento do Desafio:
1. Complete a função passwordCracker que possui os seguintes parâmetros:
- string passwords[n]: uma lista de strings de senhas.
- string loginAttempt: a string que deve ser testada para aceitação.
2. Retorne as senhas como uma única string na ordem necessária para que a senha seja aceita, separadas por um espaço. Se não for possível formar a string, retorne a string "WRONG PASSWORD".

## Exemplo
Entrada: 
- passwords = ["because", "can", "do", "must", "we", "what"]
- loginAttempt = "wedowhatwemustbecausewecan"

Saída:
- "we do what we must because we can"

Explicação:
Neste caso, precisamos verificar se podemos formar a string "wedowhatwemustbecausewecan" usando as senhas fornecidas. 

Vamos ver como podemos formar essa string:
- "we" (passwords[4])
- "do" (passwords[2])
- "what" (passwords[5])
- "we" (passwords[4])
- "must" (passwords[3])
- "because" (passwords[0])
- "we" (passwords[4])
- "can" (passwords[1])

Portanto, podemos formar a string "wedowhatwemustbecausewecan" concatenando as senhas fornecidas na seguinte ordem: "we do what we must because we can".

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Manipulação de Strings: Aprenda a trabalhar com substrings e verificar prefixos de strings.
- Estruturas de Dados: Familiarize-se com o uso de arrays ou listas para gerenciar coleções de strings.
- Algoritmos de Busca: Entenda como implementar uma busca que verifique todas as combinações possíveis de strings.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1: 
- Entrada: passwords = ["because", "can", "do", "must", "we", "what"], loginAttempt = "wedowhatwemustbecausewecan"
- Saída Esperada: "we do what we must because we can"
### Teste 2:
- Entrada: passwords = ["hello", "planet"], loginAttempt = "helloworld"
- Saída Esperada: "WRONG PASSWORD"
### Teste 3:
- Entrada: passwords = ["ab", "abcd", "cd"], loginAttempt = "abcd"
- Saída Esperada: "ab cd" ou "abcd"
### Teste 4:
- Entrada: passwords = ["ozkxyhkcst", "xvglh", "hpdnb", "zfzahm"], loginAttempt = "zfzahm"
- Saída Esperada: "zfzahm"
### Teste 5:
- Entrada: passwords = ["gurwgrb", "maqz", "holpkhqx", "aowypvopu"], loginAttempt = "gurwgrb"
- Saída Esperada: "gurwgrb"
### Teste 6:
- Entrada: passwords = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], loginAttempt = "aaaaaaaaaab"
- Saída Esperada: "WRONG PASSWORD"
### Teste 7:
- Entrada: passwords = ["ejevas", "drdv", "mgxucpnh", "wqixbctfd", "kmmam", "kjquwvis", "liznldbnh", "pivoicfu", "espropqatm", "dbrasoqg"], loginAttempt = "cfuwqixbctfdliznldbnhkmmamlsprmpqatmljevaskmmamwqixbctfdpivoicauwgixbctfdmgxucpnhejevasdrdvpivoicfuliznldbnh"
- Saída Esperada: "WRONG PASSWORD"
### Teste 8:
- Entrada: passwords = ["okweif", "rpgnteja", "ufemijimuw", "vpon", "eoncaf", "udgf", "hhtez", "aiknzgy", "bpndljur", "eeycbwv"], loginAttempt = "ufemijimuweeycbwvokweifvponbpndljurudgfaiknzgyhhtezufemijimuwufemijimuwaiknzgyudgfufemijimuwrpgntejaeoncafvponudgfbpndljurokweifhhtezbpndljurvponufemijimuwudgfbpndljurufemijimuweoncafrpgntejaudgf"
- Saída Esperada: "ufemijimuw eeycbwv okweif vpon bpndljur udgf aiknzgy hhtez ufemijimuw ufemijimuw aiknzgy udgf ufemijimuw rpgnteja eoncaf vpon udgf bpndljur okweif hhtez bpndljur vpon ufemijimuw udgf bpndljur ufemijimuw eoncaf rpgnteja udgf"

## Dicas Extras:
- Utilize recursão ou iteração com uma pilha ou fila para tentar todas as combinações possíveis de senhas.
- Considere usar uma abordagem de backtracking para desfazer combinações de senhas que não levam a uma solução válida.
- Lembre-se de que uma senha pode ser usada mais de uma vez na tentativa de formar a string de login.