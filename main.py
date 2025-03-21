from flows import main_fn, secondary_flow

if __name__ == "__main__":
    print("Iniciando automação com múltiplos fluxos")
    print("-" * 50)

    main_fn()  # Executa o primeiro fluxo
    secondary_flow()  # Executa o segundo fluxo

    print("Todos os fluxos foram concluídos.")
    print("-" * 50)
