def show_menu():
    print("\n=== MENU DA LOJA ===")
    print("1 - Maçã (5 R$)")
    print("2 - Pão (10 R$)")
    print("3 - Leite (8 R$)")
    print("4 - Adcionar disconto.")
    print("5 - Finalizar compra.")

products = {
    1: ("Maçã", 5),
    2: ("Pão", 10),
    3: ("Leite", 8)
}

cart = []
discount = 0.0
total = 0.0

while True:
    show_menu()
    
    try:
        choice = int(input("Escolha uma opção: "))
    except:
        print("Opção inválida! Utilize um número.")
        continue

    if choice == 4:
        try:
            discount = float(input("Ponha o disconto em porcentagem: "))
        except:
            print("Disconto inválido! Utilize um número.")
            continue
    else:
        break

    if choice in products:
        product_name, price = products[choice]
        cart.append(product_name)
        total += price
        print(f"{product_name} adcionado ao carrinho.")
    else:
        print("Opção inválida!")

if total > 100:
    discount = total * 0.1
    total -= discount

print("\n=== SUMÁRIO DE COMPRA ===")
print("Itens:", cart)
print(f"Disconto: ${discount:.2f}")
print(f"Total: ${total:.2f}")