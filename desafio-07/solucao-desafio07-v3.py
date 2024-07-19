def passwordCracker(passwords, loginAttempt):
    # Usamos um dicionário para memoização
    memo = {}
    
    def canFormLogin(attempt):
        # Se a tentativa já foi processada, retorna o resultado armazenado
        if attempt in memo:
            return memo[attempt]
        
        # Se a tentativa for vazia, retornamos uma lista vazia (base da recursão)
        if attempt == "":
            return []
        
        # Tentamos usar cada senha como prefixo
        for password in passwords:
            if attempt.startswith(password):
                # Chamamos recursivamente a função para o restante da tentativa
                result = canFormLogin(attempt[len(password):])
                # Se conseguirmos formar a senha, adicionamos à lista e retornamos
                if result is not None:
                    memo[attempt] = [password] + result
                    return memo[attempt]
        
        # Se não foi possível formar a string, armazenamos None
        memo[attempt] = None
        return None
    
    # Inicia a tentativa de formar a senha completa
    result = canFormLogin(loginAttempt)
    
    # Verifica o resultado e retorna a senha correta ou uma mensagem de erro
    if result is None:
        return "WRONG PASSWORD"
    else:
        return " ".join(result)

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