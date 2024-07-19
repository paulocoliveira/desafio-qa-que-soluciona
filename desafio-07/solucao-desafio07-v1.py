def passwordCracker(passwords, loginAttempt):
    n = len(loginAttempt)  # Comprimento da tentativa de login
    dp = [""] * (n + 1)  # Array para armazenar a combinação de senhas usadas até cada posição
    dp[0] = ""  # Inicializa a primeira posição como string vazia, pois não é necessário nenhuma senha para formar uma string vazia

    for i in range(1, n + 1):  # Itera sobre cada posição da string de tentativa de login
        for password in passwords:  # Itera sobre cada senha na lista de senhas
            length = len(password)  # Comprimento da senha atual
            # Verifica se a posição atual é maior ou igual ao comprimento da senha, se a combinação até a posição anterior é válida
            # e se a substring da tentativa de login corresponde à senha atual
            if i >= length and dp[i - length] is not None and loginAttempt[i - length:i] == password:
                if dp[i - length] == "":  # Se a combinação até a posição anterior for uma string vazia
                    dp[i] = password  # Armazena a senha atual em dp[i]
                else:
                    dp[i] = dp[i - length] + " " + password  # Caso contrário, concatena a senha atual à combinação anterior com um espaço
                break  # Sai do loop das senhas, pois encontrou uma combinação válida para a posição atual
        else:
            dp[i] = None  # Se nenhuma senha corresponder, marca dp[i] como None

    # Retorna a combinação de senhas usada para formar loginAttempt, ou "WRONG PASSWORD" se não for possível formar a string
    return dp[n] if dp[n] is not None else "WRONG PASSWORD"

# Testes
assert passwordCracker(["because", "can", "do", "must", "we", "what"], "wedowhatwemustbecausewecan") == "we do what we must because we can", "Teste falhou para 'wedowhatwemustbecausewecan'"
assert passwordCracker(["hello", "planet"], "helloworld") == "WRONG PASSWORD", "Teste falhou para 'helloworld'"
result = passwordCracker(["ab", "abcd", "cd"], "abcd")
assert result in ["ab cd", "abcd"], f"Teste falhou para 'abcd', resultado obtido foi '{result}'"
assert passwordCracker(["ozkxyhkcst", "xvglh", "hpdnb", "zfzahm"], "zfzahm") == "zfzahm", "Teste falhou para 'zfzahm'"
assert passwordCracker(["gurwgrb", "maqz", "holpkhqx", "aowypvopu"], "gurwgrb") == "gurwgrb", "Teste falhou para 'gurwgrb'"
assert passwordCracker(["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], "aaaaaaaaaab") == "WRONG PASSWORD", "Teste falhou para 'aaaaaaaaaab'"
assert passwordCracker(["ejevas", "drdv", "mgxucpnh", "wqixbctfd", "kmmam", "kjquwvis", "liznldbnh", "pivoicfu", "espropqatm", "dbrasoqg"], 
                        "cfuwqixbctfdliznldbnhkmmamlsprmpqatmljevaskmmamwqixbctfdpivoicauwgixbctfdmgxucpnhejevasdrdvpivoicfuliznldbnh") == "WRONG PASSWORD", "Teste falhou para a entrada complexa"
assert passwordCracker(["okweif", "rpgnteja", "ufemijimuw", "vpon", "eoncaf", "udgf", "hhtez", "aiknzgy", "bpndljur", "eeycbwv"], 
                        "ufemijimuweeycbwvokweifvponbpndljurudgfaiknzgyhhtezufemijimuwufemijimuwaiknzgyudgfufemijimuwrpgntejaeoncafvponudgfbpndljurokweifhhtezbpndljurvponufemijimuwudgfbpndljurufemijimuweoncafrpgntejaudgf") == \
       "ufemijimuw eeycbwv okweif vpon bpndljur udgf aiknzgy hhtez ufemijimuw ufemijimuw aiknzgy udgf ufemijimuw rpgnteja eoncaf vpon udgf bpndljur okweif hhtez bpndljur vpon ufemijimuw udgf bpndljur ufemijimuw eoncaf rpgnteja udgf", \
       "Teste falhou para a longa sequência de login"
