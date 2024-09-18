import sys
import time

##################################### <Texto e Frase lentos> #####################################
def escrever_frase(frase):
    for letra in frase:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.05)

def escrever_texto(text):
    for letra in text:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.04)

##################################### <Personalização do Jogador> #####################################
def inicializar_jogador(nome, genero):
    return {
        "nome": nome,
        "genero": genero,
    }

##################################### <Mapa de Erethum> #####################################
def inicializar_mapa():
    return [
        ['-', '-', '-', '-', '-'],
        ['S', '-', '-', 'A', '-'],
        ['-', '-', '-', '-', '-'],
        ['F', 'J', 'T', '-', '-'],
        ['-', '-', '-', '-', '-']
    ]

##################################### <Desenho do Mapa> #####################################
def desenhar_mapa(mapa):
    for linha in mapa:
        for celula in linha:
            print(f"{celula} ", end="")
        print("\n")

##################################### <Verificar o Status do Jogador EM COMBATE> #####################################
def verificar_estado_combate(vidas_jogador, vidas_draconato):
    if vidas_jogador <= 0:
        printar_derrota()
        sys.exit()  
    elif vidas_draconato <= 0:
        printar_vitoria()
        sys.exit()

def diminuir_vida(vida, quantidade):
    vida_atualizada = vida - quantidade

    if vida_atualizada < 0:
        return 0
    
    return vida_atualizada

def printar_vitoria():
    print("─────────────────────────────────────────────────────────────────────")
    print()
    time.sleep(1)
    vitoria = (f'''{nome}, Paladino das Terras de Torum, mostrando habilidades excepcionais e determinação implacável, com um golpe decisivo, você prevalece sobre seu formidável oponente, emergindo vitória da batalha.
Você derrota o Draconato em uma batalha épica!
Sua gana é um testemunho de sua força e coragem, destacando sua habilidade superior em combate. ''')
    escrever_texto(vitoria)
    print("\n")
    print("Você retorna a Torum com a Esfera de Esmeralda e mais um título a seu dispor!")
    print("\n")
    print('''

    〆  VICTORY  〆 
''')
    print("\n")
    print("Agradecemos a sua presença em nosso jogo! :D")
    print("\n")
    time.sleep(1)
    print("▪ Programação do jogo: Luyz Castelo, Catharina Alves e Lucas Costa")
    print("▪ Roteiro do Jogo: Catharina Alves")
    print("▪ Inspiração da História do RPG: Gabriel Gomes(Amigo próximo de Catharina)")
    print("\n")

def printar_derrota():
    print("─────────────────────────────────────────────────────────────────────")
    print()
    time.sleep(1)
    derrota = (f'''{nome} enfrenta o Draconato com bravura e determinação. No entanto, sua armadura danificada e o cansaço que consome seu corpo o levam a reconhecer sua iminente derrota. 
    Com resignação, ele dirige palavras de rendição ao seu formidável oponente, aceitando a superioridade do draconato e encontrando resignação em suas próprias falhas. 
    Nesse momento de adversidade, o paladino busca a redenção em sua derrota honrosa, desejando que a vitória do draconato seja justa.
    Com suas últimas forças, o paladino ergue sua espada e, com olhos resolutos, profere suas palavras finais com uma determinação inabalável: 

    — Que minha morte seja um testemunho de coragem e sacrifício, pois a luz da minha devoção jamais se apagará. 
    Que aqueles que seguirem meu caminho encontrem força na esperança e perseverança, e que a justiça prevaleça mesmo na escuridão mais profunda."

    {nome} recitou com clareza e bravura até sentir seu corpo doer, o Draconato gargalha após fincar a espada em seu peito.

    — Fraco... Enviarei uma mensagem extremamente agradável ao seu rei. 
    Que ele saiba que sua suposta justiça não passa de ilusão, e que seus campeões são meros joguetes insignificantes diante de minha força implacável. 
    Que meu triunfo ecoe como um aviso para todos os que ousam desafiar o poder do meu reino das sombras. ''')
    escrever_texto(derrota)
    print("\n")
    derrota2 = ("Você apaga antes de poder refutar seu adversário.")
    escrever_frase(derrota2)
    print("\n")
    morte = ("Você está morto.")
    escrever_frase(morte)
    print("\n")
    print('''
    〄  GAME OVER  〄 
''')
    print("\n")
    print("Agradecemos a sua presença até aqui! >:)")
    print("\n")
    time.sleep(1)
    print("▪ Programação do jogo: Luyz Castelo, Catharina Alves e Lucas Costa")
    print("▪ Roteiro do Jogo: Catharina Alves")
    print("▪ Inspiração da História do RPG: Gabriel Gomes(Amigo próximo de Catharina)")
    print("\n")


vidas_jogador = 10
vidas_draconato = 10

##################################### <Começo do Programa> #####################################
time.sleep(0.6)
bem_vindo = '''
              Bem-vindo ao jogo de RPG Textual!
            <> Erethum: A Esfera de Esmeralda <>
    <> Inspirado no sistema de RPG: Dungeons & Dragons <> '''

escrever_texto(bem_vindo)
print("\n")
time.sleep(0.6)

##################################### <Menu Principal> #####################################
while True:
    print("\n")
    print("────────────────⁣⁣⁣  ❐    MENU INICIAL   ❐  ──────────────────")
    print("\n")
    time.sleep(0.6)
    print("                    ►  Iniciar ⑆ [I]  ◄ ")
    time.sleep(0.6)
    print("\n")
    print("                    ►  Fechar ⑆ [F]   ◄")
    time.sleep(0.6)
    print("\n")
    print("                    ►  Sobre ⑆ [S]    ◄ ")
    time.sleep(0.6)
    print("\n")
    print("                    ►  Créditos ⑆ [C] ◄")
    time.sleep(0.6)
    print("\n")
    time.sleep(2)
    menu_principal = input("Digite aqui a sua escolha: ").lower()

##################################### <Iniciar o Jogo> #####################################
    while True:
        if menu_principal == 'f':
            print("\n")
            print("Você encerrou o jogo! Abrindo os créditos...")
            print("\n")
            print(".")
            time.sleep(0.5)    
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            print("\n")
            print("▪ Programação do jogo: Luyz Castelo, Catharina Alves e Lucas Costa")
            print("▪ Roteiro do Jogo: Catharina Alves")
            print("▪ Inspiração da História do RPG: Gabriel Gomes(Amigo próximo de Catharina)")
            print("\n")
            print("Agradecemos a sua presença em nosso jogo!")
            print(":D <3")
            sys.exit()
            # Encerramento do Jogo
        elif menu_principal == 's':
            print("\n")
            time.sleep(2)
            print("Você abriu a opção Sobre o jogo...")
            print("\n")
            print(".")
            time.sleep(0.5)    
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            print("\n")
            sobre = ('''Sobre o Jogo:
▸ Um jogo de RPG(Role-playing game) é um jogo que você assume um papel de um personagem e conta uma história colaboramente. 
▸ Neste caso, criamos uma história baseada no Sistema Dungeons & Drangons e de uma campanha onde um dos membros do grupo (Catharina Alves) jogou essa campanha com o nome de Erethum.
▸ Jogar é bem simples, apenas inserir o dígito que o programa pede.  ''')
            escrever_texto(sobre)
            print("\n")
            input("Pressione qualquer tecla para retornar ao menu principal.")
            print("\n")
            break
            # Sobre o Jogo
        elif menu_principal == 'c':
            time.sleep(2)
            print("\n")
            print("Você abriu os Créditos...")
            print("\n")
            print(".")
            time.sleep(0.5)    
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            print("\n")
            print("▪ Programação do jogo: Luyz Castelo, Catharina Alves e Lucas Costa")
            print("▪ Roteiro do Jogo: Catharina Alves")
            print("▪ Inspiração da História e falas do RPG: Gabriel Gomes(Amigo próximo de Catharina);")
            print("\n")
            input("Pressione qualquer tecla para retornar ao Menu Principal.")
            print("\n")
            break
        elif menu_principal == 'i':
            print("\n")
            time.sleep(2)
            print("Você iniciou! Abrindo o jogo...")
            print("\n")
            print(".")
            time.sleep(0.5)    
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            print("\n")
            
            texto_comeco = ('''Antes de começarmos a entrar no mundo de Erethum, você precisa estar fisicamente no mundo.
Logo, começamos pelo seu personagem!
Seu personagem já está predefinido na raça e classe, basta escolher um nome e seu genêro! ''')
            escrever_texto(texto_comeco)
            print("\n")
            time.sleep(0.5)

            nome = input("Escolha um nome para seu personagem: ")
            while not nome:
                nome = input("Nome inváido! Escolha um nome novamente para seu personagem: ")

            print("\n")
            print(f"O nome de seu personagem é: {nome}")
            print("\n")

            time.sleep(0.2)

            genero = input("Escolha o genêro entre Feminino [F], Masculino [M] ou Neutro [N]: ")
            print("\n")
            while True:
                if genero.lower() == 'm':
                    print("Genêro Masculino escolhido com sucesso!")
                    break
                elif genero.lower() == 'f':
                    print("Genêro Feminino escolhido com sucesso!")
                    break
                elif genero.lower() == 'n':
                    print("Gênero Neutro escolhido com sucesso!")
                    break
                else:
                    print("Genêro inválido!")
                    print()
                    genero = input("Digite novamente o genêro entre Feminino [F], Masculino [M] ou Neutro [N]: ")
                    print()
                    continue

            print("\n")
            time.sleep(0.5)

##################################### <Ficha do Usuário> #####################################
            print("Agora que escolheu como seu personagem é, aqui está a sua ficha: ")
            time.sleep(1)
            print("\n")
            print("────────────────  ︲◎︲ Ficha de Seu Personagem ︲◎︲  ────────────────")
            print("\n")
            print(f"Nome do personagem: {nome}")
            print("\n")
            print(("[PREDEFINIDO] Raça: Humano"))
            print("\n")
            print(f"[PREDEFINIDO] Classe: Paladino")
            print("\n")
            print(f"[PREDEFINIDO] Idade: 24 anos")
            print("\n")
            print(f"[PREDEFINIDO] Tendência: Leal e Bom")
            print("\n")
            print("─────────────────────────────────────────────────────────────────────")
            time.sleep(0.6)


            fim1 = ('''
Agora que você têm tudo que precisa, vamos adentrar ao mundo de Erethum: A Esfera de Esmeralda

Lembre-se que suas escolhas têm consequências... ''')
            escrever_texto(fim1)
            print("\n")
            
            input("Pressione qualquer tecla para começar o jogo.")
            print("\n")

            print("─────────────────────────────────────────────────────────────────────")

            jogador = inicializar_jogador(nome, genero)

##################################### <Jogo Iniciado> #####################################
            print("\n")
            historia = (f'''Você estava desfrutando de uma noite tranquila de sono até estrondos perturbarem sua soneca.
Rapidamente, você se levanta e percebe que os ruídos estão vindo da porta. 
Ao abrir a porta, nota uma carta no chão e a pega para ler atentamente.

    "Saudações, {nome},

    Aprecie meus cumprimentos. Venho informar que a preciosa Esfera de Esmeralda foi roubada. 
    Necessito urgentemente de sua ajuda para resgatá-la na temida Fenda do Abismo. 
    O mapa para chegar lá está anexado a esta correspondência.

    Atenciosamente,

    Rei Tamam"

Sem hesitação, você se prepara para embarcar em uma missão para resgatar a preciosa Esfera de Esmeralda, certificando-se de levar consigo uma variedade de recursos essenciais.
O mapa fornecido na carta será seu guia, indicando o trajeto a seguir e apontando o caminho mais direto e descomplicado.''')
            escrever_texto(historia)
            print("\n")

            print("\n")
            mapa =  inicializar_mapa()
            desenhar_mapa(mapa)
            print("\n")

            time.sleep(0.2)
            localizacao = ('''Jogador, você está em ↣ [J]
Salaz, o Deserto do Sol ↣ [S]
Fenda do Abismo ↣ [A]
Floresta ↣ [F]
Torum, a capital do Marfim ↣ [T]
''')
            escrever_frase(localizacao)
            print("\n")

            print("─────────────────────────────────────────────────────────────────────")

            print("\n")
            print(f"⤠ Aonde {nome} vai agora? ⤟")
            print("\n")
            
            time.sleep(0.4)
            print('''[S] Salaz, o Deserto do Sol
[T] Retornar a Torum, a capital do Marfim
[A] Ir direto para a Fenda pegando um atalho ''')
            print("\n")

            while True:
                resposta1 = input("Digite aqui a opção sendo: ")
                print("\n")
                if resposta1.lower() == 't':
                    print("⑅ Você escolheu retornar para Torum! ⑅")
                    print("\n")
                    paladin = ('''Antes de cotinuar o caminho de volta, você questiona a sua capacidade como Paladino.
O Paladino sempre segue o caminho da verdade, da lei e da ordem, sempre disposto a proteger e ajudar a todos.
Com esse pensamento, você retorna a floresta, ainda digno de seu nome. ''')
                    escrever_texto(paladin)
                    print("\n")

                    print("\n")
                    print('''[S] Salaz, o Deserto do Sol
[T] Retornar a Torum, a capital do Marfim
[A] Ir direto para a Fenda pegando um atalho ''')
                    print("\n")
                    continue
                elif resposta1.lower() == 'a':
                    print("⑅ Você escolheu ir direto para a Fenda pegando um atalho! ⑅")
                    print("\n")
                    caminho_a = ('''Assim que você caminha no atalho, passando pelos arbustos e árvores você se sente observado.
Um barulho de galho quebrando o faz retirar a espada da bainha
Outro barulho.''')
                    escrever_frase(caminho_a)
                    print("\n")
                    time.sleep(1)
                    barulho1 = ("Mais um.")
                    escrever_frase(barulho1)
                    print("\n")
                    time.sleep(1)
                    barulho2 = ("E mais.")
                    escrever_frase(barulho2)
                    print("\n")
                    time.sleep(1)
                    barulho3 = ("Muitos barulhos.")
                    escrever_frase(barulho3)
                    print("\n")
                    time.sleep(1)
                    acao1 = ("E de repente, sua visão fica turva e você cai.")
                    escrever_frase(acao1)                    
                    print("\n")
                    time.sleep(1)
                    acao2 = ("Você não adentrou em uma floresta qualquer. Adentrou em uma área perigosíssima.")
                    escrever_frase(acao2)
                    print("\n")
                    time.sleep(1)
                    acao3 = ("Você é capturado por uma enorme quantidade de furtivos Tieflings...")
                    escrever_frase(acao3)
                    print("\n")
                    time.sleep(1)
                    acao4 = ("...e foi capturado e morto.")
                    escrever_frase(acao4)
                    print("\n")
                    time.sleep(0.15)
                    print('''
                〄  GAME OVER  〄 ''')
                    print("\n")
                    print("Agradecemos seu caminho até aqui! >:) ")
                    print("\n")
                    sys.exit()             
                elif resposta1.lower() == 's':
                    print("⑅ Você escolheu ir para Salaz, o Deserto do Sol! ⑅")
                    print("\n")
                    caminho_s = ('''Passando pelo enorme caminho da floresta, você observa um deserto vasto e um forte calor provindo do Solaris.
Ao continuar os passos, você avista uma aldeia mais a frente e, logo mais ao fundo, você enxerga a Fenda do Abismo. ''')
                    escrever_frase(caminho_s)
                    print("\n")
                    break
                else:
                    print("\n")
                    print("Opção inválida, digite novamente")
                    print("\n")
                    continue
                
            print(f"⤠ Aonde {nome} vai agora? ⤝")
            print("\n")
            print('''[1] Ir para a Aldeia
[2] Ir para a Fenda do Abismo ''')
            while True:
                print("\n")    
                resposta2 = input("Digite aqui a opção: ")
                if resposta2 == '1':
                    print("\n")
                    print("⑅ Você escolheu ir para a Aldeia ⑅")
                    print("\n")
                    time.sleep(0.15)
                    caminho_aldeia = ('''Chegando mais perto das casas, você observa com mais clareza que não há um único respiro a não ser o seu.
Você observa o redor, parece abandonado. 
Você continua os passos e escuta o arrastar da areia. ''')
                    escrever_texto(caminho_aldeia)
                    print("\n")
                    acao1_2 = ("Ao virar a cabeça, você vê um ser com uma máscara com detalhes em dourado. O ser o encara e move o dedo para a boca da máscara.")
                    escrever_frase(acao1_2)
                    print("\n")
                    time.sleep(1)
                    acao1_3 = ("— Shh... — Ele sussura, como se estivesse no pé de seu ouvido.")
                    escrever_frase(acao1_3)
                    print("\n")
                    time.sleep(1)
                    acao1_4 = ("E de repente, sua visão fica turva.") 
                    escrever_frase(acao1_4)
                    print("\n")
                    time.sleep(1)
                    acao1_5 = ("Você não esperava que essa aldeia seria habitada por caninbais insanos.")
                    escrever_frase(acao1_5)
                    print("\n")
                    time.sleep(1)
                    acao1_6 = ("A Aldeia Canibus, onde sob os raios de Solaris se encontra com a insanidade.")
                    escrever_frase(acao1_6)
                    print("\n")
                    time.sleep(0.5)
                    acao1_7 = ("Você foi devorado, como um ótimo banquete.")
                    escrever_frase(acao1_7)
                    print("\n")
                    print('''
                〄  GAME OVER  〄 
''')
                    print("\n")
                    print("Agradecemos seu caminho até aqui! >:) ")
                    print("\n")
                    sys.exit()

                elif resposta2 == '2':
                    print("\n")
                    print("⑅ Você escolhe a Fenda do Abismo! ⑅")
                    print("\n")
                    caminho_abismo = ('''À medida que você avança pela densa camada de areia, a escuridão se intensifica, forçando-o a acender uma tocha para iluminar seu caminho.
Conforme se aproxima, a cintilante luz da esmeralda se revela, mas, emergindo das sombras, você vislumbra um temível Draconato brandindo uma espada, ameaçando-o com determinação. ''')
                    escrever_texto(caminho_abismo)
                    print("\n")

                    draconato = ("— Interrompa seu avanço, paladino! A Esfera de Esmeralda não será entregue a mãos indignas. Se ousar prosseguir, encontrará a fúria de um dragão ardente! — Exclama o Draconato.")
                    escrever_frase(draconato)
                    print("\n")
                    break
                else:
                    print("\n")
                    print("Opção inválida, digite novamente")
                    print("\n")
                    print('''[1] Ir para a Aldeia
[2] Ir para a Fenda do Abismo ''')

##################################### <COMBATE> #####################################
            narrador = (f'''Para que {nome} derrote o Draconato, você deve responder algumas perguntas! 
A cada resposta correta, você garante -1 ou mais da vida do Draconato que contém: 10/10 vidas. 
A cada resposta errada, {nome} perde -1 ou mais de: 10/10 vidas. ''')
            escrever_texto(narrador)
            print("\n")

            print("─────────────────────────────────────────────────────────────────────")
            
##################################### <PERGUNTAS - MATÉRIA ALGORITMOS> #####################################
##################################### <QUESTÃO 1.1> #####################################
            time.sleep(1)
            print("\n")
            print("QUESTÃO I: Qual é o conceito de Algoritmo?")
            time.sleep(0.5)
            opcoes1 = ('''
[1] Uma função matemática que relaciona o expoente necessário para obter um número específico a partir de uma base.
[2] Uma sucessão regular dos tempos fortes e fracos em uma frase musical.
[3] Um conjunto de instruções ou passos sequenciais que descrevem como resolver um problema ou realizar uma tarefa.
''') 
            escrever_frase(opcoes1)

            #[1] Logaritmo
            #[2] Ritmo Musical
            #[3] Algoritmo - CORRETA

            while True:
                print("\n")
                resposta_cap1 = input("Digite aqui a sua resposta: ")
                if resposta_cap1 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe1 = ("O ataque inimigo encontra uma brecha em sua defesa, causando um golpe contundente que faz suas pernas fraquejarem momentaneamente.")
                    escrever_frase(golpe1)
                    print("\n")
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    time.sleep(1)
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta_cap1 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Errada!")
                    print("\n")
                    golpe1_2 = ("Um feitiço sombrio enreda seu ser, drenando sua energia vital e deixando-o exausto e vulnerável.")
                    escrever_frase(golpe1_2)
                    print("\n")
                    print(f"﹝{nome} sofreu -2 de vida﹞")
                    print("\n")
                    time.sleep(0.8)
                    vidas_jogador = diminuir_vida(vidas_jogador, 2)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta_cap1 == '3':
                    time.sleep(1)
                    print("\n")
                    print("Resposta certa!")
                    print("\n") 
                    golpe1_3 = ("Ao erguer a espada, de forma astuta você finca a espada no ombro do Draconato!")
                    escrever_frase(golpe1_3)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    print("\n")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)
            
##################################### <QUESTÃO 2> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO II: Sobre Abstração e Generalização, qual o exemplo que mais se assemelha a ela?")
            opcoes2 = ('''
[1] A agenda diária para representar uma semana em termos de dias e hora.
[2] Um chef escreve uma receita de um prato.
[3] As pessoas olham para os padrões nos preços das ações para decidir quando comprar e vender.
''')
            escrever_texto(opcoes2)

            #Correta: [1]

            while True:
                print("\n")
                resposta2_cap1 = input("Digite aqui sua resposta: ")
                if resposta2_cap1 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Resposta certa!")
                    print("\n")
                    golpe2 = ('''Com um golpe preciso, seu ataque fende o ar, cortando as sombras e encontrando seu alvo. 
O Draconato é banhado em dor, seu corpo treme sob o impacto devastador. ''')
                    escrever_frase(golpe2)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")

                elif resposta2_cap1 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_1 = ("Uma lâmina perfurante encontra o Paladino, cortando através de sua proteção e deixando uma ferida profunda em seu corpo.")
                    escrever_frase(golpe2_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -2 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 2)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")  

                elif resposta2_cap1 == '3':
                    time.sleep(1)
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_2 = ("O inimigo acerta um golpe certeiro em seu escudo, enviando uma onda de dor que reverbera por seus braços.")
                    escrever_frase(golpe2_2)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <QUESTÃO 3> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO III: Quais são os tipos de váriaveis do Python?")
            opcoes3 = ('''
[1] int, char, boolean, string, array, class
[2] int, float, str, bool, list, tuple, dict, set ''')
            escrever_texto(opcoes3)
            
            #[2] CORRETA

            while True:
                print("\n")
                resposta3_cap1 = input("Digite aqui sua resposta: ")
                if resposta3_cap1 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe3 = ("O impacto do golpe atravessa sua armadura, enviando uma onda de dor intensa através de seu corpo resiliente.")
                    escrever_frase(golpe3)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta3_cap1 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe3_1 = ('''Seu poderoso golpe irrompe como um relâmpago, atravessando as defesas do Draconato com facilidade. 
O choque da colisão ecoa pelas trevas, deixando-o cambaleante e atordoado.''')
                    escrever_frase(golpe3_1)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")			
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <QUESTÃO 4> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO IV: Qual é o erro desse código?")
            opcoes4 = ('''
1    def soma(a, b):
2        resultado = a + b
3        return resultado
4
5    resultado_soma = soma(10, 5)
6           print(resultado_da_soma)

[1] NameError
[2] TypeError
[3] IndentationError ''')
            escrever_texto(opcoes4)
            #[1] Correta

            while True:
                print("\n")
                resposta4_cap1 = input("Digite aqui a sua resposta: ")
                if resposta4_cap1 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe4 = ("O golpe certeiro atinge o Draconato, fazendo suas escamas tremerem com a força do impacto e arrancando um rosnado de dor.")
                    escrever_frase(golpe4)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")	
                elif resposta4_cap1 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe4_1 = ("Um ataque implacável atinge em cheio seu escudo, fazendo seus braços tremerem sob a força do impacto.")
                    escrever_frase(golpe4_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -2 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 2)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta4_cap1 == '3':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe4_2 = ("O golpe do inimigo penetra em sua defesa, deixando uma ferida profunda que arde com agonia em seu corpo.")
                    escrever_frase(golpe4_2)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <PERGUNTAS - MATÉRIA 2> #####################################
##################################### <QUESTÃO 1> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO V: Quais são os operadores lógicos usados no Python?")
            opcoes5 = ('''
[1] is, me, or
[2] or, and, yes
[3] or, and, not ''')
            escrever_texto(opcoes5)
            
            #[3] CORRETA
            
            while True:
                print("\n")
                resposta1_cap2 = input("Digite aqui a sua resposta: ")
                if resposta1_cap2 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_1_1 = ("Um corte certeiro perfura sua armadura, deixando uma marca sangrenta que mostra a força do ataque desferido.")
                    escrever_frase(golpe2_1_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                
                elif resposta1_cap2 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_1_2 = ("O golpe desferido atinge o paladino com força, fazendo-o vacilar e deixando-o ofegante, lutando contra a dor agonizante.")
                    escrever_frase(golpe2_1_2)
                    print("\n")
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    time.sleep(1)
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                
                elif resposta1_cap2 == '3':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe4 = ("A lâmina cortante penetra nas defesas do draconato, causando feridas profundas que jorram sangue e desafiam sua resistência.")
                    escrever_frase(golpe4)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <QUESTÃO 2> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")            
            time.sleep(1)
            print("QUESTÃO VI: Quais são as condicionais em ordem correta?")
            opcoes6 = ('''
[1] if, elif, else
[2] if, else, else
[3] elif, elif, if ''')
            escrever_texto(opcoes6)

            #[1] CORRETA

            while True:
                print("\n")
                resposta2_cap2 = input("Digite aqui a sua resposta: ")
                if resposta2_cap2 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe2_2_1 = ("O impacto de um feitiço mágico desencadeia uma explosão de energia, lançando o draconato para trás e deixando-o ofegante com a dor ardente.")
                    escrever_frase(golpe2_2_1)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                
                elif resposta2_cap2 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_2_2 = ("Um projétil mágico atravessa o ar e atinge seu peito, fazendo-o cambalear com o impacto e dificultando sua respiração.")
                    escrever_frase(golpe2_2_2)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    time.sleep(1)
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                
                elif resposta2_cap2 == '3':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_2_3 = ("Uma explosão de energia desencadeada pelo adversário faz com que seu corpo seja arremessado para trás, deixando-o atordoado e com dores intensas.")
                    escrever_frase(golpe2_2_3)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    time.sleep(1)
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)
            
##################################### <QUESTÃO 3> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO VII: Esse código está correto?")
            opcoes7 = ('''
1    idade = 25
2
3    if idade < 18:
4        print("Você é menor de idade.")
5    else:
6        print("Você é maior de idade.")
7
8    if idade > 65:
9        print("Você é idoso.")
10
11    else:
12        print("Você não é idoso.")
                
[1] Sim
[2] Não  ''')
            escrever_texto(opcoes7)
            # [2] CORRETA

            while True:
                print("\n")
                resposta3_cap2 = input("Digite aqui a sua resposta: ")
                if resposta3_cap2 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_3_1 = ("A energia negra do ataque se choca contra a proteção do paladino, causando uma sensação de dor intensa que ameaça enfraquecer sua resolução.")
                    escrever_frase(golpe2_3_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -3 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 3)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                
                elif resposta3_cap2 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe2_3_2 = ("Um projétil afiado atinge o draconato em cheio, perfurando suas escamas e arrancando um rugido doloroso de sua garganta.")
                    escrever_frase(golpe2_3_2)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -2 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 2)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")		
                
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break
            
            verificar_estado_combate(vidas_jogador, vidas_draconato)
            
##################################### <QUESTÃO 4> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO VIII: Quais são os operadores relacionais em ordem?")
            opcoes8 = ('''
[1] > & >= & < & <= & == & !=
[2] > & => & < & >= & = & !=
[3] >> & >= & < $ <= & += & !+ ''')
            escrever_texto(opcoes8)
            # [1] CORRETA 

            while True:
                print("\n")
                resposta4_cap2 = input("Digite aqui a sua resposta: ")
                if resposta4_cap2 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe2_4_1 = ("Uma explosão de fogo consome o draconato, queimando suas escamas e deixando-o contorcendo-se de dor.")
                    escrever_frase(golpe2_4_1)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                
                elif resposta4_cap2 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_4_2 = ("Uma série de golpes rápidos e furiosos o atinge, fazendo você recuar a cada impacto e testando sua resistência.")
                    escrever_frase(golpe2_4_2)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                
                elif resposta4_cap2 == '3':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe2_4_3 = ("Uma explosão de energia desencadeada pelo adversário faz com que seu corpo seja arremessado para trás, deixando-o atordoado e com dores intensas.")
                    escrever_frase(golpe2_4_3)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <PERGUNTAS - CAP 3> #####################################
##################################### <QUESTÃO 1> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO IX: Qual desses códigos está em Python?")
            opcoes9 = ('''
1        a) do{
2        comando1;
3        comando2;
4    } while(condicao);

1        b) while True:
2            comando1
3            comando2
4            if condicao:
5                break

[1] B
[2] A ''')
            escrever_texto(opcoes9)
            #CORRETA B
            while True:
                print("\n")
                resposta1_cap3 = input("Digite aqui a sua reposta: ")
                if resposta1_cap3 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe3 = ("O draconato é envolvido por uma rajada de vento cortante, rasgando suas escamas e causando feridas que ardem intensamente, desafiando sua resistência.")
                    escrever_frase(golpe3)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                elif resposta1_cap3 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe3_1 = ("O inimigo acerta um golpe preciso em seu ponto fraco, causando uma dor lancinante que quase o faz perder o fôlego.")
                    escrever_frase(golpe3_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <QUESTÃO 2> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO X: Termine a frase - 'Contadores são sempre do tipo....:")
            opcoes10 = ('''
[1] binário
[2] decimal
[3] inteiro ''')
            escrever_texto(opcoes10)
            #[3] CORRETA

            while True:
                print("\n")
                resposta2_cap3 = input("Digite aqui a sua resposta: ")
                if resposta2_cap3 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe3_2_1 = ("Um feitiço sombrio é lançado contra você, envolvendo-o em chamas negras que queimam sua pele e enfraquecem sua determinação.")
                    escrever_frase(golpe3_2_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -2 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 2)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta2_cap3 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe3_2_2 = ("O ataque inimigo encontra seu alvo com precisão, causando uma dor lancinante que se espalha pelo corpo do paladino como uma chama ardente.")
                    escrever_frase(golpe3_2_2)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta2_cap3 == '3':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe3_2_3 = ("Um veneno venenoso se infiltra no corpo do draconato, enfraquecendo-o gradualmente e fazendo-o sentir uma dor lancinante em cada movimento.")
                    escrever_frase(golpe3_2_3)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)


##################################### <QUESTÃO 3> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO XI: Esse código está errado?")
            opcoes11 = ('''
1            contador = 0
2
3            while contador < 10
4                print(contador)
5                contador += 1

[1] Sim
[2] Não ''')
            escrever_texto(opcoes11)

            #[1] CORRETA

            while True:
                print("\n")
                resposta2_cap3 = input("Digite aqui a sua resposta: ")
                if resposta2_cap3 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe3_3_2 = ("Um ataque mágico atinge o paladino com força, envolvendo-o em uma aura de dor pulsante que desafia sua tenacidade.")
                    escrever_frase(golpe3_3_2)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta2_cap3 == '2':
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe3_3_1 = ("Um golpe direto no ponto fraco do draconato faz com que ele solte um grunhido de agonia, lutando para se manter de pé diante do impacto.")
                    escrever_frase(golpe3_3_1)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break

            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <QUESTÃO 4> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO XII: Qual comando deve ser utilizado para sair do loop infinito a baixo e continuar a execução do código?")
            print("<Tiramos a pergunta de uma prova do Professor Howard!>")
            opcoes12 = ('''
            ...

    while True:

        ...

    ...


[1] default
[2] break
[3] return 0 ''')
            escrever_texto(opcoes12)
            #[2] CORRETA

            while True:
                print("\n")
                resposta2_cap3 = input("Digite aqui a sua resposta: ")
                if resposta2_cap3 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe3_4_1 = ("O inimigo desfere um golpe surpreendentemente poderoso, fazendo o paladino grunhir de dor e lutando para manter sua postura firme diante do impacto.")
                    escrever_frase(golpe3_4_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -3 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 3)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta2_cap3 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe3_4_2 = ("Um golpe poderoso desfere um estrondo ensurdecedor contra o corpo do draconato, deixando-o cambaleando sob a dor excruciante.")
                    escrever_frase(golpe3_4_2)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -2 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 2)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                elif resposta2_cap3 == '3':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe3_4_1 = ("Um golpe violento penetra a armadura do paladino, causando um impacto doloroso que o faz cambalear momentaneamente.")
                    escrever_frase(golpe3_4_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -2 de vida﹞")
                    print("\n")
                    time.sleep(1)
                    vidas_jogador = diminuir_vida(vidas_jogador, 2)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break
            
            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <PERGUNTAS - CAP 4> #####################################
##################################### <QUESTÃO 1> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO XII: O que é vetor?")
            opcoes13 = ('''
[1] Caracterizam as grandezas vetoriais, que são as grandezas que precisam de orientação.
[2] É uma variável composta homogênea unidimensional. ''')
            escrever_texto(opcoes13)
            #[2] CORRETA
            while True:
                print("\n")
                resposta1_cap4 = input("Digite aqui a sua resposta: ")
                if resposta1_cap4 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe4_1 = ("Um golpe incisivo corta através da defesa do Paladino, causando uma dor aguda que o faz grunhir de aflição.")
                    escrever_frase(golpe4_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta1_cap4 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe4_2 = ("Uma série de ataques rápidos e precisos atinge o draconato, deixando-o atordoado e desorientado sob a dor incessante.")
                    escrever_frase(golpe4_2)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break
            
            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <QUESTÃO 2> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            time.sleep(1)
            print("QUESTÃO XIV: Como podemos dizer que o vetor é uma variável?")
            opcoes14 = ('''
[1] Inserir um valor
[2] Colocar um sufixo ''')
            escrever_texto(opcoes14)
            #[2] CORRETO
            
            while True:
                print("\n")
                resposta1_cap4 = input("Digite aqui sua resposta: ")
                if resposta1_cap4 == '1':
                    time.sleep(1)
                    print("\n")
                    print("Reposta Errada!")
                    print("\n")
                    golpe4_2_1 = ("O impacto do golpe é como um martelo implacável, deixando o paladino atordoado e enfrentando uma onda de dor debilitante.")
                    escrever_frase(golpe4_2_1)
                    print("\n")
                    time.sleep(0.8)
                    print(f"﹝{nome} sofreu -1 de vida﹞")
                    print("\n")
                    vidas_jogador = diminuir_vida(vidas_jogador, 1)
                    print(f"⌯ {nome} ⌯")
                    print(f"♡︲Vida: {vidas_jogador}/10")
                    print("\n")
                elif resposta1_cap4 == '2':
                    time.sleep(1)
                    print("\n")
                    print("Resposta Correta!")
                    print("\n") 
                    golpe4_2_2 = ("O draconato é envolvido por uma rajada de vento cortante, rasgando suas escamas e causando feridas que ardem intensamente, desafiando sua resistência.")
                    escrever_frase(golpe4_2_2)
                    print("\n")
                    time.sleep(0.8)
                    print("﹝Draconato sofreu -1 de vida﹞")
                    print("\n")
                    print("⌯ Draconato ⌯")
                    vidas_draconato = diminuir_vida(vidas_draconato, 1)
                    print(f"♡︲ Vida: {vidas_draconato}/10")
                    print("\n")
                else:
                    print("\n")
                    print("Opção inválida! Digite novamente!")
                    continue
                break
            
            verificar_estado_combate(vidas_jogador, vidas_draconato)

##################################### <QUESTÃO DECISIVA> #####################################
            print("─────────────────────────────────────────────────────────────────────")
            print("\n")
            print('''Após uma batalha brutal, você e o Draconato, cobertos de feridas, juntam suas forças para desferir um último golpe contra um inimigo poderoso. 
Combinando as habilidades do Paladino e o poder elemental do Draconato, vocês avançam com determinação... ''')
            print("\n")
            time.sleep(1)
            print("QUESTÃO FINAL: Qual o erro neste código?")
            opcaofinal = ('''
1            vet_des = [5, 3, 1, 4, 2]
2
3        for i in range(len(vet_des)):
4            for j in range(i, len(vet_des) - 1):
5                if vet_des[i] > vet_des[j+1]:
6                    vet_des[i], vet_des[j] = vet_des[j], vet_des[i] 
            
[1] Linha 3: Deveria ser 'for in range(len(vet_des)):'
[2]' Linha 6: No 'vet_des[j]' deveria ser [j+1]  ''')
            escrever_texto(opcaofinal)
            #CORRETA 2

            while True:
                print("\n")
                ultima_resposta = input("Digite aqui sua última resposta: ")
                if ultima_resposta == '1':
                    printar_derrota()
                elif ultima_resposta == '2':
                    printar_vitoria()
                else:
                    print("\n")
                    print("Não deixe seu inimigo reconhecer suas fraquezas! Digite novamente, rápido!")
                    continue
                sys.exit()
            ##DESEMPATE##
        else:
            print("\n")
            print("Opção inválida!")
            print("Retornando ao Menu Principal")
            break
##################################### <Fim do Combate> #####################################