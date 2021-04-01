import ply.yacc as yacc
import ply.lex as lex    
import sys
 

tokens = (
    'NAME', 'NUMBER', 'INT', 'FLOAT','FLOATTYPE', 'BOOL', 'STRING', 'STRINGTYPE', 'VOID', 'COMMA',
    'AND', 'OR', 'EQUALS', 'SAMEAS', 'NEQUAL', 'HEQUAL', 'LEQUAL', 'RBRACK', 'LBRACK',
    'HIGHER', 'LOWER', 'SUM', 'SUB', 'MULTIPLY', 'DIVIDE', 
    'RESTOF', 'DECLARATION', 'DEFINITION', 
    'RETURN', 'IF', 'ELSE', 'WHILE', 'LCURLY', 'RCURLY', 'LPAR',
    'RPAR', 'TRUE', 'FALSE', 'SEMICOLON', 'COLON', 'QMARK', 'DIFFER', 
    )

#Variables
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_STRING = r'"[a-zA-Z0-9/]*"'


#Binary operators
t_AND= r'&&'
t_OR= r'\|\|'
t_EQUALS = r'='
t_SAMEAS= r'=='
t_NEQUAL= r'!='
t_HEQUAL= r'>='
t_LEQUAL= r'<='
t_HIGHER= r'\>'
t_LOWER= r'\<'
t_SUM= r'\+'
t_SUB= r'-'
t_MULTIPLY= r'\*'
t_DIVIDE= r'/'
t_RESTOF= r'\%'


t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_QMARK = r'"'

#Punctuation
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_DIFFER = r'!'

def t_INT(t):
    r'Int'
    return t

def t_FLOATTYPE(t):
    r'Float'
    return t

def t_BOOL(t):
    r'Boolean'
    return t

def t_STRINGTYPE(t):
    r'String'
    return t

def t_VOID(t):
    r'Void'
    return t

#Boolean
def t_TRUE(t):
    r'True'
    return t

def t_FALSE(t):
    r'False'
    return t



def t_RETURN(t):
    r'return'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t



def t_DECLARATION(t):
    r'decl'
    return t

def t_DEFINITION(t):
    r'def'
    return t



def t_FLOAT(t):
    r'([0-9])*.([0-9])+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_NUMBER(t):
    r'[0-9]([0-9]|_)*'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


#error handling
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

#new line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


#Discarted tokens 
t_ignore_COMMENT = r'\#.*'

#ignore
t_ignore = r' | ' #space, tab and enter

lexer = lex.lex()

precedence = (
    ('left', 'AND', 'OR'),
    ('nonassoc', 'LOWER', 'HIGHER', 'HEQUAL', 'LEQUAL', 'NEQUAL', 'SAMEAS', 'DIFFER'),
    ('left','SUM','SUB'),
    ('left','MULTIPLY','DIVIDE', 'RESTOF'),
    )

# Error rule for syntax errors
def p_program(t):
    '''program : DECLARATION declaration
               | DEFINITION definition
               | DECLARATION declaration program
               | DEFINITION definition program'''

def p_types(t):
    '''types :    INT 
                | FLOATTYPE 
                | BOOL 
                | STRINGTYPE'''

def p_declaration(t):
    '''declaration : NAME LPAR dargument RPAR COLON types
                    | NAME LPAR dargument RPAR COLON VOID 
                    | NAME LPAR RPAR COLON types 
                    | NAME LPAR RPAR COLON VOID '''

def p_definition(t):
    '''definition : NAME LPAR dargument RPAR COLON types block
                    | NAME LPAR RPAR COLON types block
                    | NAME LPAR RPAR COLON VOID block
                    | NAME LPAR dargument RPAR COLON VOID block '''

def p_d_argument(t):
    '''dargument :   NAME COLON types
                  | NAME COLON types COMMA dargument '''

#############################################################################################################


def p_block(t):
    '''block : LCURLY RCURLY
            | LCURLY block_content RCURLY'''

def p_block_content(t):
    '''block_content : statement  
                    | statement block_content '''

def p_return_statement(t):
    '''statement : RETURN SEMICOLON 
                | RETURN expression SEMICOLON'''

def p_ifelse_statement(t):
    '''statement : IF expression block
                | IF expression block ELSE block '''

def p_while_statement(t):
    '''statement : WHILE expression block'''

def p_var_decl_statment(t):
    '''statement : NAME COLON types EQUALS expression SEMICOLON
                 | NAME COLON types EQUALS QMARK STRING QMARK SEMICOLON'''

def p_var_assign_statment(t):
    '''statement : NAME EQUALS expression SEMICOLON
                 | NAME EQUALS QMARK STRING QMARK SEMICOLON'''

############################################################################################################

def p_statement_expr(t):
   '''statement : expression'''

def p_expression_binop(t):
     '''expression : expression SUM expression
                  | expression SUB expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression RESTOF expression
                  | expression SAMEAS expression
                  | expression NEQUAL expression
                  | expression HEQUAL expression
                  | expression LEQUAL expression
                  | expression HIGHER expression
                  | expression LOWER expression 
                  | expression AND expression
                  | expression OR expression'''

def p_expression_bool(t):
    '''expression : TRUE 
                | FALSE'''

def p_expression_nuo(t):
    '''expression : DIFFER expression'''

def p_expression_int(t):
    'expression : NUMBER'

def p_expression_float(t):
    '''expression : FLOAT'''

def p_expression_string(t):
    '''expression : STRING'''

def p_expression_name(t):
    'expression : NAME'

def p_expression_index(t):
    'expression : NAME LBRACK expression RBRACK'

def p_expression_index_fun(t):
    '''expression :  NAME LPAR RPAR LBRACK expression RBRACK
                    | NAME LPAR argument RPAR LBRACK expression RBRACK '''

def p_expression_fun_invoc(t):
    'expression : NAME LPAR argument RPAR'

def p_argument(t):
    '''argument :   expression
                  | expression COMMA expression '''

##################################################################################################################
def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

def p_error(t):
    if t != None:
        print("Syntax error at '%s', line %s, column %s" % (t.value, t.lineno, find_column(code, t)))
    else: 
        print("Syntax error at '%s'" % t)
    
parser = yacc.yacc()

try:
    with open(sys.argv[1]) as inputfile:
        code = inputfile.read()
        print(code)
        parser.parse(code)  
except EOFError:
    print("Unable to read file")
