from emitter import Emitter

def get_type (argtype):
    if argtype == "Int":
        return "i32"
    elif argtype == "Float":
        return "float"
    elif argtype == "Void":
        return "void"
    elif argtype == "String":
        return "i8*"
    elif argtype == "Boolean":
        return "zeroext"

def get_align (exptype):
    if exptype == "Int" or exptype == "Float":
        return "align 4"
    elif exptype == "String":
        return "align 8"
    elif exptype == "Boolean":
        return "align 1"


def compilador(node, emitter=None):
    if node["nt"] == "programb":
        print("-------------------")
        emitter = Emitter()
        for decl_def in node["program"]:
            compilador(decl_def, emitter)
        
        return emitter.get_code()

    elif node["nt"] == "definition":
        name = node["name"]
        funtype = get_type(node["type"])
        arguments = ""
        if node["darguments"] != "empty":
            #funçao tem argumentos
            for arg in node["darguments"]:
                if len(arguments) == 0:
                    #primeiro argumentos a ser adicionado
                    arguments += get_type(arg["type"]) + " %" + arg["name"]
                else:
                    #resto dos argumentos depois do primeiro
                    arguments += ", " + get_type(arg["type"]) + " %" + arg["name"]

        emitter << f"define {funtype} @{name}({arguments}) #0 {'{'}"
        #adicionar conteudo do bloco
        if node["darguments"] != "empty":
            for arg in node["darguments"]:
                emitter << f"{emitter.get_pointer_name(arg['name'])} = alloca {get_type(arg['type'])}, {get_align(arg['type'])}"
                emitter << f"store {get_type(arg['type'])} %{arg['name']}, {get_type(arg['type'])}* {emitter.get_pointer_name(arg['name'])}, {get_align(arg['type'])}"

        compilador(node["block"], emitter)
        emitter << "}"

    elif node["nt"] == "block":
        for statment in node['block_content']:
            compilador(statment, emitter)

    elif node["nt"] == "statement_expr":
        compilador(node["expressiom"], emitter)
   
    elif node["nt"] == "var_decl_statment":
        pointer = emitter.get_pointer_name(node['name'])
        vartype = get_type(node['type'])
        tyoealign = get_align(node['type'])

        if node["expression"] != "empty":
            #variavel declarada e defnida
            emitter << f"{pointer} = alloca {vartype}, {tyoealign}"
            compilador(node["expression"], emitter)
            
        else:
            print("something went wrong")

    elif node["nt"] == "var_assign_statment":

        pass
    
    elif node["nt"] == "return_statement":
        pass
    
    elif node["nt"] == "ifelse_statement":
        pass

    elif node["nt"] == "while_statement":
        pass
    
    elif node["nt"] == "array_decl_statment":
        pass

    elif node["nt"] == "array_assign_statment":
        pass

    elif node["nt"] == "binop_expression":
        if node["value"] == "+" or "-" or "*" or "/"
        pass

    elif node["nt"] == "bool_expression":
        pass
       
    elif node["nt"] == "nuo_expression":
        pass

    elif node["nt"] == "int_expression":
        emitter << f""
        pass

    elif node["nt"] == "float_expression":
        print("FLOATR")

    elif node["nt"] == "string_expression":
        pass

    elif node["nt"] == "array_expression":
        pass

    elif node["nt"] == "name_expression":
        return "var"

    elif node["nt"] == "group_expression":
        pass

    elif node["nt"] == "expression_index_fun":
        pass

    elif node["nt"] == "expression_fun_invoc":
        pass