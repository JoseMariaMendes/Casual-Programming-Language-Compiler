class Emitter(object):
    def __init__(self):
        self.count = 0
        self.labelcount = 0
        self.lines = []
        self.linestemp = []
        self.andor = []
        self.stack = [{}]
        self.value = [{}]

    def get_count(self):
        self.count += 1
        return self.count

    def get_id(self):
        id = self.get_count()
        return f"cas_{id}"

    def get_labelcount(self):
        self.labelcount += 1
        return self.labelcount

    def get_labelid(self):
        id = self.get_labelcount()
        return f"{id}"
    
    def __lshift__(self, v):
        self.lines.append(v)

    def get_code(self):
        return "\n".join(self.lines)

    def get_pointer_name(self, n):
        return f"%pont_{n}"
    
    def get_type(self, name):
        for scope in self.stack:
            if name in scope:
                return scope[name]
        raise TypeError(f"Variavel {name} nao esta no contexto")
    
    def set_type(self, name, value):
        scope = self.stack[0]
        scope[name] = value
    
    def get_value(self, name):
        for scope in self.value:
            if name in scope:
                return scope[name]
        raise TypeError(f"Variavel {name} nao esta no contexto")
    
    def set_value(self, name, value):
        scope = self.value[0]
        scope[name] = value