import ply.yacc as yacc
from collections.abc import Iterable
import ply.lex as lex    
import sys
 

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
    r'\d*.\d+'
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
                    | NAME LPAR RPAR COLON VOID '''
    if len(t) == 7:
        t[0] = {'nt': 'declaration', 'name': t[1], 'darguments': list(list_helper(t[3])), 'type': t[6]}
    elif len(t) == 6:
        t[0] = {'nt': 'declaration', 'name': t[1], 'darguments': "empty", 'type': t[5]}


def p_definition(t):
    '''definition : NAME LPAR dargument RPAR COLON types block
                    | NAME LPAR RPAR COLON types block
                    | NAME LPAR RPAR COLON VOID block
                    | NAME LPAR dargument RPAR COLON VOID block '''
    if len(t) == 8:
        t[0] = {'nt': 'definition', 'name': t[1], 'darguments': list(list_helper(t[3])), 'type': t[6], 'block': t[7]}
    elif len(t) == 7:
        t[0] = {'nt': 'definition', 'name': t[1],'darguments': "empty", 'type': t[5], 'block': t[6]}

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

#############################################################################################################


def p_block(t):
    '''block : LCURLY RCURLY
            | LCURLY block_content RCURLY'''
    if len(t) == 4:
        t[0] = {'nt': 'block', 'block_content': list(list_helper(t[2]))}

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
    '''statement : NAME COLON LBRACK types RBRACK SEMICOLON'''
    t[0] = {'nt': 'array_decl_statment', 'name': t[1], 'type': t[3]}     

def p_array_assign_statment(t):
    '''statement : NAME LBRACK expression RBRACK EQUALS expression SEMICOLON'''
    t[0] = {'nt': 'array_assign_statment', 'index': t[3], 'name': t[1], 'expression': t[6]}

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
    t[0] = {'nt': 'binop_expression', 'value': t[2], 'expression_left': t[1], 'expression_right': t[3]}
    
def p_expression_bool(t):
    '''expression : TRUE 
                | FALSE'''
    t[0] = {'nt': 'bool_expression', 'bool': t[1]}

def p_expression_nuo(t):
    '''expression : DIFFER expression'''
    t[0] = ['nuo_expression',t[2]]

def p_expression_int(t):
    'expression : NUMBER'
    t[0] = {'nt': 'int_expression', 'number': t[1]}

def p_expression_float(t):
    '''expression : FLOAT'''
    t[0] = {'nt': 'float_expression', 'float': t[1]}

def p_expression_string(t):
    '''expression : STRING '''
    t[0] = {'nt': 'string_expression', 'string': t[1]}

def p_expression_array(t):
    'expression : NAME LBRACK expression RBRACK'
    t[0] = {'nt': 'array_expression', 'name': t[1], 'expression': t[3]}

def p_expression_name(t):
    'expression : NAME'
    t[0] = {'nt': 'name_expression', 'name': t[1]}

def p_expression_group(t):
    'expression : LPAR expression RPAR'
    t[0] = {'nt': 'group_expression', 'expression': t[2]}

def p_expression_index_fun(t):
    '''expression :  NAME LPAR RPAR LBRACK expression RBRACK
                    | NAME LPAR argument RPAR LBRACK expression RBRACK '''
    if len(t) == 7:
        t[0] = {"nt": 'expression_index_fun','name': t[1], 'argument': 'empty', 'expression': t[5]}
    elif len(t) == 8:
        t[0] = {"nt": 'expression_index_fun','name': t[1], 'argument': [t[3]], 'expression': t[6]}

def p_expression_fun_invoc(t):
    '''expression : NAME LPAR RPAR
                    | NAME LPAR argument RPAR'''
    if len(t) == 5:
        t[0] = {"nt": 'expression_fun_invoc','name': t[1], 'argument': list(list_helper(t[3]))}
    elif len(t) == 4:
        t[0] = {"nt": 'expression_fun_invoc','name': t[1], 'argument': "empty"}

def p_argument(t):
    '''argument :   expression
                  | expression COMMA argument '''
    if len(t) == 2:
        t[0] =  [t[1]]
    elif len(t) == 4:
        t[0] = [t[1], t[3]]
        
##################################################################################################################
def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

def p_error(t):
    if t != None:
        print("Syntax error at '%s', line %s, column %s" % (t.value, t.lineno, find_column(code, t)))
    else: 
        print("Syntax error at '%s'" % t)
    
######################################################################################################################
class TypeError(Exception):
    pass

class Context(object):
    def __init__(self):
        self.stack = [{}]
    
    def get_type(self, name):
        for scope in self.stack:
            if name in scope:
                return scope[name]
        raise TypeError(f"Variavel {name} nao esta no contexto")
    
    def set_type(self, name, value):
        scope = self.stack[0]
        scope[name] = value

    def has_var(self, name):
        for scope in self.stack:
            if name in scope:
                return True
        return False

    def has_var_in_current_scope(self, name):
        return name in self.stack[0]

    def enter_scope(self):
        self.stack.insert(0, {})

    def exit_scope(self):
        self.stack.pop(0)


def verify(ctx:Context, node):
    #print(node)
    #print('-------')
    if node["nt"] == "programb":
        for decl_def in node["program"]:
            verify(ctx, decl_def)
    
    elif node["nt"] == "declaration":
        name = node['name']
        if ctx.has_var(name):
            if 'declaration' in ctx.get_type(name)[0] and 'definition' not in ctx.get_type(name)[0]:
                #declarada mas nao definida
                raise TypeError(f"Funcao {name} ja esta declarada no contexto")
            elif 'declaration' in ctx.get_type(name)[0] and 'definition' in ctx.get_type(name)[0]:
                #declarada e definida
                raise TypeError(f"Funcao {name} ja esta declarada e definidano contexto")
            elif 'declaration' not in ctx.get_type(name)[0] and 'definition' in ctx.get_type(name)[0]:
                #não declarada mas definida
                if len(node['darguments']) > 0:
                    assinatura = ([node['nt']],  node["type"], [[name["name"] for name in node['darguments']],  
                                                                [arg["type"] for arg in node['darguments']]], "function")

                    if ctx.get_type(name)[1] == assinatura[1] and ctx.get_type(name)[2] == assinatura[2]:
                        #o tipo e os argumentos sao iguais
                        assinatura = ctx.get_type(name)
                        assinatura[0].append("declaration")
                        ctx.set_type(name, assinatura)
                    elif ctx.get_type(name)[1] != assinatura[1] and ctx.get_type(name)[2] == assinatura[2]:
                        #o tipo é diferente e os argumentos iguais
                        raise TypeError(f"declaração da funcao {name} tem tipo diferente")
                    elif ctx.get_type(name)[1] == assinatura[1] and ctx.get_type(name)[2] != assinatura[2]:
                        #o tipo é igual e os argumentos diferentes
                        raise TypeError(f"declaração da funcao {name} tem argumentos diferente")
                else:
                    #nao tem argumentos
                    assinatura = ([node['nt']],  node["type"], "empty", "function")

                    if ctx.get_type(name)[1] == assinatura[1] and ctx.get_type(name)[2] == assinatura[2]:
                        #o tipo e os argumentos sao iguais
                        assinatura = ctx.get_type(name)
                        assinatura[0].append("declaration")
                        ctx.set_type(name, assinatura)
                    elif ctx.get_type(name)[1] != assinatura[1] and ctx.get_type(name)[2] == assinatura[2]:
                        #o tipo é diferente e os argumentos iguais
                        raise TypeError(f"declaração da funcao {name} tem tipo diferente da definição")
                    elif ctx.get_type(name)[1] == assinatura[1] and ctx.get_type(name)[2] != assinatura[2]:
                        #o tipo é igual e os argumentos diferentes
                        raise TypeError(f"declaração da funcao {name} tem argumentos diferente da definição")
        else:       
            if node['darguments'] != "empty":
                #não existe o nome
                ctx.set_type("RETURN_CODE", node["type"])

                assinatura = ([node['nt']],  node["type"], [[name["name"] for name in node['darguments']],  
                                                            [arg["type"] for arg in node['darguments']]], "function")
                ctx.set_type(name, assinatura)
            else:
                ctx.set_type("RETURN_CODE", node["type"])
                assinatura = ([node['nt']],  node["type"], "empty", "function")
                ctx.set_type(name, assinatura)
                
    elif node["nt"] == "definition":
        ctx.enter_scope()
        name = node['name']
        if ctx.has_var(name):
            if 'declaration' not in ctx.get_type(name)[0] and 'definition' in ctx.get_type(name)[0]:
                #não declarada mas definida~
                raise TypeError(f"Funcao {name} ja esta definida no contexto")
            elif 'declaration' in ctx.get_type(name)[0] and 'definition' in ctx.get_type(name)[0]:
                #declarada e definida
                raise TypeError(f"Funcao {name} ja esta declarada e definida no contexto")
            elif 'declaration' in ctx.get_type(name)[0] and 'definition' not in ctx.get_type(name)[0]:
                #declarada mas nao definida
                if len(node['darguments']) > 0:
                    assinatura = ([node['nt']],  node["type"], [[name["name"] for name in node['darguments']],  
                                                                [arg["type"] for arg in node['darguments']]], "function")

                    if ctx.get_type(name)[1] == assinatura[1] and ctx.get_type(name)[2] == assinatura[2]:
                        #o tipo e os argumentos sao iguais
                        assinatura = ctx.get_type(name)
                        assinatura[0].append("definition")
                        ctx.set_type(name, assinatura)
                        #adicionar argumentos ao contexto 
                        for arg in node["darguments"]:
                            assinatura = (["var_decl_statment"],  arg["type"], "argumento")
                            ctx.set_type(arg["name"], assinatura)

                    elif ctx.get_type(name)[1] != assinatura[1] and ctx.get_type(name)[2] == assinatura[2]:
                        #o tipo é diferente e os argumentos iguais
                        raise TypeError(f"definição da funcao {name} tem tipo diferente")
                    elif ctx.get_type(name)[1] == assinatura[1] and ctx.get_type(name)[2] != assinatura[2]:
                        #o tipo é igual e os argumentos diferentes
                        raise TypeError(f"definição da funcao {name} tem argumentos diferente")
                else:
                    assinatura = ([node['nt']],  node["type"], "empty", "function")

                    if ctx.get_type(name)[1] == assinatura[1] and ctx.get_type(name)[2] == assinatura[2]:
                        #o tipo e os argumentos sao iguais
                        assinatura = ctx.get_type(name)
                        assinatura[0].append("definition")

                        ctx.set_type(name, assinatura)
                    elif ctx.get_type(name)[1] != assinatura[1] and ctx.get_type(name)[2] == assinatura[2]:
                        #o tipo é diferente e os argumentos iguais
                        raise TypeError(f"definição da funcao {name} tem tipo diferente da declaração")
                    elif ctx.get_type(name)[1] == assinatura[1] and ctx.get_type(name)[2] != assinatura[2]:
                        #o tipo é igual e os argumentos diferentes
                        raise TypeError(f"definição da funcao {name} tem argumentos diferentes da declaração")
        else:
            #não declarada nem definida
            if node['darguments'] != "empty":
                #funçao tem argumentos
                ctx.set_type("RETURN_CODE", node["type"])
                assinatura = ([node['nt']],  node["type"], [[name["name"] for name in node['darguments']],  
                                                            [arg["type"] for arg in node['darguments']]], "function")
                ctx.set_type(name, assinatura)
                #adicionar argumentos ao contexto 
                for arg in node["darguments"]:
                    assinatura = (["var_decl_statment"],  arg["type"], "argumento")
                    ctx.set_type(arg["name"], assinatura)

            else:
                #funçao nao tem argumentos
                ctx.set_type("RETURN_CODE", node["type"])
                assinatura = ([node['nt']],  node["type"], "empty", "function")
                ctx.set_type(name, assinatura)

        
        verify(ctx, node['block'])
        ctx.exit_scope()
    
    elif node["nt"] == "block":
        ctx.enter_scope()
        for statment in node['block_content']:
            verify(ctx, statment)  
        ctx.exit_scope()

    elif node["nt"] == "block_content":
        pass

    elif node["nt"] == "return_statement":
        expression = node['expression']
        if expression != 'empty':
            if verify(ctx, node['expression']) != ctx.get_type("RETURN_CODE"):
                raise TypeError(f"expressao do return nao tem o tipo certo")
        else:
            if ctx.get_type("RETURN_CODE") != "Void":
                raise TypeError(f"expressao do return nao tem o tipo certo")

    elif node["nt"] == "ifelse_statement":
        cond = node["expression"]
        if verify(ctx, cond) != "Boolean":
            raise TypeError(f"Condicao do if {cond} nao e boolean")
        for statment in node["block"]:
            verify(ctx, statment)

    elif node["nt"] == "while_statement":
        cond = node["expression"]
        if verify(ctx, cond) != "Boolean":
            raise TypeError(f"Condicao do while {cond} nao e boolean")
        verify(ctx, node['block'])

    elif node["nt"] == "var_decl_statment":
        name = node['name']
        if ctx.has_var_in_current_scope(name):
            if 'var_decl_statment' in ctx.get_type(name)[0] and 'var_assign_statment' not in ctx.get_type(name)[0]:
                #declarada mas nao definida
                raise TypeError(f"variavel {name} ja esta declarada no contexto")
            elif 'var_decl_statment' in ctx.get_type(name)[0] and 'var_assign_statment' in ctx.get_type(name)[0]:
                #declarada e definida
                raise TypeError(f"variavel {name} ja esta declarada e definida no contexto")
            elif 'var_decl_statment' not in ctx.get_type(name)[0] and 'var_assign_statment' in ctx.get_type(name)[0]:
                #não declarada mas definida
                raise TypeError(f"variavel {name} ja esta  definida no contexto")
        else:
            #não existe o nome
            if node["expression"] != "empty":
                if verify(ctx, node['expression']) == node['type']:
                    assinatura = ([node['nt']],  node["type"], "argumento")
                    ctx.set_type(name, assinatura)
                else:
                    raise TypeError(f"definiçao de  {name} nao corresponde ao tipo dado")
            else:
                assinatura = ([node['nt']],  node["type"], "argumento")
                ctx.set_type(name, assinatura)
        #return verify(ctx, node['type'])
    
    elif node["nt"] == "var_assign_statment":
        name = node['name']
        if ctx.has_var(name):
            #a variavel ja esta declarada
            if ctx.get_type(name)[1] == "Int":
                pass
            elif ctx.get_type(name)[1] == "Float":
                pass
            elif ctx.get_type(name)[1] == "Bool":
                pass
            elif ctx.get_type(name)[1] == "String":
                pass

            assinatura = ctx.get_type(name)
            #assinatura[0].append(node['nt'])
            if ctx.get_type(name)[1] == assinatura[1]:
                #o tipo e igual
                assinatura = ctx.get_type(name)
                ctx.set_type(name, assinatura)
            elif ctx.get_type(name)[1] != assinatura[1]:
                #o tipo é diferente
                raise TypeError(f"definição da variavel {name} tem tipo diferente da declaraçao")
        else:
            #não declarada nem definida
            raise TypeError(f"variavel {name} nao esta declarada")

        #return verify(ctx, node['type'])

    elif node["nt"] == "statement_expr":
        verify(ctx, node['expression'])
        
    elif node["nt"] == "binop_expression":
        op = node['value']
        el = node['expression_left']
        er = node['expression_right']
        #print(verify(ctx, er))
        #print(verify(ctx, el))
        if op == '+' or op == '-' or op == '*' or op == '/' :
            #print( er)
            #print( el)
            #print(ctx.get_type(er["name"]))
            if verify(ctx, er) == "Int" and verify(ctx, el) == "Int":
                return "Int"
            elif verify(ctx, er) == "Float" and verify(ctx, el) == "Float":
                return "Float"
            elif verify(ctx, er)[1] == "Int" and verify(ctx, el)[1] == "Int":
                return "Int"
            elif verify(ctx, er)[1] == "Float" and verify(ctx, el)[1] == "Float":
                return "Float"
            else:
                raise TypeError(f"As expressoes {op} nao sao inteiros nem float")

        elif op == '%':
            if verify(ctx, er) == "Int" and verify(ctx, el) == "Int":
                return "Int"#######################################################
            if verify(ctx, er)[1] == "Int" and verify(ctx, el)[1] == "Int":
                return "Int"##########################################################
            else:
                raise TypeError(f"As expressoes {op} nao sao inteiros")

        elif op == '>=' or op == '>' or op == '<=' or op == '<':
            
            if verify(ctx, er) == "Int" and verify(ctx, el) == "Int":
                return "Boolean"
            elif verify(ctx, er) == "Float" and verify(ctx, el) == "Float":
                return "Boolean"
            else:
                raise TypeError(f"As expressoes {op} nao sao inteiros nem float")

        elif op == '==' or op == '!=':

            if verify(ctx, er) == "Int" and verify(ctx, el) == "Int":
                return "Boolean"
            elif verify(ctx, er) == "Float" and verify(ctx, el) == "Float":
                return "Boolean"
            elif verify(ctx, er) == "Boolean" and verify(ctx, el) == "Boolean":
                return "Boolean"
            if verify(ctx, er)[1] == "Int" and verify(ctx, el)[1] == "Int":
                return "Boolean"
            elif verify(ctx, er)[1] == "Float" and verify(ctx, el)[1] == "Float":
                return "Boolean"
            elif verify(ctx, er)[1] == "Boolean" and verify(ctx, el)[1] == "Boolean":
                return "Boolean"
            else:
                raise TypeError(f"As expressoes {op} nao sao inteiros nem float nem booleanos")

        elif op == '&&' or op == '||':
            if verify(ctx, el) == "Boolean" and verify(ctx, er) == "Boolean":
                return "Boolean"
            if verify(ctx, el)[1] == "Boolean" and verify(ctx, er[1]) == "Boolean":
                return "Boolean"
            else:
                raise TypeError(f"As expressoes {op} nao sao booleanas")
        
    elif node["nt"] == "bool_expression":
        return "Boolean"

    elif node["nt"] == "nuo_expression":
        return "Boolean"
    
    elif node["nt"] == "int_expression":
        return "Int"

    elif node["nt"] == "float_expression":
        return "Float"

    elif node["nt"] == "string_expression":
        return "String"

    elif node["nt"] == "name_expression":
        name = node["name"]
        if ctx.has_var(name):
            if ctx.get_type(name)[2] == "argumento":
                return ctx.get_type(name)[1]
            else:
                raise TypeError(f"expressao {name}, não é uma variavel")
        else:
            raise TypeError(f"expressao {name}, não existe")
    
    elif node["nt"] == "expression_fun_invoc":
        name = node["name"]
        if ctx.get_type(name)[3] == "function":    
            if len(node["argument"]) == len(ctx.get_type(name)[2][1]):         
                (lista, tipo, argumentos, string) = ctx.get_type(node["name"])
                ass = list((lista, tipo, argumentos, string))
                ass.remove(lista)
                ass.remove(string)
                (expected_return, parameter_types) = tuple(ass)
                if parameter_types != "empty":
                    for (i, (arg, par_t)) in enumerate(zip(node["argument"], parameter_types[1])):
                        arg_t = verify(ctx, arg)
                        if arg_t != par_t:
                            index = i+1
                            raise TypeError(f"Argumento {name} esperava {par_t} mas recebe {arg_t}") 
                    return expected_return
                else:
                    #se funçao nao tem parametros
                    print("ahhhhhhhhhhhhh")
            else:
                raise TypeError(f"Função {name} não tem o numero certo de argumentos")
        else:
            raise TypeError(f"expressao {name}, não é uma funçao")
    
    elif node["nt"] == "array_decl_statment":
        name = node['name']
        if ctx.has_var_in_current_scope(name):
            if 'array_decl_statment' in ctx.get_type(name)[0] and 'array_assign_statment' not in ctx.get_type(name)[0]:
                #declarada mas nao definida
                raise TypeError(f"Array {name} ja esta declarada no contexto")
            elif 'array_decl_statment' in ctx.get_type(name)[0] and 'array_assign_statment' in ctx.get_type(name)[0]:
                #declarada e definida
                raise TypeError(f"Array {name} ja esta declarada e definida no contexto")
            elif 'array_decl_statment' not in ctx.get_type(name)[0] and 'array_assign_statment' in ctx.get_type(name)[0]:
                #não declarada mas definida
                raise TypeError(f"Array {name} ja esta  definida no contexto")
            elif 'var_decl_statment' or 'var_assign_statment' in ctx.get_type(name)[0]:
                raise TypeError(f"Variavel {name} ja esta declarada no contexto")

        else:
            assinatura = ([node['nt']],  node["type"], "array")
            ctx.set_type(name, assinatura)
            
    elif node["nt"] == "array_assign_statment":
        name = node['name']
        if verify(ctx, node["index"]) != "Int":
            raise TypeError(f"Index do array {name} nao é inteiro")
        if ctx.has_var_in_current_scope(name):
            if 'array_decl_statment' in ctx.get_type(name)[0] and 'array_assign_statment' not in ctx.get_type(name)[0]:
                #declarada mas nao definida
                assinatura = ctx.get_type(name)
                if ctx.get_type(name)[1] == assinatura[1]:
                    #o tipo e igual
                    assinatura = ctx.get_type(name)
                    ctx.set_type(name, assinatura)
                elif ctx.get_type(name)[1] != assinatura[1]:
                    #o tipo é diferente
                    raise TypeError(f"definição da variavel {name} tem tipo diferente da declaraçao")
            elif 'array_decl_statment' in ctx.get_type(name)[0] and 'array_assign_statment' in ctx.get_type(name)[0]:
                #declarada e definida
                raise TypeError(f"Array {name} ja esta declarada e definida no contexto")
            elif 'array_decl_statment' not in ctx.get_type(name)[0] and 'array_assign_statment' in ctx.get_type(name)[0]:
                #não declarada mas definida
                raise TypeError(f"Array {name} ja esta  definida no contexto")
            elif 'var_decl_statment' or 'var_assign_statment' in ctx.get_type(name)[0]:
                raise TypeError(f"Variavel {name} ja esta declarada no contexto")
        else:
            raise TypeError(f"Array  {name} nao esta declarado") 
    
    elif node["nt"] == "array_expression":
        expression = node['expression']
        name = node['name']
        if verify(ctx, node['expression']) != ctx.get_type(name):
            raise TypeError(f"expressao do return nao tem o tipo certo")
        return ctx.get_type(name)

    else:
        t = node["nt"]
        print(f"E preciso tratar do node {t}")    

parser = yacc.yacc()

try:
    with open(sys.argv[1]) as inputfile:
        code = inputfile.read()
        print(code)
        verify(Context(), parser.parse(code))
except EOFError:
    print("Unable to read file")