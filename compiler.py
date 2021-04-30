from emitter import Emitter
import struct


def get_type (argtype, stattype):
    if argtype == "Int":
        return "i32"
    elif argtype == "Float":
        return "float"
    elif argtype == "Void":
        return "void"
    elif argtype == "String":
        return "i8*"
    elif argtype == "Boolean" and stattype == "funarg":
        return "i1 zeroext"
    elif argtype == "Boolean" and stattype == "fun":
        return "zeroext i1"
    elif argtype == "Boolean" and stattype == "var":
        return "i8"
    elif argtype == "Boolean" and stattype == "ret":
        return "i1"

def get_align (exptype):
    if exptype == "Int" or exptype == "Float":
        return "align 4"
    elif exptype == "String":
        return "align 8"
    elif exptype == "Boolean":
        return "align 1"

def float_to_hex(f):
    unpack = struct.unpack('f', struct.pack('f', f))[0]
    return hex(struct.unpack('<Q', struct.pack('<d', unpack))[0])

def compilador(node, emitter=None):
    global currentvar
    if node["nt"] == "programb":
        print("-------------------")
        emitter = Emitter()
        for decl_def in node["program"]:
            compilador(decl_def, emitter)
        
        return emitter.get_code()

    elif node["nt"] == "definition":
        name = node["name"]
        funtype = get_type(node["type"], "fun")
        arguments = ""
        if node["darguments"] != "empty":
            #funçao tem argumentos
            for arg in node["darguments"]:
                if len(arguments) == 0:
                    #primeiro argumentos a ser adicionado
                    arguments += get_type(arg["type"], "funarg") + " %" + arg["name"]
                else:
                    #resto dos argumentos depois do primeiro
                    arguments += ", " + get_type(arg["type"], "funarg") + " %" + arg["name"]

        emitter << f"define {funtype} @{name}({arguments}) #0 {'{'}"
        #adicionar conteudo do bloco
        if node["darguments"] != "empty":
            for arg in node["darguments"]:
                emitter << f"{emitter.get_pointer_name(arg['name'])} = alloca {get_type(arg['type'], 'var')}, {get_align(arg['type'])}"
                emitter << f"store {get_type(arg['type'], 'var')} %{arg['name']}, {get_type(arg['type'], 'var')}* {emitter.get_pointer_name(arg['name'])}, {get_align(arg['type'])}"

        compilador(node["block"], emitter)
        emitter << "}"

    elif node["nt"] == "block":
        for statment in node['block_content']:
            compilador(statment, emitter)

    elif node["nt"] == "statement_expr":
        compilador(node["expressiom"], emitter)
   
    elif node["nt"] == "var_decl_statment":
        pointer = emitter.get_pointer_name(node['name'])
        vartype = get_type(node['type'], "var")
        typealign = get_align(node['type'])

        if node["expression"] != "empty":
            #variavel declarada e defnida
            emitter << f"{pointer} = alloca {vartype}, {typealign}"
            currentvar = [node['type'], pointer]
            compilador(node["expression"], emitter)
            currentvar = []
        else:
            print("something went wrong")

    elif node["nt"] == "var_assign_statment":
        pointer = emitter.get_pointer_name(node['name'])
        currentvar = ["unknown", pointer]
        compilador(node["expression"], emitter)
    
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
        er = node["expression_right"]
        el = node["expression_left"]
        value = node["value"]
        if node["value"] == "+":
            result = compilador
        #elif value == "-":
        #elif value == "*":
        #elif value == "/":
        #elif value == "%":
        #elif value == "==":
        #elif value == "!=":
        #elif value == ">=":
        #elif value == "<=":
        #elif value == ">":
        #elif value == "<":
        #elif value == "&&":
        #elif value == "||":

    elif node["nt"] == "bool_expression":
        #store i8 1, i8* %11, align 1
        value = node["bool"]
        if value == "True":
            value = 1
        else:
            value = 0
        exptype = "i8"
        
        emitter << f"store {exptype} {value}, {exptype}* {currentvar[1]}, {get_align('Boolean')}"
        return exptype
       
    elif node["nt"] == "nuo_expression":
        pass

    elif node["nt"] == "int_expression":
        #store i32 0, i32* %9, align 4
        value = node["number"]
        exptype = "i32"
        emitter << f"store {exptype} {value}, {exptype}* {currentvar[1]}, {get_align('Int')}"
        return exptype
        
    elif node["nt"] == "float_expression":
        value = float_to_hex(node["float"])
        exptype = "float"
        emitter << f"store {exptype} {value}, {exptype}* {currentvar[1]}, {get_align('Float')}"
        return exptype

    elif node["nt"] == "string_expression":
        pointer = currentvar[1]
        vartype = "i8*"
        align = get_align('String')
        value = node["string"]
        size = len(value)-1
        nn = value.count("\\n")
        size -= nn
        value = value.replace('"', '')
        value = value.replace("\\n", "\\0A")
        value = f'"{value}\\00"'
        id = emitter.get_id()
        str_name = f"@.casual_str_{id}"
        str_decl = f"""{str_name} = private unnamed_addr constant [{size} x i8] c{value}, align 1"""
        emitter.lines.insert(0, str_decl)
        emitter << f"store {vartype} getelementptr inbounds ([{size} x i8], [{size} x i8]* @.str, i64 0, i64 0), {vartype}* {pointer}, {align}"
        return vartype

    elif node["nt"] == "array_expression":
        print(currentvar)
        pass

    elif node["nt"] == "name_expression":
        name = node["name"]
        exptype = currentvar

        print(currentvar)
        emitter << f"%{emitter.get_id()} = load {exptype}, {exptype}* {emitter.get_pointer_name(name)}, {get_align(exptype)}"
        return "var"

    elif node["nt"] == "group_expression":
        pass

    elif node["nt"] == "expression_index_fun":
        print(currentvar)
        pass

    elif node["nt"] == "expression_fun_invoc":
        print(currentvar)
        pass