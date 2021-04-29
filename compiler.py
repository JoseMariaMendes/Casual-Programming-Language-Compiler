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

    elif node["nt"] == "ifelse_statement":
        
    """
    elif node["nt"] == "return_statement":
    elif node["nt"] == "while_statement":
    elif node["nt"] == "var_decl_statment":
    elif node["nt"] == "var_assign_statment":
    elif node["nt"] == "array_decl_statment":
    elif node["nt"] == "array_assign_statment":
    elif node["nt"] == "statement_expr":
    elif node["nt"] == "binop_expression":
    elif node["nt"] == "bool_expression":
    elif node["nt"] == "nuo_expression":
    elif node["nt"] == "int_expression":
    elif node["nt"] == "float_expression":
    elif node["nt"] == "string_expression":
    elif node["nt"] == "array_expression":
    elif node["nt"] == "name_expression":
    elif node["nt"] == "group_expression":
    elif node["nt"] == "expression_index_fun":
    elif node["nt"] == "expression_fun_invoc":
        
    """