import os

def main():
    mensagens = []
    nome = input("Nome: ")

    while True:    
        # limpando o terminal
        os.system('cls')
        
        if len(mensagens) > 0:
            for m in mensagens:
                print(f"{m['nome']} - {m['texto']}")
        
        print("___________________")
        
        # obtendo texto
        texto = input("mensagem: ")
        if texto == "fim":
            break
        
        # adicionando mensagem na lista
        mensagens.append({
            "nome": nome,
            "texto": texto
        })

if __name__ == '__main__':
    main()

  
# ------------------------------------------------------------------------------  
'''
    Comandos:
    fim  ---------  sair do chat
'''
