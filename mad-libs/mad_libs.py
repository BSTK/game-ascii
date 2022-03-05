"""
Game: Mad Libs - Histórias Loucas
"""

FONT_BOLD = '\033[1m'
FONT_NORMAL = '\033[0m'
FONT_AZUL = '\033[38;5;33m'
FONT_ROSA = '\033[38;5;200m'
FONT_AMARELA = '\033[38;5;226m'
FONT_UNDERLINE = '\033[4m'

print('\n')

verbo_A = input('\tInforme um verbo: ')
verbo_B = input('\tInforme um verbo: ')
adjetivo = input('\tInforme um adjetivo: ')
substantivo = input('\tInforme um substantivo (plural): ')

print('\n')

verbo_A_formatado = f'{ FONT_BOLD }{ FONT_AMARELA }{ FONT_UNDERLINE }{ verbo_A.upper() }{ FONT_NORMAL }'
verbo_B_formatado = f'{ FONT_BOLD }{ FONT_AMARELA }{ FONT_UNDERLINE }{ verbo_B.upper() }{ FONT_NORMAL }'
adjetivo_formatado = f'{ FONT_BOLD }{ FONT_ROSA }{ FONT_UNDERLINE }{ adjetivo.upper() }{ FONT_NORMAL }'
substantivo_formatado = f'{ FONT_BOLD }{ FONT_AZUL }{ FONT_UNDERLINE }{ substantivo.upper() }{ FONT_NORMAL }'

historias_loucas = [
    """
        adjetivo - pobre
        verbo_a - baixar
        verbo_b - afastando
        substantivo - plantas
    """
    f'\t-> Não basta ser { adjetivo_formatado }. '
    f'Tem de { verbo_A_formatado } o volume da TV pra escutar quando tem briga no vizinho.'
    f'\t-> Estou me { verbo_B_formatado } de tanta gente, que daqui a uns dias a solução vai '
    f'ser conversar com as { substantivo_formatado }.',

    """
        adjetivo - lindo
        verbo_a - cuidando
        verbo_b - ama
        substantivo - pessoas
    """
    f'\t-> Se quem { verbo_B_formatado } cuida, muita gente deve me amar. Porque o que tem de '
    f'{ substantivo_formatado } { verbo_A_formatado } da minha vida não é brincadeira!'
    f'\t-> Certas { substantivo_formatado } são como nuvens. Quando somem, o dia fica '
    f'{ adjetivo_formatado }!',


    """
        adjetivo - brilhante
        verbo_a - achando
        verbo_b - Tornei-me
        substantivo - casa
    """
    f'\t-> Tem muita testa oleosa { verbo_A_formatado } que é mente { adjetivo_formatado }.'
    f'\t-> { verbo_B_formatado } o que eu mais temia: quem desmarca o rolê para ficar em '
    f'{ substantivo_formatado }.',


    """
        adjetivo - deveria
        verbo_a - fazer
        verbo_b - trabalhar
        substantivo - final de semana
    """
    f'\t-> O { substantivo_formatado } { adjetivo_formatado } levar uma multa por excesso de velocidade.'
    f'\t-> Deve ser muito chique { verbo_B_formatado }, estudar, { verbo_A_formatado } academia e ainda conseguir dormir bem.',


    """
        adjetivo - 
        verbo_a -
        verbo_b - 
        substantivo - espelho
    """
    f'\t-> Espelho, espelho meu... por que as pessoas se preocupam mais com a minha vida do que eu?'
    f'\t-> Até a bateria do meu celular dura mais do que o amor eterno de certas pessoas!'
]

historia_louca = \
    f'\tProgramar é muito ' \
    f'{ adjetivo_formatado }! Sempre me emociona porque me encanta ' \
    f'{ verbo_A_formatado } problemas.\n\tAprendenda a ' \
    f'{ verbo_B_formatado } com freeCodeCamp e alcanse seus (suas) ' \
    f'{ substantivo_formatado }!'

print(historia_louca)
print('\n')
