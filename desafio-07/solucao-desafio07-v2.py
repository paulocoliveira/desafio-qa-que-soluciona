def passwordCracker(passwords, loginAttempt):
    stack = [(loginAttempt, [])]  # Inicializa a pilha com a tentativa de login e um caminho vazio
    
    while stack:  # Enquanto a pilha não estiver vazia
        attempt, path = stack.pop()  # Pega o último elemento da pilha
        
        if attempt == "":  # Se a tentativa de login for uma string vazia
            return " ".join(path)  # Retorna o caminho como uma string de senhas separadas por espaço
        
        for password in passwords:  # Para cada senha na lista de senhas
            if attempt.startswith(password):  # Se a tentativa de login começa com a senha atual
                stack.append((attempt[len(password):], path + [password]))  # Adiciona à pilha a substring da tentativa de login sem a senha atual e o caminho atualizado
    
    return "WRONG PASSWORD"  # Retorna "WRONG PASSWORD" se nenhuma combinação funcionar

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