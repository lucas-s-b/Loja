products = {
    1: ("Maçã", 5),
    2: ("Pão", 10),
    3: ("Leite", 8)
}

cart = []
discount = 0.0
total = 0.0

while True:
    print("=== MENU DA LOJA ===")
    print("1 - Maçã (5 R$)")
    print("2 - Pão (10 R$)")
    print("3 - Leite (8 R$)")
    print("4 - Adcionar disconto.")
    print("5 - Finalizar compra.\n")
    
    try:
        choice = int(input("Escolha uma opção: "))
    except:
        print("Opção inválida! Utilize um número inteiro.\n")
        continue

    if choice == 4:
        try:
            discount = max(min(float(input("Ponha o disconto em porcentagem: ")), 100), 0)
            print(f"Disconto atual: {discount}%.\n")
        except:
            print("Disconto inválido! Utilize um número.\n")
        continue
    elif choice == 5:
        break

    if choice in products:
        product_name, price = products[choice]
        cart.append(product_name)
        total += price
        print(f"{product_name} adcionado ao carrinho.\n")
    else:
        print("Opção inválida!\n")

print("\n=== SUMÁRIO DE COMPRA ===\n")
print("Itens:", cart)
print(f"\nDisconto: {discount:.2f}%\n")
print(f"Total sem disconto: {total:.2f} R$\n")
print(f"Total: {total - (total * discount / 100):.2f} R$\n")