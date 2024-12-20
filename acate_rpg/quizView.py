import os
import random
import time
class QuizView():
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def comeca_quiz(self, dificuldade, setor, quiz):
        self.limpar_terminal()
        print(f"Bem-vindo ao quiz de {setor}! ##É necessário gabaritar para ganhar experiência## \nResponda as perguntas abaixo:\n")
        
        
        pontos = 0
        perguntas = []
        while len(perguntas) != int(dificuldade):
            numero = random.randint(1,20)
            if numero not in perguntas:
                perguntas.append(numero)

        
        for i in range(len(perguntas)): 
            pergunta = quiz[str(perguntas[i])]["pergunta"]
            a = quiz[str(perguntas[i])]["a"]
            b = quiz[str(perguntas[i])]["b"]
            c = quiz[str(perguntas[i])]["c"]
            resposta_correta = quiz[str(perguntas[i])]["resposta"]
            
            
            print(f"{(perguntas[i])}. {pergunta}")
            print("\n")
            print(f"a) {a}")
            print(f"b) {b}")
            print(f"c) {c}")
            
            
            while True:
                try:
                    resposta_usuario = input("Digite a sua resposta (a, b ou c): ").lower()
                    if resposta_usuario not in ['a', 'b', 'c']:
                        print("\n")
                        raise ValueError("Opção inválida, tente novamente.")  # Levanta exceção se a resposta for inválida
                    break
                except ValueError as e:
                    print(e)
                    print("\n")
                
                
            if resposta_usuario == resposta_correta:
                print("Resposta correta!\n")
                print("\n")
                pontos += 1  # Incrementar a pontuação
            else:
                print(f"Resposta incorreta. A resposta correta era '{resposta_correta}'.\n")
                print("\n")

        if pontos == len(perguntas):
            print("Parabéns, você gabaritou o quiz! \n")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return True

        else:
            print("Infelizmente você não foi aprovado no curso :(")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return False


        



    