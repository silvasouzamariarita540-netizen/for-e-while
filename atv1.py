pergunta = [
    {
        "pergunta":"Esse numero é positivo ou negativo?(9)",
        "resposta_correta":"positivo"

    },
    {
        
        "pergunta":"essa pessoa tem 12 anos ela é (adulta ou crinaça)",
        "resposta_correta":"criança"
    },
    {
        
        "pergunta":"Qual é o maior valor (30 ou 39)",
        "resposta_correta":"39"
    },
    {
        
        "pergunta":"Esse numero é par ou impar(2)",
        "resposta_correta":"par"
    },
    {
        
        "pergunta":"A soma de 10+20:",
        "resposta_correta":"30"
    }
]

nome = input("Digite seu nome: ")
pontos = 0 

for item in pergunta:
    resposta = input(item["pergunta"] + ": ").strip().lower()

    if resposta == item["resposta_correta"]:
        print("Acertou!")
        pontos += 1
    else:
        print(f"Errou! A resposta certa era: {item['resposta_correta']}")
        

print(f"Parabéns, {nome}! Você completou todas as perguntas.")



    

 



    




