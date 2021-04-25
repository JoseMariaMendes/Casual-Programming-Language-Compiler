import ply.yacc as yacc
from collections.abc import Iterable
import ply.lex as lex    
import sys
from context import Context
from verify import verify
from parser import *
 
parser = yacc.yacc()

try:
    with open(sys.argv[1]) as inputfile:
        code = inputfile.read()
        print(code)
        verify(Context(), parser.parse(code))
except EOFError:
    print("Unable to read file")