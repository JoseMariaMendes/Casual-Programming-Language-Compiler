import ply.yacc as yacc
from collections.abc import Iterable
import ply.lex as lex    
import sys
from context import Context

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

        
        ctx.enter_scope()
        
        if node['block']['block_content'] != "empty":
            verify(ctx, node['block'])
        else:
            raise TypeError(f"funcao {name} está vazia")
        
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
                #assinatura = ([node['nt']],  node["type"], "argumento")
                #ctx.set_type(name, assinatura)
                raise TypeError(f"{name} nao tem valor inicial")
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
            if ctx.get_type(name)[1] == verify(ctx, node["expression"]):
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
                raise TypeError(f"variavel {name} não é do mesmo tipo que a expressão atribuida")
        else:
            #não declarada nem definida
            raise TypeError(f"variavel {name} nao esta declarada")

        #return verify(ctx, node['type'])

    elif node["nt"] == "statement_expr":
        verify(ctx, node['expression'])
        
    elif node["nt"] == "binop_expression":
        op = node['oper']
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
                if isinstance(el%er, int):
                    return "Int"
                if isinstance(el%er, float):
                    return "Float"
            if verify(ctx, er)[1] == "Int" and verify(ctx, el)[1] == "Int":
                if isinstance(el%er, int):
                    return "Int"
                if isinstance(el%er, float):
                    return "Float"
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

    elif node["nt"] == "group_expression":
        return verify(ctx, node["expression"])
    
    else:
        t = node["nt"]
        print(f"E preciso tratar do node {t}")