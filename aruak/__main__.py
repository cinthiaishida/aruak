from .db import AruakDB

def main():
    db = AruakDB()

    while True:
        print("\nEscolha a opção de busca:")
        print("1. Buscar por conceito")
        print("2. Buscar por transcrição (letras/sons)")
        print("3. Imprimir dicionário completo")
        print("Digite 'sair' para encerrar.")

        escolha = input("Escolha uma opção: ").lower()

        if escolha == "sair":
            print("Encerrando o programa.")
            break

        elif escolha == "1":
            conceito = input("Digite o conceito: ")
            resultados = db.buscar_traducao_por_conceito(conceito)

            if resultados:
                print("\nResultados:")
                for idioma, conceito, forma, fonte in resultados:
                    print(f"{conceito.capitalize()} - {idioma.capitalize()}: {forma} (Fonte: {fonte or 'Não disponível'})")
            else:
                print("Nenhum resultado encontrado.")

        elif escolha == "2":
            trecho = input("Digite o trecho da transcrição: ")
            resultados = db.buscar_por_transcricao(trecho)

            if resultados:
                print("\nResultados:")
                for idioma, conceito, forma, fonte in resultados:
                    print(f"{conceito.capitalize()} - {idioma.capitalize()}: {forma} (Fonte: {fonte or 'Não disponível'})")
            else:
                print("Nenhum resultado encontrado.")

        elif escolha == "3":
            todos = db.dicionario_completo()

            agrupado = {}
            for idioma, conceito, forma, fonte in todos:
                agrupado.setdefault(conceito, []).append((idioma, forma, fonte))

            print("\nDicionário completo:")
            for conceito in sorted(agrupado):
                print(f"\n{conceito.capitalize()}:")
                for idioma, forma, fonte in agrupado[conceito]:
                    print(f"  {idioma.capitalize()}: {forma} (Fonte: {fonte or 'Não disponível'})")

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
