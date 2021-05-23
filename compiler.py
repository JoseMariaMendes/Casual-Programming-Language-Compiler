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
    elif argtype == "[Int]":
        return "i32*"
    elif argtype == "[Float]":
        return "float*"
    elif argtype == "[String]":
        return "i8**"
    elif argtype == "[Boolean]" :
        return "i8*"

def get_align (exptype):
    if exptype == "Int" or exptype == "Float":
        return "align 4"
    elif exptype == "String":
        return "align 8"
    elif exptype == "Boolean":
        return "align 1"
    if exptype == "[Int]" or exptype == "[Float]" or exptype == "[Boolean]" or exptype == "[String]":
        return "align 8"

def float_to_hex(f):
    unpack = struct.unpack('f', struct.pack('f', f))[0]
    return hex(struct.unpack('<Q', struct.pack('<d', unpack))[0])


def compilador(node, emitter=None):
    if node["nt"] == "programb":
        print("-------------------")
        emitter = Emitter()
        emitter.set_type("inlambda", "false")
        emitter.set_type("bprint", "false")
        
        for decl_def in node["program"]:
            compilador(decl_def, emitter)
        
        return emitter.get_code()

    elif node["nt"] == "definition":
        name = node["name"]
        emitter.set_type(name, node["type"])
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
        name = node["name"]
        emitter.set_type(name, node["type"])
        pass

    elif node["nt"] == "array_declaration":
        pass
    
    elif node["nt"] == "array_definition":
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
                
                emitter.set_value(node['name'], value)
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
        
        emitter.set_value(node['name'], value)
        if exptype == "i8":
            #é boolean
            trunc = f"%trunc_{emitter.get_id()}"
            zext = f"%zext_{emitter.get_id()}"
            emitter << f"{trunc} = trunc i8 {value} to i1"
            emitter << f"{zext} = zext i1 {trunc} to i8"
            emitter << f"store {exptype} {zext}, {exptype}* {pointer}, {aligntype}"
            #emitter << f"store {storetype} {zext}, {storetype}* {getelem}, align 1"
            
        else:
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
        #print(node)
        var = node["expression"]
        labelif = f"if_{emitter.get_id()}"
        labelelse = f"else_{emitter.get_id()}"
        labelcont = f"cont_{emitter.get_id()}"
        trunc = f"%trunc_{emitter.get_id()}"
        
        while var["nt"] == "group_expression":
            var = var["expression"]
            
        if var['oper'] == "&&":
            exp = compilador(var["expression_left"], emitter)
            
            if exp[1] != "i1":
                emitter << f"{trunc} = trunc {exp[1]} {exp[0]} to i1"
            else:
                trunc = exp[0]
            
            if var["nt"] == "nuo_expression":
                if exp[3] == False:
                    emitter << f"br i1 {trunc}, label %{labelelse}, label %{labelif}"
                else:
                    emitter << f"br i1 {trunc}, label %{labelif}, label %{labelelse}"
            else:
                emitter << f"br i1 {trunc}, label %{labelif}, label %{labelelse}"
            
            label = compilador(var["expression_right"], emitter)
            emitter << f"br i1 {label}, label %{labelif}, label %{labelelse}"
            
        elif var['oper'] == "||":
            pass
        else:
            exp = compilador(var, emitter)
            
            if exp[1] != "i1":
                emitter << f"{trunc} = trunc {exp[1]} {exp[0]} to i1"
            else:
                trunc = exp[0]
            
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
        
        if exp[1] != "i1":
            emitter << f"{trunc} = trunc {exp[1]} {exp[0]} to i1"
        else:
            trunc = exp[0]
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
        

        oper = node["oper"]
        if emitter.get_type("inlambda") == "true":
            if oper != "+" and "-" and "/" and "*" and "%":
                raise TypeError(f"o lambda so aceita expressões +, -, *, / e %")

        if oper == "+":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            if er[1]  == "i32": 
                emitter << f"{value} = add nsw {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fadd {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
        elif oper == "-":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            if er[1]  == "i32": 
                emitter << f"{value} = sub nsw {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fsub {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
        elif oper == "*":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            if er[1]  == "i32": 
                emitter << f"{value} = mul nsw {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fmul {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
        elif oper == "/":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            if er[1]  == "i32": 
                emitter << f"{value} = sdiv {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fdiv {exptype} {el[0]}, {er[0]}"
                return[value, exptype, aligntype]
        elif oper == "%":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            emitter << f"{value} = srem {exptype} {el[0]}, {er[0]}"
            return[value, exptype, aligntype]
        ########################################################################
        elif oper == "<=":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            if er[1]  == "i32": 
                emitter << f"{value} = icmp sle {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp ole {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
        elif oper == ">":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            if er[1]  == "i32": 
                emitter << f"{value} = icmp sgt {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp ogt {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
        elif oper == "<":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            if er[1]  == "i32": 
                emitter << f"{value} = icmp slt {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp olt {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
        elif oper == ">=":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
            if er[1]  == "i32": 
                emitter << f"{value} = icmp sge {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            elif er[1]  == "float":
                emitter << f"{value} = fcmp oge {exptype} {el[0]}, {er[0]}"
                return[value, "i1", aligntype]
            
        ##############################################################################
        elif oper == "==":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
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
                return[value, "i1", aligntype]
        elif oper == "!=":
            el = compilador(node["expression_left"], emitter)
            er = compilador(node["expression_right"], emitter)
            exptype = er[1]
            aligntype = er[2]
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
                return[value, "i1", aligntype]
                
        elif oper == "&&":
            label = f"&&_{emitter.get_id()}:"
            emitter << ""
            emitter << f"{label}"
            el = compilador(node["expression_left"], emitter)
            emitter << f"br {el[0]}, label "
            
            if node["expression_right"]["nt"] == 'binop_expression' and node["expression_right"]["oper"] == '&&':
                compilador(node["expression_right"], emitter)
            else:
                #ultimo
                label = f"&&_{emitter.get_id()}:"
                print(label)
                emitter << ""
                emitter << f"{label}"
                er = compilador(node["expression_right"], emitter)
                return er
        
        elif oper == "||":
            #print(node["expression_right"])
            #print(node["expression_left"])
            pass

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
        if emitter.get_type("inlambda") == "true":
            pointer = emitter.get_pointer_name(name)
            vartype = get_type(emitter.get_type(name), "var")
            typealign = get_align(emitter.get_type(name))
            emitter << f"{pointer} = alloca {vartype}, {typealign}"
            value = emitter.get_value(name)
            exptype = get_type(emitter.get_type(name), "var")
            aligntype = get_align(emitter.get_type(name))
            emitter << f"store {exptype} {value}, {exptype}* {pointer}, {aligntype}"
                
        gettype = emitter.get_type(name)
        if "[" and "]" and "x" not in gettype:
            exptype = get_type(emitter.get_type(name), "var") 
            aligntype = get_align(emitter.get_type(name))
            loadpointer = f"%load_{emitter.get_id()}_{name}"
            emitter << f"{loadpointer} = load {exptype}, {exptype}* {emitter.get_pointer_name(name)}, {aligntype}"
            
            return [loadpointer, exptype, aligntype]
        else:
            exptype = gettype 
            aligntype = get_align(emitter.get_type(name))
            loadpointer = f"%load_{emitter.get_id()}_{name}"
            emitter << f"{loadpointer} = getelementptr inbounds {exptype}, {exptype}* {emitter.get_pointer_name(name)}, i64 0, i64 0"
            if "i32" in exptype:
                exptype = "i32*"
            elif "float" in exptype:
                exptype = "float*"
            elif "i8*" in exptype:
                exptype = "i8**"
            else:
                exptype = "i8*"
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
    
    elif node["nt"] == "array_decl_statment":
        
        size = node["size"]
        pointer = emitter.get_pointer_name(node['name'])
        t = node['type']
        
        for char in "[]":
            t = t.replace(char, "")
            
        vartype = get_type(t, "var")
        if size < 4:
            typealign = "align 4"
        else:
            typealign = "align 16"
        a_type = f"[{size} x {vartype}]"    
        emitter << f"{pointer} = alloca {a_type}, {typealign}"        
        emitter.set_type(node['name'], a_type)
        currentvar = [node['type'], pointer]

    elif node["nt"] == "array_assign_statment":
        indexvar = compilador(node["index"], emitter)
        index = indexvar[0]
        indextype = indexvar[1]
        pointer = emitter.get_pointer_name(node['name'])
        
        exptype = emitter.get_type(node['name'])
        
        size = ""
        
        for char in exptype:
            if char == "x":
                break
            if char != "[":
                size += char 
    
        size = int(size)
        if isinstance(index, int):
            if index > size:
                raise TypeError(f"index de {node['name']} não suportado")
        else:
            sext = f"%sext_{emitter.get_id()}"
            emitter << f"{sext} = sext {indextype} {index} to i64"
            index = sext
        
        var = compilador(node["expression"], emitter)
        getelem = f"%getelem_{emitter.get_id()}"
        value = var[0]
        storetype = var[1]
        aligntype = var[2]
        
        if storetype == "i8":
            #é boolean
            loadpointer = f"%load_{emitter.get_id()}"
            trunc = f"%trunc_{emitter.get_id()}"
            zext = f"%zext_{emitter.get_id()}"
            #%4 = alloca [10 x i8], align 1
            #%5 = alloca i8, align 1
            #%6 = load i8, i8* %5, align 1, !dbg !23
            trunc = f"%trunc_{emitter.get_id()}"
            zext = f"%zext_{emitter.get_id()}"
            emitter << f"{trunc} = trunc i8 {value} to i1"
            emitter << f"{getelem} = getelementptr inbounds {exptype}, {exptype}* {pointer}, i64 0, i64 {index}"
            emitter << f"{zext} = zext i1 {trunc} to i8"
            emitter << f"store i8 {zext}, i8* {getelem}, {aligntype}"
            
        else:
            emitter << f"{getelem} = getelementptr inbounds {exptype}, {exptype}* {pointer}, i64 0, i64 {index}"
            emitter << f"store {storetype} {value}, {storetype}* {getelem}, align 8"

    elif node["nt"] == "array_expression":
        
        name = node["name"]
        indexvar = compilador(node["index"], emitter)
        aligntype = "align 1"
        loadpointer = f"%load_{emitter.get_id()}_{name}"
        getelem = f"%getelem_{emitter.get_id()}_{name}"
        index = indexvar[0]
        indextype = indexvar[1]
        pointer = emitter.get_pointer_name(node['name'])
        a_type = emitter.get_type(name)
        size =  ""
        
        if "x" in a_type:
            for char in a_type:
                if char == "x":
                    break
                if char != "[":
                    size += char 
            size = int(size)
            if isinstance(index, int):
                if index > size:
                    raise TypeError(f"index de {node['name']} não suportado")
            else:
                sext = f"%sext_{emitter.get_id()}"
                emitter << f"{sext} = sext {indextype} {index} to i64"
                index = sext
    
            pointer = emitter.get_pointer_name(name)
            type = emitter.get_type(name) 
            
            if "i32" in type:
                exptype = "i32"
            elif "float" in type:
                exptype = "float"
            else:
                exptype = "i8"
        
            emitter << f"{getelem} = getelementptr inbounds {a_type}, {a_type}* {pointer}, i64 0, i64 {index}"
            emitter << f"{loadpointer} = load {exptype}, {exptype}* {getelem}, {aligntype}"
        else:
            loadarr = get_type(a_type, "var")
            for char in "[]":
                a_type = a_type.replace(char, "")
            exptype = get_type(a_type, "var")
            load = f"%load_{emitter.get_id()}"
            emitter << f"{load} = load {loadarr}, {loadarr}* {pointer}, align 8"
            emitter << f"{getelem} = getelementptr inbounds {exptype}, {exptype}* {load}, i64 {index}"
            emitter << f"{loadpointer} = load {exptype}, {exptype}* {getelem}, {aligntype}"
            pass
        return [loadpointer, exptype, aligntype]
        
    elif node["nt"] == "expression_index_fun":
        pass

    elif node["nt"] == "expression_fun_invoc":
        name = node["name"]
        type = emitter.get_type(name)
        aligntype = get_align(type)
        args = node["argument"]
        call = f"%call_{emitter.get_id()}_{name}"
        arguments = ""
        if args != "empty":
            for arg in args:
                argid = compilador(arg, emitter)
                
                argvalue = argid[0]
                argtype = argid[1]
                #print(arguments)
                if len(arguments) == 0:
                    #primeiro argumentos a ser adicionado
                    arguments += f"{argtype} {argvalue}"
                else:
                    #resto dos argumentos depois do primeiro
                    arguments += f", {argtype} {argvalue}"
                
            if type != "Void":
                type = get_type(type, "var")
                emitter << f"{call} = call {type} @{name}({arguments})"
                    #%3 = call i32 @fun(i32 3)
                    
            else:
                #call void @fun(i32 3)
                type = get_type(type)
                emitter << f"call void @{name}({arguments})"
                pass
        else:
            if type != "Void":
                type = get_type(type, "var")
                emitter << f"{call} = call {type} @{name}()"
                
            else:
                type = get_type(type)
                emitter << f"call void @{name}()"
        return [call, type, aligntype]
       
    elif node["nt"] == "print":
        if emitter.get_type("bprint") == "false":
            emitter.lines.insert(0, f"declare i32 @printf(i8*, ...)")
            emitter.set_type("bprint", "true")
        vartype = "i8*"
        align = get_align('String')
        value = node["string"]
        size = len(value)-1
        nn = value.count("\\n")
        arguments = ""
        size -= nn
        value = value.replace('"', '')
        value = value.replace("\\n", "\\0A")
        value = f'"{value}\\00"'
        id = emitter.get_id()
        str_name = f"@.casual_str_{id}"
        str_decl = f"""{str_name} = private unnamed_addr constant [{size} x i8] c{value}, align 1"""
        emitter.lines.insert(0, str_decl)
        value = f"getelementptr inbounds ([{size} x i8], [{size} x i8]* {str_name}, i64 0, i64 0)"
        
        
        if node["arguments"] != "empty":
            for arg in node["arguments"]:
                var = compilador(arg, emitter)
                arguments += f", {var[1]} {var[0]}"
            emitter << f"%print_{emitter.get_id()}= call i32 ({vartype}, ...) @printf({vartype} {value}{arguments})"
            pass
        else:
            emitter << f"%print_{emitter.get_id()} = call i32 ({vartype}, ...) @printf (i8* {value})"
            pass 
        
    elif node["nt"] == "lambda_expression":
        emitter.set_type("inlambda", "true")
        emitter.linestemp = emitter.lines
        returntype = get_type(node['rtype'], "var")
        funtype = get_type(node['rtype'], "fun")
        name = node["name"]
        emitter.set_type(name, node['rtype'])
        arguments = ""
        cont = 0
        currentfun = ""
        for arg in node["darguments"]:
            if len(arguments) == 0:
                #primeiro argumentos a ser adicionado
                
                arguments += get_type(arg["type"], "funarg") + " %" + arg["name"]
            else:
                #resto dos argumentos depois do primeiro
                arguments += ", " + get_type(arg["type"], "funarg") + " %" + arg["name"]
        
        for line in emitter.lines:
            if "define" in line:
                currentfunindex = cont
            cont += 1
            
            
        emitter.lines = []
        emitter << f"define {funtype} @{name}({arguments}) #0 {'{'}"
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

        for exp in node["block_lam"]['block_content_lam']:
            print(exp)
            som = compilador(exp, emitter)
            print(som)
        
        retexp = som[0]
        emitter << f"ret {returntype} {retexp}"
        emitter << "}"
        
        for line in emitter.lines:
            emitter.linestemp.insert(currentfunindex, line)
            currentfunindex += 1
        emitter.lines = emitter.linestemp
        
        emitter.set_type("inlambda", "false")
        
    elif node["nt"] == "block_lam":
        for exp in node['block_content_lam']:
            compilador(exp, emitter)
        
    else:
        t = node["nt"]
        print(f"E preciso tratar do node {t}")