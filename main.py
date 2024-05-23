"""
Crie um programa de aplicativo de cinema que faça o seguinte:
- O usuário informa nome e idade.
- O programa mostra uma lista de 5 filmes, a sala em que cada filme está passando, e a classificação indicativa (idade mínima) de cada filme.
- O usuário informa a sala onde está passando o filme desejado.
- Se o usuário tiver a idade mínima para o filme, o programa imprime o ingresso e encerra a aplicação.
- Se o usuário não tiver a idade mínima para o filme, o programa proíbe a entrada e solicita ao usuário que decida por outro filme.

Ao terminar, faça o commit e envie para um repositório remoto no GitHub, e por fim responda a atividade colando o link do repositório.

"""
nome = str(input("Insira o nome do usuario:\n"))
idade = int(input("Insira a idade\n"))


while True:
    print("Sala 1 - FILME: VERMES MALDITOS - Classificação: 18 anos")
    print("Sala 2 - FILME: XUXA E OS DOENDES - Classificação: livre")
    print("Sala 3 - FILME: 007 CASSINO ROYALE - Classificação: 16 anos")
    print("Sala 4 - FILME: VELOZES E FURIOSOS 25 - Classificação: 12 anos")
    print("Sala 5 - FILME: JACKIE CHAN, PORRADA A SOLTA - Classificação: 12 anos")

    sala = int(input("Escolha a sala\n"))

    match sala:
        case 1:
            if idade < 18:
                print(
                    "Idade incompativel com a classificação indicativa, escolha outro filme\n")
                continue
            else:
                print(
                    f"INGRESSO PARA O FILME: VERMES MALDITOS - SALA 1 |Nome: {nome}")
                break

        case 2:
            print(
                f"INGRESSO PARA O FILME: XUXA E OS DOENTES - SALA 2 |Nome: {nome}")
            break

        case 3:
            if idade < 16:
                print(
                    "Idade incompativel com a classificação indicativa, escolha outro filme\n")
                continue
            else:
                print(
                    f"INGRESSO PARA O FILME: 007 CASSINO ROYALE -SALA 3 |Nome: {nome}")
                break

        case 4:
            if idade < 12:
                print(
                    "Idade incompativel com a classificação indicativa, escolha outro filme\n")
                continue
            else:
                print(
                    f"INGRESSO PARA O FILME VELOZES E FURIOSOS 25 - SALA 4 |Nome: {nome}")
                break

        case 5:
            if idade < 12:
                print(
                    "Idade incompativel com a classificação indicativa, escolha outro filme\n")

            else:
                print(
                    f"INGRESSO PARA O JACKIE CHAN, PORRADA A SOLTA - SALA 4 |Nome: {nome}")
                break
