# Definição da função para criar a lista de compras
def criar_lista_compras():
    # Inicializa uma lista vazia para armazenar os itens da lista de compras
    lista = []

    # Loop infinito para permitir ao usuário adicionar itens à lista de compras
    while True:
        # Solicita ao usuário que insira o nome do item (ou 'sair' para encerrar)
        item = input("Digite o nome do item (ou 'sair' para encerrar): ")
        
        # Verifica se o usuário digitou 'sair' para encerrar a inserção de itens
        if item.lower() == "sair":
            break  # Sai do loop se o usuário digitar 'sair'
        
        # Solicita ao usuário que insira a quantidade do item
        quantidade = float(input(f"Digite a quantidade de '{item}' (em kg, l ou unid): "))
        
        # Solicita ao usuário que insira a unidade do item
        unidade = input("Digite a unidade (kg, l ou unid): ")
        
        # Adiciona o item, sua quantidade e unidade à lista de compras
        lista.append((item, quantidade, unidade))

    # Retorna a lista de compras preenchida
    return lista

# Definição da função para mostrar a lista de compras
def mostrar_lista_compras(lista):
    # Imprime um cabeçalho indicando que é a lista de compras
    print("\nLista de Compras:")
    
    # Loop através da lista de compras e imprime cada item formatado
    for i, (item, quantidade, unidade) in enumerate(lista, start=1):
        print(f"{i}. {quantidade:.2f} {unidade} de {item}")

# Verifica se este script está sendo executado diretamente
if __name__ == "__main__":
    # Exibe uma mensagem de boas-vindas ao usuário
    print("Bem-vindo à Lista de Compras!")
    
    # Chama a função para criar a lista de compras e armazena o resultado em uma variável
    lista_compras = criar_lista_compras()
    
    # Chama a função para mostrar a lista de compras, passando a lista criada como argumento
    mostrar_lista_compras(lista_compras)

