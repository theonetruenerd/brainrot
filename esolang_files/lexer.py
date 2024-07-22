import ply.lex as lex

# List of token names. This is always required
tokens = (
    'HIGHKEY', 'LOWKEY', 'IDENTIFIER', 'NUMBER', 'STRING', 'ASSIGN', 'LPAREN', 'RPAREN',
    'SEMICOLON', 'VIBECHECK', 'BIGYIKES', 'LEFTPILLED', 'RIGHTMAXXER', 'SHOUTOUT', 'FUCKAROUND',
    'FINDOUT', 'ITSGIVING', 'SPILLTEA', 'YAP', 'YEET', 'RATIOS','GRIND','CAP','NOCAP','GG','PERIODT',
    'TEA','CRINGE','BRUH','REDFLAG','BODYCOUNT','SLEPTON','STAN','NPC','IYKYK','SITUATIONSHIP','HOOKUP',
    'BASED','POURTEA','OOF','ICK','TWEAKING','SNEAKYLINK','BFFR','HOMIES','RUNATRAIN','GETYOURBOY','NOHOMO',
    'MANDEM','COMMA','MID','COOK','BET','BASIC','LEADON','GHOST','UWU','WHATSTHIS','ROMANEMPIRE','ATE','SKIBIDI',
    'VALID','GAGGED'
)

# Regular expression rules for simple tokens
def t_HIGHKEY(t):
    r'highkey'
    return t

def t_LOWKEY(t):
   r'lowkey'
   return t

def t_VIBECHECK(t):
    r'vibe_check'
    return t

def t_BIGYIKES(t):
    r'big_yikes'
    return t

def t_LEFTPILLED(t):
    r'leftpilled'
    return t

def t_RIGHTMAXXER(t):
    r'rightmaxxer'
    return t

def t_SHOUTOUT(t):
    r'shoutout'
    return t

def t_FUCKAROUND(t):
    r'fuck_around'
    return t

def t_FINDOUT(t):
    r'find_out'
    return t

def t_ITSGIVING(t):
    r'its_giving'
    return t

def t_SPILLTEA(t):
    r'spill_tea'
    return t

def t_YAP(t):
    r'yap'
    return t

def t_YEET(t):
    r'yeet'
    return t

def t_RATIOS(t):
    r'ratios'
    return t

def t_GRIND(t):
    r'grind'
    return t

def t_CAP(t):
    r'cap'
    return t

def t_NOCAP(t):
    r'no_cap'
    return t

def t_GG(t):
    r'gg'
    return t

def t_PERIODT(t):
    r'periodt'
    return t

def t_TEA(t):
    r'tea'
    return t

def t_CRINGE(t):
    r'cringe'
    return t

def t_BRUH(t):
    r'bruh'
    return t

def t_REDFLAG(t):
    r'redflag'
    return t

def t_BODYCOUNT(t):
    r'bodycount'
    return t

def t_SLEPTON(t):
    r'slept_on'
    return t

def t_STAN(t):
    r'stan'
    return t

def t_NPC(t):
    r'npc'
    return t

def t_IYKYK(t):
    r'iykyk'
    return t

def t_SITUATIONSHIP(t):
    r'situationship'
    return t

def t_HOOKUP(t):
    r'hooks_up_with'
    return t

def t_BASED(t):
    r'based'
    return t

def t_POURTEA(t):
    r'pour_tea'
    return t

def t_OOF(t):
    r'oof'
    return t

def t_TWEAKING(t):
    r'tweaking'
    return t

def t_ICK(t):
    r'ick'
    return t

def t_SNEAKYLINK(t):
    r'sneaky_link'
    return t

def t_BFFR(t):
    r'bffr'
    return t

def t_HOMIES(t):
    r'homies'
    return t

def t_RUNATRAIN(t):
    r'run_a_train_on'
    return t

def t_GETYOURBOY(t):
    r'get_your_boy'
    return t

def t_NOHOMO(t):
    r'no_homo_tho'
    return t

def t_MANDEM(t):
    r'mandem'
    return t

def t_MID(t):
    r'mid'
    return t

def t_COOK(t):
    r'cook'
    return t

def t_BET(t):
    r'bet'
    return t

def t_BASIC(t):
    r'basic'
    return t

def t_GHOST(t):
    r'ghost'
    return t

def t_LEADON(t):
    r'lead_on'
    return t

def t_UWU(t):
    r'uwu'
    return t

def t_WHATSTHIS(t):
    r'whats_this'
    return t

def t_ROMANEMPIRE(t):
    r'roman_empire'
    return t

def t_ATE(t):
    r'ate'
    return t

def t_SKIBIDI(t):
    r'skibidi'
    return t

def t_VALID(t):
    r'valid'
    return t

def t_GAGGED(t):
    r'gagged'
    return t

# Regular expression rules for simple tokens
def t_ASSIGN(t):
    r'='
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^\\"]|\\.)*"'
    t.value = t.value[1:-1]
    return t

def t_COMMA(t):
    r','
    return t

# Define a dictionary of reserved words for the lexer
reserved = {
    'aura': 'AURA',
    'banger': 'BANGER',
    'brainrot': 'BRAINROT',
    'cook': 'COOK',
    'cooked': 'COOKED',
    'era': 'ERA',
    'fanum_tax': 'FANUMTAX',
    'fit': 'FIT',
    'gatekeep': 'GATEKEEP',
    'gaslight': 'GASLIGHT',
    'girlboss': 'GIRLBOSS',
    'goat': 'GOAT',
    'gyat': 'GYAT',
    'oop': 'OOP',
    'karen': 'KAREN',
    'lit': 'LIT',
    'mew': 'MEW',
    'oomf': 'OOMF',
    'opp': 'OPP',
    'owned': 'OWNED',
    'rizz': 'RIZZ',
    'salty': 'SALTY',
    'shook': 'SHOOK',
    'sigma': 'SIGMA',
    'simp': 'SIMP',
    'skibidi': 'SKIBIDI',
    'slaps': 'SLAPS',
    'slay': 'SLAY',
    'snatched': 'SNATCHED',
    'sus': 'SUS',
    'touch_grass': 'TOUCHGRASS',
    'wig': 'WIG'
}

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
