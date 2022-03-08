FONT_BOLD = '\033[1m'
FONT_NORMAL = '\033[0m'
FONT_AZUL = '\033[38;5;33m'
FONT_ROSA = '\033[38;5;200m'
FONT_AMARELA = '\033[38;5;226m'
FONT_UNDERLINE = '\033[4m'

CARTAS = f"""
{FONT_BOLD}
{FONT_ROSA}\t┌───────────────┐{FONT_AMARELA}┌────────────────┐┌────────────────┐{FONT_AZUL}┌────────────────┐ 
{FONT_ROSA}\t│  ADJETIVOS    │{FONT_AMARELA}│      VERBO     ││     VERBO      │{FONT_AZUL}│ SUBSTANTIVOS   │ 
{FONT_ROSA}\t|───────────────|{FONT_AMARELA}|────────────────||────────────────|{FONT_AZUL}|────────────────| 
{FONT_ROSA}\t│ ○ pobre       │{FONT_AMARELA}│  ○ baixar      ││   ○ afastando  │{FONT_AZUL}│  ○ plantas     │ 
{FONT_ROSA}\t│ ○ lindo       │{FONT_AMARELA}│  ○ cuidando    ││   ○ ama        │{FONT_AZUL}│  ○ pessoas     │ 
{FONT_ROSA}\t│ ○ brilhante   │{FONT_AMARELA}│  ○ achando     ││   ○ Tornei-me  │{FONT_AZUL}│  ○ casa        │ 
{FONT_ROSA}\t│ ✔ deveria     │{FONT_AMARELA}│  ○ fazer       ││   ○ trabalhar  │{FONT_AZUL}│  ○ f de semana │ 
{FONT_ROSA}\t│               │{FONT_AMARELA}│                ││                │{FONT_AZUL}│                │ 
{FONT_ROSA}\t└───────────────┘{FONT_AMARELA}└────────────────┘└────────────────┘{FONT_AZUL}└────────────────┘ 
{FONT_NORMAL}
"""


def mostar():
    print(CARTAS)


class Cartas():

    def __init__(self):
        None
