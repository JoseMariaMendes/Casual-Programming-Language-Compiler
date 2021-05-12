import ply.yacc as yacc
from collections.abc import Iterable
import ply.lex as lex    
import sys
#sys.tracebacklimit = 0
from context import Context
from verify import verify
from compiler import compilador
from emitter import Emitter
 
def list_helper(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, dict):
            for x in list_helper(item):
                yield x
        else:
            yield item

tokens = (
    'NAME', 'NUMBER', 'INT', 'FLOAT','FLOATTYPE', 'BOOL', 'STRING', 'STRINGTYPE', 'VOID', 'COMMA',
    'AND', 'OR', 'EQUALS', 'SAMEAS', 'NEQUAL', 'HEQUAL', 'LEQUAL', 'RBRACK', 'LBRACK',
    'HIGHER', 'LOWER', 'SUM', 'SUB', 'MULTIPLY', 'DIVIDE', 
    'RESTOF', 'DECLARATION', 'DEFINITION', 
    'RETURN', 'IF', 'ELSE', 'WHILE', 'LCURLY', 'RCURLY', 'LPAR',
    'RPAR', 'TRUE', 'FALSE', 'SEMICOLON', 'COLON', 'QMARK', 'DIFFER', 'PRINT', 'GETARRAY',  
    )

#Variables
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_STRING = r'"[a-zA-Z0-9\\]*"'


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
t_LBRACK = r"\["
t_RBRACK = r']'
t_QMARK = r'"'

#Punctuation
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_DIFFER = r'!'

def t_INT(t):
    r'Int'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_GETARRAY(t):
    r'get_array'
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
    r'[0-9]*\.[0-9]+'
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
t_ignore =" \t" #space, tab and enter

lexer = lex.lex()

precedence = (
    ('left', 'AND', 'OR'),
    ('nonassoc', 'LOWER', 'HIGHER', 'HEQUAL', 'LEQUAL', 'NEQUAL', 'SAMEAS', 'DIFFER'),
    ('left','SUM','SUB'),
    ('left','MULTIPLY','DIVIDE', 'RESTOF'),
    )

# Error rule for syntax errors
def p_programb(t):
    '''programb : program'''
    t[0] = {'nt': 'programb', 'program': list(list_helper(t[1]))}

def p_program(t):
    '''program : DECLARATION declaration
               | DEFINITION definition
               | DECLARATION declaration program
               | DEFINITION definition program'''
    if len(t) == 3:
        t[0] = [t[2]]
    elif len(t) == 4:
        t[0] = [t[2],t[3]]

def p_declaration(t):
    '''declaration : NAME LPAR dargument RPAR COLON types
                    | NAME LPAR dargument RPAR COLON VOID 
                    | NAME LPAR RPAR COLON types 
                    | NAME LPAR RPAR COLON VOID 
                    | NAME LPAR RPAR COLON LBRACK types RBRACK
                    | NAME LPAR dargument RPAR COLON LBRACK types RBRACK '''
    if len(t) == 7:
        t[0] = {'nt': 'declaration', 'name': t[1], 'darguments': list(list_helper(t[3])), 'type': t[6]}
    elif len(t) == 6:
        t[0] = {'nt': 'declaration', 'name': t[1], 'darguments': "empty", 'type': t[5]}
    elif len(t) == 8:
        t[0] = {'nt': 'array_declaration', 'name': t[1],'darguments': "empty", 'type': f"{t[5]}{t[6]}{t[7]}"}
    elif len(t) == 9:
        t[0] = {'nt': 'array_declaration', 'name': t[1],'darguments': list(list_helper(t[3])), 'type': f"{t[6]}{t[7]}{t[8]}"}


def p_definition(t):
    '''definition : NAME LPAR dargument RPAR COLON types block
                    | NAME LPAR RPAR COLON types block
                    | NAME LPAR RPAR COLON VOID block
                    | NAME LPAR dargument RPAR COLON VOID block 
                    | NAME LPAR RPAR COLON LBRACK types RBRACK block
                    | NAME LPAR dargument RPAR COLON LBRACK types RBRACK block'''
    if len(t) == 8:
        t[0] = {'nt': 'definition', 'name': t[1], 'darguments': list(list_helper(t[3])), 'type': t[6], 'block': t[7]}
    elif len(t) == 7:
        t[0] = {'nt': 'definition', 'name': t[1],'darguments': "empty", 'type': t[5], 'block': t[6]}
    elif len(t) == 9:
        t[0] = {'nt': 'array_definition', 'name': t[1],'darguments': "empty", 'type': f"{t[5]}{t[6]}{t[7]}", 'block': t[8]}
    elif len(t) == 10:
        t[0] = {'nt': 'array_definition', 'name': t[1],'darguments': list(list_helper(t[3])), 'type': f"{t[6]}{t[7]}{t[8]}", 'block': t[9]}

def p_types(t):
    '''types :    INT 
                | FLOATTYPE 
                | BOOL 
                | STRINGTYPE'''

    t[0] = t[1]

def p_d_argument(t):
    '''dargument :   NAME COLON types
                  | NAME COLON types COMMA dargument '''
    if len(t) == 4:
        t[0] = [{'nt': 'dargument', 'name': t[1], 'type': t[3]}]
    elif len(t) == 6:
        t[0] = [{'nt': 'dargument', 'name': t[1], 'type': t[3]}, t[5]]

def p_array_d_argument(t):
    '''dargument : NAME COLON LBRACK types RBRACK
                  | NAME COLON LBRACK types RBRACK COMMA dargument'''
    if len(t) == 6:
        t[0] = [{'nt': 'array_dargument', 'name': t[1], 'type': f"{t[3]}{t[4]}{t[5]}"}]
    elif len(t) == 8:
        t[0] = [{'nt': 'array_dargument', 'name': t[1], 'type': f"{t[3]}{t[4]}{t[5]}"}, t[7]]


                  
#############################################################################################################


def p_block(t):
    '''block : LCURLY RCURLY
            | LCURLY block_content RCURLY'''
    if len(t) == 4:
        t[0] = {'nt': 'block', 'block_content': list(list_helper(t[2]))}
    if len(t) == 3:
        t[0] = {'nt': 'block', 'block_content': "empty"}

def p_block_content(t):
    '''block_content : statement  
                    | statement block_content '''
    if len(t) == 2:
        t[0] = [t[1]]
    elif len(t) == 3:
        t[0] = [t[1],t[2]]

def p_return_statement(t):
    '''statement : RETURN SEMICOLON 
                | RETURN expression SEMICOLON'''
    if len(t) == 3:
        t[0] = {'nt': 'return_statement', 'expression': 'empty'}
    if len(t) == 4:
        t[0] = {'nt': 'return_statement', 'expression': t[2]}

def p_ifelse_statement(t):
    '''statement : IF expression block
                | IF expression block ELSE block '''
    if len(t) == 4:
        t[0] = {'nt': 'ifelse_statement', 'expression': t[2], 'block': [t[3]]}
    elif len(t) == 6:
        t[0] = {'nt': 'ifelse_statement', 'expression': t[2], 'block': [t[3], t[5]]}

def p_while_statement(t):
    '''statement : WHILE expression block'''
    t[0] = {'nt': 'while_statement', 'expression': t[2], 'block': t[3]}

def p_var_decl_statment(t):
    '''statement : NAME COLON types EQUALS expression SEMICOLON
                | NAME COLON types SEMICOLON'''
    if len(t) == 7:
        t[0] = {'nt': 'var_decl_statment', 'name': t[1], 'type': t[3], 'expression': t[5]}        
    if len(t) == 5:
        t[0] = {'nt': 'var_decl_statment', 'name': t[1], 'type': t[3], 'expression': 'empty'}

def p_var_assign_statment(t):
    '''statement : NAME EQUALS expression SEMICOLON'''
    t[0] = {'nt': 'var_assign_statment', 'name': t[1], 'expression': t[3]}
    
def p_array_decl_statment(t):
    '''statement : NAME COLON LBRACK types RBRACK EQUALS NUMBER SEMICOLON'''
    t[0] = {'nt': 'array_decl_statment', 'name': t[1], 'type': f"{t[3]}{t[4]}{t[5]}", 'size': t[7]}     

def p_array_assign_statment(t):
    '''statement : NAME LBRACK expression RBRACK EQUALS expression SEMICOLON'''
    t[0] = {'nt': 'array_assign_statment', 'index': t[3], 'name': t[1], 'expression': t[6]}

def p_expression_array(t):
    'expression : NAME LBRACK expression RBRACK'
    t[0] = {'nt': 'array_expression', 'name': t[1], 'expression': t[3]}

def p_expression_index_fun(t):
    '''expression :  GETARRAY LPAR RPAR LBRACK expression RBRACK
                    | GETARRAY LPAR argument RPAR LBRACK expression RBRACK '''
    if len(t) == 7:
        t[0] = {"nt": 'expression_index_fun', 'argument': 'empty', 'expression': t[5]}
    elif len(t) == 8:
        t[0] = {"nt": 'expression_index_fun', 'argument': list(list_helper(t[3])), 'expression': t[6]}

def p_expression_fun_invoc(t):
    '''expression : NAME LPAR RPAR
                    | NAME LPAR argument RPAR'''
    if len(t) == 5:
        t[0] = {"nt": 'expression_fun_invoc','name': t[1], 'argument': list(list_helper(t[3]))}
    elif len(t) == 4:
        t[0] = {"nt": 'expression_fun_invoc','name': t[1], 'argument': "empty"}
        
############################################################################################################

def p_statement_expr(t):
   '''statement : expression SEMICOLON'''
   t[0] = {'nt': 'statement_expr', 'expression': t[1]}

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
    t[0] = {'nt': 'binop_expression', 'oper': t[2], 'expression_left': t[1], 'expression_right': t[3]}
    
def p_expression_bool(t):
    '''expression : TRUE 
                | FALSE'''
    t[0] = {'nt': 'bool_expression', 'value': t[1]}

def p_expression_nuo(t):
    '''expression : DIFFER expression'''
    t[0] = {'nt': 'nuo_expression', 'expression': t[2]}

def p_expression_int(t):
    'expression : NUMBER'
    t[0] = {'nt': 'int_expression', 'value': t[1]}

def p_expression_float(t):
    '''expression : FLOAT'''
    t[0] = {'nt': 'float_expression', 'value': t[1]}

def p_expression_string(t):
    '''expression : STRING '''
    t[0] = {'nt': 'string_expression', 'value': t[1]}

def p_expression_name(t):
    'expression : NAME'
    t[0] = {'nt': 'name_expression', 'name': t[1]}

def p_expression_group(t):
    'expression : LPAR expression RPAR'
    t[0] = {'nt': 'group_expression', 'expression': t[2]}

def p_argument(t):
    '''argument :   expression
                  | expression COMMA argument '''
    if len(t) == 2:
        t[0] =  [t[1]]
    elif len(t) == 4:
        t[0] = [t[1], t[3]]

#def p_print(t):
#    '''print : PRINT LPAR expression RPAR 
#    '''
#    pass
        
##################################################################################################################
def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

def p_error(t):
    if t != None:
        print("Syntax error at '%s', line %s, column %s" % (t.value, t.lineno, find_column(code, t)))
        exit()
    else: 
        print("Syntax error at '%s'" % t)
        exit()

parser = yacc.yacc()

try:
    with open(sys.argv[1]) as inputfile:
        code = inputfile.read()
        print(code)
        verify(Context(), parser.parse(code))
        codigo_llvm = compilador(parser.parse(code))
        print("\n" + codigo_llvm)

        with open("code.ll", "w") as f:
            f.write(codigo_llvm)
        import subprocess

        # /usr/local/opt/llvm/bin/lli code.ll
        r = subprocess.call(
            "/usr/bin/llc code.ll && clang code.s -o code && ./code",
            shell=True,
        )
        print("Return code", r)

except EOFError:
    print("Unable to read file")