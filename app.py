def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def saudacao(nome):
    """Retorna uma mensagem de saudação personalizada."""
    return f"Olá, {nome}! Bem-vindo ao pipeline DevOps."

if __name__ == "__main__":
    print(saudacao("ECDE"))
    print(f"2 + 3 = {soma(2, 3)}")
