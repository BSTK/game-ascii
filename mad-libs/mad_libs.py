"""
Game: Mad Libs - Histórias Loucas
Video: https://www.youtube.com/watch?v=tWnyBD2src0&t=2159s
"""
import random
import shutil

FONT_BOLD = '\033[1m'
FONT_NORMAL = '\033[0m'
FONT_AZUL = '\033[38;5;33m'
FONT_ROSA = '\033[38;5;200m'
FONT_AMARELA = '\033[38;5;226m'
FONT_UNDERLINE = '\033[4m'

CARTAS = f"""
{ FONT_BOLD }
┌───────────────┐┌────────────────┐┌────────────────┐┌────────────────┐ 
│  ADJETIVOS    ││      VERBO     ││     VERBO      ││ SUBSTANTIVOS   │ 
|───────────────||────────────────||────────────────||────────────────| 
│ ○ pobre       ││  ○ baixar      ││   ○ afastando  ││  ○ plantas     │ 
│ ○ lindo       ││  ○ cuidando    ││   ○ ama        ││  ○ pessoas     │ 
│ ○ brilhante   ││  ○ achando     ││   ○ Tornei-me  ││  ○ casa        │ 
│ ○ deveria     ││  ○ fazer       ││   ○ trabalhar  ││  ○ f de semana │ 
│               ││                ││                ││                │ 
└───────────────┘└────────────────┘└────────────────┘└────────────────┘ 
{ FONT_NORMAL }
"""

terminal_size = shutil.get_terminal_size().columns


def texto_centralizado(texto: str):
    print(texto.center(terminal_size))


print('\n')


print(f'{ FONT_AMARELA }')
texto_centralizado('░░█████   █████              █████    █████      ████████ \n')
texto_centralizado('░░██████ ██████             ░░███    ░░███      ░░░░░███ \n')
texto_centralizado('░░███░█████░███  ██████   ███████     ░███      ████░██████░░░█████\n')
texto_centralizado('░░███░░███ ░███ ░░░░░███ ███░░███     ░███     ░░███░███░░ ██  ████░░\n')
texto_centralizado('░░███ ░░░  ░███  ███████░███ ░███     ░███      ░███░███ ░ ██░░█████\n')
texto_centralizado('░░███      ░███ ███░░███░███ ░███     ░███      ░███░███ ░ ██░░░░███\n')
texto_centralizado('░█████     ████░░███████░░████████    ██████████████████████ ██████\n')
print(f'{ FONT_NORMAL }')

print()
print(CARTAS)
print()

verbo_A = input('Informe um verbo: ')
verbo_B = input('Informe um verbo: ')
adjetivo = input('Informe um adjetivo: ')
substantivo = input('Informe um substantivo (plural): ')

print('\n')

verbo_A_formatado = f'{ FONT_BOLD }{ FONT_AMARELA }{ FONT_UNDERLINE }{ verbo_A.upper() }{ FONT_NORMAL }'
verbo_B_formatado = f'{ FONT_BOLD }{ FONT_AMARELA }{ FONT_UNDERLINE }{ verbo_B.upper() }{ FONT_NORMAL }'
adjetivo_formatado = f'{ FONT_BOLD }{ FONT_ROSA }{ FONT_UNDERLINE }{ adjetivo.upper() }{ FONT_NORMAL }'
substantivo_formatado = f'{ FONT_BOLD }{ FONT_AZUL }{ FONT_UNDERLINE }{ substantivo.upper() }{ FONT_NORMAL }'

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

print(historia_louca)
print('\n')
