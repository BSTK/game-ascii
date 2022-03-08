"""
Game: Mad Libs - Histórias Loucas
Video: https://www.youtube.com/watch?v=tWnyBD2src0&t=2159s
"""
import random

import cores

font = cores.Font()
cores = cores.Cores()

CARTAS = f"""
{ font.BOLD }
{ cores.ROSA }\t┌───────────────┐{ cores.AMARELA }┌────────────────┐┌────────────────┐{ cores.AZUL }┌────────────────┐ 
{ cores.ROSA }\t│  ADJETIVOS    │{ cores.AMARELA }│      VERBO     ││     VERBO      │{ cores.AZUL }│ SUBSTANTIVOS   │ 
{ cores.ROSA }\t|───────────────|{ cores.AMARELA }|────────────────||────────────────|{ cores.AZUL }|────────────────| 
{ cores.ROSA }\t│ ○ pobre       │{ cores.AMARELA }│  ○ baixar      ││   ○ afastando  │{ cores.AZUL }│  ○ plantas     │ 
{ cores.ROSA }\t│ ○ lindo       │{ cores.AMARELA }│  ○ cuidando    ││   ○ ama        │{ cores.AZUL }│  ○ pessoas     │ 
{ cores.ROSA }\t│ ○ brilhante   │{ cores.AMARELA }│  ○ achando     ││   ○ Tornei-me  │{ cores.AZUL }│  ○ casa        │ 
{ cores.ROSA }\t│ ✔ deveria     │{ cores.AMARELA }│  ○ fazer       ││   ○ trabalhar  │{ cores.AZUL }│  ○ f de semana │ 
{ cores.ROSA }\t│               │{ cores.AMARELA }│                ││                │{ cores.AZUL }│                │ 
{ cores.ROSA }\t└───────────────┘{ cores.AMARELA }└────────────────┘└────────────────┘{ cores.AZUL }└────────────────┘ 
{ font.NORMAL }
"""

print(f'{ cores.AMARELA }')
print(f'\t░░█████   █████              █████    █████      ████████ \n')
print(f'\t░░██████ ██████             ░░███    ░░███      ░░░░░███ \n')
print(f'\t░░███░█████░███  ██████   ███████     ░███      ████░██████░░░█████\n')
print(f'\t░░███░░███ ░███ ░░░░░███ ███░░███     ░███     ░░███░███░░ ██  ████░░\n')
print(f'\t░░███ ░░░  ░███  ███████░███ ░███     ░███      ░███░███ ░ ██░░█████\n')
print(f'\t░░███      ░███ ███░░███░███ ░███     ░███      ░███░███ ░ ██░░░░███\n')
print(f'\t░█████     ████░░███████░░████████    ██████████████████████ ██████\n')
print(f'{ font.NORMAL }')

print(CARTAS)

verbo_A = input('\tInforme um verbo: ')
verbo_B = input('\tInforme um verbo: ')
adjetivo = input('\tInforme um adjetivo: ')
substantivo = input('\tInforme um substantivo (plural): ')

print('\n')

verbo_A_formatado = f'{ font.BOLD }{ cores.AMARELA }{ font.UNDERLINE }{ verbo_A.upper() }{ font.NORMAL }'
verbo_B_formatado = f'{ font.BOLD }{ cores.AMARELA }{ font.UNDERLINE }{ verbo_B.upper() }{ font.NORMAL }'
adjetivo_formatado = f'{ font.BOLD }{ cores.ROSA }{ font.UNDERLINE }{ adjetivo.upper() }{ font.NORMAL }'
substantivo_formatado = f'{ font.BOLD }{ cores.AZUL }{ font.UNDERLINE }{ substantivo.upper() }{ font.NORMAL }'

historias_loucas = [

    # adjetivo - pobre / verbo_a - baixar / verbo_b - afastando / substantivo - plantas
    f'\t-> Não basta ser { adjetivo_formatado }. '
    f'Tem de { verbo_A_formatado } o volume da TV pra escutar quando tem briga no vizinho.\n'
    f'\t-> Estou me { verbo_B_formatado } de tanta gente, que daqui a uns dias a solução vai '
    f'ser conversar com as { substantivo_formatado }.',

    # adjetivo - lindo / verbo_a - cuidando / verbo_b - ama / substantivo - pessoas
    f'\t-> Se quem { verbo_B_formatado } cuida, muita gente deve me amar. Porque o que tem de '
    f'{ substantivo_formatado } { verbo_A_formatado } da minha vida não é brincadeira!\n'
    f'\t-> Certas { substantivo_formatado } são como nuvens. Quando somem, o dia fica '
    f'{ adjetivo_formatado }!',

    # adjetivo - brilhante / verbo_a - achando / verbo_b - Tornei-me / substantivo - casa
    f'\t-> Tem muita testa oleosa { verbo_A_formatado } que é mente { adjetivo_formatado }.\n'
    f'\t-> { verbo_B_formatado } o que eu mais temia: quem desmarca o rolê para ficar em '
    f'{ substantivo_formatado }.',

    # adjetivo - deveria / verbo_a - fazer /verbo_b - trabalhar / substantivo - final de semana
    f'\t-> O { substantivo_formatado } { adjetivo_formatado } levar uma multa por excesso de velocidade.\n'
    f'\t-> Deve ser muito chique { verbo_B_formatado }, estudar, '
    f'{ verbo_A_formatado } academia e ainda conseguir dormir bem.',
]

indice_aleatorio = random.randint(0, len(historias_loucas))
historia_louca = historias_loucas[indice_aleatorio]

print(f'\t{historia_louca}')
print('\n')
