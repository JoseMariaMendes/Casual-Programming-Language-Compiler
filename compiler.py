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
    
    if node["nt"] == "programb":
        print("-------------------")
        emitter = Emitter()
        for decl_def in node["program"]:
            compilador(decl_def, emitter)
        
        return emitter.get_code()

    elif node["nt"] == "definition":
        name = node["name"]
        funtype = get_type(node["type"], "fun")
        emitter.set_type("RETURN_TYPE", node["type"])
        aligntype = get_align(node["type"])
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
                emitter.set_type(arg["name"], arg["type"])
                if arg["type"] == "Boolean":
                    pont = f"%{emitter.get_id()}"
                    name = emitter.get_pointer_name(arg['name'])
                    emitter << f"{name} = alloca i8, align 1"
                    emitter << f"{pont} = zext i1 %{arg['name']} to i8"
                    emitter << f"store i8 {pont}, i8* {name}, align 1"
                else:
                    emitter << f"{emitter.get_pointer_name(arg['name'])} = alloca {get_type(arg['type'], 'var')}, {get_align(arg['type'])}"
                    emitter << f"store {get_type(arg['type'], 'var')} %{arg['name']}, {get_type(arg['type'], 'var')}* {emitter.get_pointer_name(arg['name'])}, {get_align(arg['type'])}"

        compilador(node["block"], emitter)
        
        emitter << "}"

    elif node["nt"] == "declaration":
        pass

    elif node["nt"] == "block":
        for statment in node['block_content']:
            compilador(statment, emitter)

    elif node["nt"] == "statement_expr":
        compilador(node["expression"], emitter)
   
    elif node["nt"] == "var_decl_statment":
        pointer = emitter.get_pointer_name(node['name'])
        vartype = get_type(node['type'], "var")
        typealign = get_align(node['type'])

        if node["expression"] != "empty":
            #variavel declarada e defnida
            
            emitter << f"{pointer} = alloca {vartype}, {typealign}"
            emitter.set_type(node['name'], node['type'])
            currentvar = [node['type'], pointer]
            var = compilador(node["expression"], emitter)
            if var != None:
                value = var[0]
                exptype = var[1]
                aligntype = var[2]
                emitter << f"store {exptype} {value}, {exptype}* {pointer}, {aligntype}"
            else:
                pass
        else:
            print("something went wrong")

    elif node["nt"] == "var_assign_statment":
        #print(node['name'])
        pointer = emitter.get_pointer_name(node['name'])
        exptype = emitter.get_type(node['name'])
        currentvar = [exptype, pointer]
        var = compilador(node["expression"], emitter)
        value = var[0]
        exptype = var[1]
        aligntype = var[2]
        emitter << f"store {exptype} {value}, {exptype}* {pointer}, {aligntype}"
        
    elif node["nt"] == "return_statement":
        exp = compilador(node["expression"], emitter)
        value = exp[0]
        exptype = exp[1]
        aligntype = exp[2]
        if emitter.get_type("RETURN_TYPE") == "Boolean":
            truncname = f"%{emitter.get_id()}"
            emitter << f"{truncname} = trunc {exptype} {value} to i1"
            value = truncname
            emitter << f"ret i1 {value}"
        else:
            emitter << f"ret {exptype} {value}"
        
        
        pass
    
    elif node["nt"] == "ifelse_statement":
        var = node["expression"]
        while var["nt"] == "group_expression":
            var = var["expression"]
        
        exp = compilador(var, emitter)
        labelif = f"if_{emitter.get_id()}"
        labelelse = f"else_{emitter.get_id()}"
        labelcont = f"cont_{emitter.get_id()}"
        trunc = f"%trunc_{emitter.get_id()}"
        emitter << f"{trunc} = trunc {exp[1]} {exp[0]} to i1"
        
        if var["nt"] == "nuo_expression":
            if exp[3] == False:
                emitter << f"br i1 {trunc}, label %{labelelse}, label %{labelif}"
            else:
                emitter << f"br i1 {trunc}, label %{labelif}, label %{labelelse}"
        else:
            emitter << f"br i1 {trunc}, label %{labelif}, label %{labelelse}"
        
        
        if len(node["block"]) == 2:
            emitter <<""
            emitter << f"{labelif}:"
            compilador(node["block"][0], emitter)
            emitter << f"br label %{labelcont}"
            emitter << ""
            emitter << f"{labelelse}:"
            compilador(node["block"][1], emitter)
            emitter << f"br label %{labelcont}"
            emitter << ""
            emitter << f"{labelcont}:"
        else:
            emitter <<""
            emitter << f"{labelif}:"
            compilador(node["block"][0], emitter)
            emitter << f"br label %{labelelse}"
            emitter << ""
            emitter << f"{labelelse}:"

    elif node["nt"] == "while_statement":
        var = node["expression"]
        while var["nt"] == "group_expression":
            var = var["expression"]
        
        xor = f"%xor_{emitter.get_id()}"
        labelwhile = f"while_{emitter.get_id()}"
        labelblock = f"block_{emitter.get_id()}"
        labelcont = f"cont_{emitter.get_id()}"
        trunc = f"%trunc_{emitter.get_id()}"
        exp = compilador(var, emitter)
        
        
        
        emitter << f"br label %{labelwhile}"
        emitter << ""
        emitter << f"{labelwhile}:"
        
        emitter << f"{trunc} = trunc {exp[1]} {exp[0]} to i1"
        if var["nt"] == "nuo_expression":
            if exp[3] == False:
                #trocar
                #%4 = trunc i8 %3 to i1
                # %5 = xor i1 %4, true
                emitter << f"{xor} = xor i1 {trunc}, true"
                emitter << f"br i1 {xor}, label %{labelblock}, label %{labelcont}"
            else:
                emitter << f"br i1 {trunc}, label %{labelblock}, label %{labelcont}"
        else:
            emitter << f"br i1 {trunc}, label %{labelblock}, label %{labelcont}"
            
        emitter << ""
        emitter << f"{labelblock}:"
        compilador(node["block"], emitter)
        emitter << f"br label %{labelwhile}"
        emitter << ""
        emitter << f"{labelcont}:"
        
    elif node["nt"] == "binop_expression":
        #print("binop")
        value = f"%{emitter.get_id()}_binopexp"
        ernt = node["expression_right"]["nt"]
        elnt = node["expression_left"]["nt"]
        er = compilador(node["expression_right"], emitter)
        el = compilador(node["expression_left"], emitter)
        exptype = er[1]
        aligntype = er[2]
        oper = node["oper"]

        if oper == "+":
            if er[1]  == "i32": 
                emitter << f"{value} = add nsw {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fadd {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
        elif oper == "-":
            if er[1]  == "i32": 
                emitter << f"{value} = sub nsw {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fsub {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
        elif oper == "*":
            if er[1]  == "i32": 
                emitter << f"{value} = mul nsw {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fmul {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
        elif oper == "/":
            if er[1]  == "i32": 
                emitter << f"{value} = sdiv {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fdiv {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
        elif oper == "%":
            emitter << f"{value} = srem {exptype} {el[0]}, {er[0]}"
            return[value, exptype, aligntype]
        ########################################################################
        elif oper == "<=":
            if er[1]  == "i32": 
                emitter << f"{value} = icmp sle {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp ole {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
        elif oper == ">":
            if er[1]  == "i32": 
                emitter << f"{value} = icmp sgt {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp ogt {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
        elif oper == "<":
            if er[1]  == "i32": 
                emitter << f"{value} = icmp slt {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp olt {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
        elif oper == ">=":
            if er[1]  == "i32": 
                emitter << f"{value} = icmp sge {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp oge {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            
        ##############################################################################
        elif oper == "==":
            if er[1]  == "i32": 
                emitter << f"{value} = icmp eq {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp oeq {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1] == "i8":
                if not isinstance(er[0], int):
                    tran = er[0]
                    other = er[0]
                elif not isinstance(el[0], int):
                    tran = el[0]
                    other = er[0]
                
                temp1 = f"%trunc_{emitter.get_id()}"
                temp2 = f"%zext_{emitter.get_id()}"
                
                emitter << f"{temp1} = trunc {exptype} {tran} to i1"
                emitter << f"{temp2} = zext i1 {temp1} to i32"
                emitter << f"{value} = icmp eq i32 {temp2}, {other}"
        elif oper == "!=":
            if er[1]  == "i32": 
                emitter << f"{value} = icmp ne {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp une {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1] == "i8":
                if not isinstance(er[0], int):
                    tran = er[0]
                    other = er[0]
                elif not isinstance(el[0], int):
                    tran = el[0]
                    other = er[0]
                
                temp1 = f"%trunc_{emitter.get_id()}"
                temp2 = f"%zext_{emitter.get_id()}"
                
                emitter << f"{temp1} = trunc {exptype} {tran} to i1"
                emitter << f"{temp2} = zext i1 {temp1} to i32"
                emitter << f"{value} = icmp ne i32 {temp2}, {other}"
                
        #elif oper == "&&":
        #elif oper == "||":

    elif node["nt"] == "nuo_expression":
        nnuo = 1
        exptype = "i8"
        aligntype = get_align('Boolean')
        exp = node["expression"]
        while exp["nt"] == "nuo_expression":
            exp = exp["expression"]
            nnuo += 1
        var = compilador(exp, emitter)
        
        if nnuo % 2 == 0:
            #par
            value = True
        else:
            value = False
            
        return [var[0], var[1], var[2], value]

    elif node["nt"] == "bool_expression":
        #store i8 1, i8* %11, align 1
        
        value = node["value"]
        if value == "True":
            value = 1
        else:
            value = 0
        exptype = "i8"
        aligntype = get_align('Boolean')
        return [value, exptype, aligntype]

    elif node["nt"] == "int_expression":
        #store i32 0, i32* %9, align 4
        value = node["value"]
        exptype = "i32"
        aligntype = get_align('Int')
        return [value, exptype, aligntype]
        
    elif node["nt"] == "float_expression":
        value = float_to_hex(node["value"])
        exptype = "float"
        aligntype = get_align('Float')
        return [value, exptype, aligntype]

    elif node["nt"] == "name_expression":
        name = node["name"]
        exptype = get_type(emitter.get_type(name), "var") 
        aligntype = get_align(emitter.get_type(name))
        loadpointer = f"%load_{emitter.get_id()}_{name}"
        emitter << f"{loadpointer} = load {exptype}, {exptype}* {emitter.get_pointer_name(name)}, {aligntype}"
        return [loadpointer, exptype, aligntype]
    
    elif node["nt"] == "string_expression":
        vartype = "i8*"
        align = get_align('String')
        value = node["value"]
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
        value = f"getelementptr inbounds ([{size} x i8], [{size} x i8]* {str_name}, i64 0, i64 0)"
        return [value, vartype, align]

    elif node["nt"] == "group_expression":
        return compilador(node["expression"], emitter)
    
    elif node["nt"] == "array_expression":
        pass

    elif node["nt"] == "array_decl_statment":
        pass

    elif node["nt"] == "array_assign_statment":
        pass

    elif node["nt"] == "expression_index_fun":
        pass

    elif node["nt"] == "expression_fun_invoc":
        pass
    
    else:
        t = node["nt"]
        print(f"E preciso tratar do node {t}")