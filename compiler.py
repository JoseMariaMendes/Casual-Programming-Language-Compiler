from emmiter import Emitter

def compilador(p, emitter=None):
    if p[0] == "program":
        emitter = Emitter()

        emitter << "define i32 @main() #0 {"
        
        return emitter.get_code()
    