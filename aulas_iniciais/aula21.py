import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione Enter para continuar...")

turma = []

while True:
    limpar()
    print("=== MENU PRINCIPAL ===")
    print("OP 1: ALUNOS")
    print("OP 2: NOTAS")
    print("OP 3: PRESENÇAS")
    print("OP 4: TURMA")
    print("OP 0: SAIR")
    print()
    
    try:
        op1 = int(input("SELECIONE: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        pausar()
        continue

    if op1 == 0:
        print("Saindo do programa... Até mais!")
        break

    elif op1 == 1:
        while True:
            limpar()
            print("--- SUBMENU ALUNOS ---")
            print("OP 1: ADICIONAR ALUNO")
            print("OP 2: MUDAR ALUNO (EDITAR NOME)")
            print("OP 3: REMOVER ALUNO")
            print("OP 4: MOSTRAR LISTA DE ALUNOS")
            print("OP 0: VOLTAR")
            print()
            
            try:
                op_aluno = int(input("SELECIONE: "))
            except ValueError:
                continue

            if op_aluno == 0:
                break

            elif op_aluno == 1:
                limpar()
                nome = input("Digite o nome do novo aluno: ").strip()
                if nome:
                    aluno = {"nome": nome, "notas": [], "presencas": {}}
                    turma.append(aluno)
                    print(f"Aluno '{nome}' adicionado com sucesso!")
                else:
                    print("Nome inválido.")
                pausar()

            elif op_aluno == 2:
                limpar()
                nome_antigo = input("Digite o nome do aluno que deseja alterar: ").strip()
                for aluno in turma:
                    if aluno["nome"].lower() == nome_antigo.lower():
                        novo_nome = input(f"Digite o novo nome para {aluno['nome']}: ").strip()
                        if novo_nome:
                            print(f"Nome de '{aluno['nome']}' alterado para '{novo_nome}'!")
                            aluno["nome"] = novo_nome
                        break
                else:
                    print("Aluno não encontrado.")
                pausar()

            elif op_aluno == 3:
                limpar()
                nome_remover = input("Digite o nome do aluno a ser removido: ").strip()
                for aluno in turma:
                    if aluno["nome"].lower() == nome_remover.lower():
                        turma.remove(aluno)
                        print(f"Aluno '{aluno['nome']}' removido com sucesso.")
                        break
                else:
                    print("Aluno não encontrado.")
                pausar()

            elif op_aluno == 4:
                limpar()
                print("--- LISTA DE ALUNOS ---")
                if not turma:
                    print("Nenhum aluno cadastrado.")
                for i, aluno in enumerate(turma, 1):
                    print(f"{i}. {aluno['nome']}")
                pausar()

    elif op1 == 2:
        while True:
            limpar()
            print("--- SUBMENU NOTAS ---")
            print("OP 1: ADICIONAR NOTA")
            print("OP 2: MUDAR NOTA")
            print("OP 3: REMOVER NOTA")
            print("OP 4: MOSTRAR NOTA DE ALUNO DIGITADO")
            print("OP 0: VOLTAR")
            print()
            
            try:
                op_nota = int(input("SELECIONE: "))
            except ValueError:
                continue

            if op_nota == 0:
                break

            elif op_nota == 1:
                limpar()
                nome = input("Nome do aluno: ").strip()
                for aluno in turma:
                    if aluno["nome"].lower() == nome.lower():
                        try:
                            nota = float(input(f"Digite a nota para {aluno['nome']}: "))
                            aluno["notas"].append(nota)
                            print("Nota adicionada!")
                        except ValueError:
                            print("Valor de nota inválido.")
                        break
                else:
                    print("Aluno não encontrado.")
                pausar()

            elif op_nota == 2:
                limpar()
                nome = input("Nome do aluno: ").strip()
                for aluno in turma:
                    if aluno["nome"].lower() == nome.lower():
                        if not aluno["notas"]:
                            print("Este aluno não possui notas para alterar.")
                            break
                        print(f"Notas atuais de {aluno['nome']}: {aluno['notas']}")
                        try:
                            idx = int(input(f"Qual nota deseja mudar? (Digite de 1 a {len(aluno['notas'])}): ")) - 1
                            if 0 <= idx < len(aluno['notas']):
                                nova_nota = float(input("Digite a nova nota: "))
                                aluno["notas"][idx] = nova_nota
                                print("Nota alterada com sucesso!")
                            else:
                                print("Opção inválida.")
                        except ValueError:
                            print("Entrada inválida.")
                        break
                else:
                    print("Aluno não encontrado.")
                pausar()

            elif op_nota == 3:
                limpar()
                nome = input("Nome do aluno: ").strip()
                for aluno in turma:
                    if aluno["nome"].lower() == nome.lower():
                        if not aluno["notas"]:
                            print("Este aluno não possui notas para remover.")
                            break
                        print(f"Notas atuais: {aluno['notas']}")
                        try:
                            idx = int(input(f"Qual nota deseja remover? (Digite de 1 a {len(aluno['notas'])}): ")) - 1
                            if 0 <= idx < len(aluno['notas']):
                                removida = aluno["notas"].pop(idx)
                                print(f"Nota {removida} removida!")
                            else:
                                print("Opção inválida.")
                        except ValueError:
                            print("Entrada inválida.")
                        break
                else:
                    print("Aluno não encontrado.")
                pausar()

            elif op_nota == 4:
                limpar()
                nome = input("Digite o nome do aluno: ").strip()
                for aluno in turma:
                    if aluno["nome"].lower() == nome.lower():
                        print(f"\nAluno: {aluno['nome']}")
                        print(f"Notas: {aluno['notas']}")
                        if aluno["notas"]:
                            media = sum(aluno["notas"]) / len(aluno["notas"])
                            print(f"Média: {media:.2f}")
                        break
                else:
                    print("Aluno não encontrado.")
                pausar()

    elif op1 == 3:
        dia_selecionado = None
        dias_validos = ["segunda", "terça", "quarta", "quinta", "sexta"]
        
        while True:
            limpar()
            print("--- SUBMENU PRESENÇAS ---")
            print(f"Dia selecionado atualmente: {str(dia_selecionado).upper()}")
            print("-------------------------")
            print("OP 1: SELECIONAR DIA DA SEMANA (segunda a sexta)")
            print("OP 2: LANÇAR PRESENÇA DA TURMA")
            print("OP 3: MOSTRAR LISTA DE PRESENÇAS DO DIA")
            print("OP 0: VOLTAR")
            print()
            
            try:
                op_presenca = int(input("SELECIONE: "))
            except ValueError:
                continue

            if op_presenca == 0:
                break

            elif op_presenca == 1:
                limpar()
                print("Dias válidos: segunda, terça, quarta, quinta, sexta")
                dia = input("Digite o dia da semana: ").strip().lower()
                # Remove o "-feira" se o usuário digitar ex: "segunda-feira"
                dia = dia.replace("-feira", "")
                
                if dia in dias_validos:
                    dia_selecionado = dia
                    print(f"Dia {dia_selecionado.upper()} selecionado com sucesso!")
                else:
                    print("Dia inválido! Digite apenas o nome do dia (ex: segunda).")
                pausar()

            elif op_presenca == 2:
                limpar()
                if not dia_selecionado:
                    print("Erro: Você precisa selecionar um dia da semana primeiro (Opção 1).")
                    pausar()
                    continue
                if not turma:
                    print("Nenhum aluno cadastrado para chamada.")
                    pausar()
                    continue
                
                print(f"--- CHAMADA PARA {dia_selecionado.upper()} ---")
                print("Responda com 'p' para Presente ou 'f' para Falta.")
                
                for aluno in turma:
                    while True:
                        resp = input(f"{aluno['nome']}: ").strip().lower()
                        if resp == 'p':
                            aluno["presencas"][dia_selecionado] = "Presente"
                            break
                        elif resp == 'f':
                            aluno["presencas"][dia_selecionado] = "Ausente"
                            break
                        else:
                            print("Resposta inválida! Digite apenas 'p' ou 'f'.")
                print("\nChamada concluída!")
                pausar()

            elif op_presenca == 3:
                limpar()
                print("Dias disponíveis: segunda, terça, quarta, quinta, sexta")
                dia_busca = input("De qual dia você quer ver a lista de presença? ").strip().lower().replace("-feira", "")
                
                if dia_busca in dias_validos:
                    print(f"\n--- PRESENÇAS DE {dia_busca.upper()} ---")
                    houve_registro = False
                    for aluno in turma:
                        status = aluno["presencas"].get(dia_busca, "Não lançada")
                        print(f"Aluno: {aluno['nome']} -> {status}")
                        houve_registro = True
                    if not turma:
                        print("Nenhum aluno na turma.")
                else:
                    print("Dia inválido.")
                pausar()

    elif op1 == 4:
        while True:
            limpar()
            print("--- SUBMENU TURMA ---")
            print("OP 1: MOSTRAR TURMA COMPLETA")
            print("OP 0: VOLTAR")
            print()
            
            try:
                op_turma = int(input("SELECIONE: "))
            except ValueError:
                continue

            if op_turma == 0:
                break
                
            elif op_turma == 1:
                limpar()
                print("====================================")
                print("          DADOS DA TURMA            ")
                print("====================================")
                if not turma:
                    print("Turma vazia.")
                for aluno in turma:
                    print(f"Nome: {aluno['nome']}")
                    print(f"Notas: {aluno['notas']}")
                    # Mostra as presenças de forma limpa
                    presencas_formatadas = ", ".join([f"{dia.capitalize()}: {status}" for dia, status in aluno["presencas"].items()])
                    print(f"Presenças: {presencas_formatadas if presencas_formatadas else 'Nenhuma lançada'}")
                    print("-" * 36)
                pausar()
