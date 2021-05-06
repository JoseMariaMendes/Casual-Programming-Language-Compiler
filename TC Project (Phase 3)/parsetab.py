
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDORnonassocLOWERHIGHERHEQUALLEQUALNEQUALSAMEASDIFFERleftSUMSUBleftMULTIPLYDIVIDERESTOFAND BOOL COLON COMMA DECLARATION DEFINITION DIFFER DIVIDE ELSE EQUALS FALSE FLOAT FLOATTYPE HEQUAL HIGHER IF INT LBRACK LCURLY LEQUAL LOWER LPAR MULTIPLY NAME NEQUAL NUMBER OR QMARK RBRACK RCURLY RESTOF RETURN RPAR SAMEAS SEMICOLON STRING STRINGTYPE SUB SUM TRUE VOID WHILEprogramb : programprogram : DECLARATION declaration\n               | DEFINITION definition\n               | DECLARATION declaration program\n               | DEFINITION definition programdeclaration : NAME LPAR dargument RPAR COLON types\n                    | NAME LPAR dargument RPAR COLON VOID \n                    | NAME LPAR RPAR COLON types \n                    | NAME LPAR RPAR COLON VOID definition : NAME LPAR dargument RPAR COLON types block\n                    | NAME LPAR RPAR COLON types block\n                    | NAME LPAR RPAR COLON VOID block\n                    | NAME LPAR dargument RPAR COLON VOID block types :    INT \n                | FLOATTYPE \n                | BOOL \n                | STRINGTYPEdargument :   NAME COLON types\n                  | NAME COLON types COMMA dargument block : LCURLY RCURLY\n            | LCURLY block_content RCURLYblock_content : statement  \n                    | statement block_content statement : RETURN SEMICOLON \n                | RETURN expression SEMICOLONstatement : IF expression block\n                | IF expression block ELSE block statement : WHILE expression blockstatement : NAME COLON types EQUALS expression SEMICOLON\n                | NAME COLON types SEMICOLONstatement : NAME EQUALS expression SEMICOLONstatement : NAME COLON LBRACK types RBRACK SEMICOLONstatement : NAME LBRACK expression RBRACK EQUALS expression SEMICOLONstatement : expression SEMICOLONexpression : expression SUM expression\n                  | expression SUB expression\n                  | expression MULTIPLY expression\n                  | expression DIVIDE expression\n                  | expression RESTOF expression\n                  | expression SAMEAS expression\n                  | expression NEQUAL expression\n                  | expression HEQUAL expression\n                  | expression LEQUAL expression\n                  | expression HIGHER expression\n                  | expression LOWER expression\n                  | expression AND expression\n                  | expression OR expressionexpression : TRUE \n                | FALSEexpression : DIFFER expressionexpression : NUMBERexpression : FLOATexpression : STRING expression : NAME LBRACK expression RBRACKexpression : NAMEexpression : LPAR expression RPARexpression :  NAME LPAR RPAR LBRACK expression RBRACK\n                    | NAME LPAR argument RPAR LBRACK expression RBRACK expression : NAME LPAR RPAR\n                    | NAME LPAR argument RPARargument :   expression\n                  | expression COMMA argument '
    
_lr_action_items = {'DECLARATION':([0,5,7,24,25,26,27,29,30,35,36,39,41,43,44,45,60,],[3,3,3,-14,-15,-16,-17,-8,-9,-6,-7,-11,-12,-10,-13,-20,-21,]),'DEFINITION':([0,5,7,24,25,26,27,29,30,35,36,39,41,43,44,45,60,],[4,4,4,-14,-15,-16,-17,-8,-9,-6,-7,-11,-12,-10,-13,-20,-21,]),'$end':([1,2,5,7,9,11,24,25,26,27,29,30,35,36,39,41,43,44,45,60,],[0,-1,-2,-3,-4,-5,-14,-15,-16,-17,-8,-9,-6,-7,-11,-12,-10,-13,-20,-21,]),'NAME':([3,4,10,12,34,40,45,47,48,50,51,55,59,60,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,87,88,102,103,114,115,117,119,120,123,126,129,130,131,135,],[6,8,13,13,13,52,-20,52,64,64,64,64,64,-21,-24,-34,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-25,64,-26,-28,64,-30,-31,64,64,-27,64,64,-29,-32,-33,]),'LPAR':([6,8,40,45,47,48,50,51,52,55,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,87,88,102,103,114,115,117,119,120,123,126,129,130,131,135,],[10,12,59,-20,59,59,59,59,84,59,59,-21,-24,84,-34,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-25,59,-26,-28,59,-30,-31,59,59,-27,59,59,-29,-32,-33,]),'RPAR':([10,12,14,16,23,24,25,26,27,42,53,54,56,57,58,64,84,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,108,109,110,111,121,122,128,133,136,],[15,17,19,21,-18,-14,-15,-16,-17,-19,-48,-49,-51,-52,-53,-55,108,-50,111,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-59,-61,121,-56,-60,-54,-62,-57,-58,]),'COLON':([13,15,17,19,21,52,],[18,20,22,28,31,81,]),'INT':([18,20,22,28,31,81,105,],[24,24,24,24,24,24,24,]),'FLOATTYPE':([18,20,22,28,31,81,105,],[25,25,25,25,25,25,25,]),'BOOL':([18,20,22,28,31,81,105,],[26,26,26,26,26,26,26,]),'STRINGTYPE':([18,20,22,28,31,81,105,],[27,27,27,27,27,27,27,]),'VOID':([20,22,28,31,],[30,33,36,38,]),'COMMA':([23,24,25,26,27,53,54,56,57,58,64,85,89,90,91,92,93,94,95,96,97,98,99,100,101,108,109,111,121,122,133,136,],[34,-14,-15,-16,-17,-48,-49,-51,-52,-53,-55,-50,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-59,120,-56,-60,-54,-57,-58,]),'LCURLY':([24,25,26,27,32,33,37,38,53,54,56,57,58,64,79,80,85,89,90,91,92,93,94,95,96,97,98,99,100,101,108,111,113,121,122,133,136,],[-14,-15,-16,-17,40,40,40,40,-48,-49,-51,-52,-53,-55,40,40,-50,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-59,-56,40,-60,-54,-57,-58,]),'EQUALS':([24,25,26,27,52,104,118,],[-14,-15,-16,-17,82,114,126,]),'SEMICOLON':([24,25,26,27,48,49,52,53,54,56,57,58,63,64,85,89,90,91,92,93,94,95,96,97,98,99,100,101,104,106,108,111,118,121,122,124,125,132,133,136,],[-14,-15,-16,-17,62,65,-55,-48,-49,-51,-52,-53,87,-55,-50,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,115,117,-59,-56,-54,-60,-54,130,131,135,-57,-58,]),'RBRACK':([24,25,26,27,53,54,56,57,58,64,85,89,90,91,92,93,94,95,96,97,98,99,100,101,107,108,111,112,116,121,122,127,133,134,136,],[-14,-15,-16,-17,-48,-49,-51,-52,-53,-55,-50,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,118,-59,-56,122,125,-60,-54,133,-57,136,-58,]),'RCURLY':([40,45,46,47,60,61,62,65,87,102,103,115,117,123,130,131,135,],[45,-20,60,-22,-21,-23,-24,-34,-25,-26,-28,-30,-31,-27,-29,-32,-33,]),'RETURN':([40,45,47,60,62,65,87,102,103,115,117,123,130,131,135,],[48,-20,48,-21,-24,-34,-25,-26,-28,-30,-31,-27,-29,-32,-33,]),'IF':([40,45,47,60,62,65,87,102,103,115,117,123,130,131,135,],[50,-20,50,-21,-24,-34,-25,-26,-28,-30,-31,-27,-29,-32,-33,]),'WHILE':([40,45,47,60,62,65,87,102,103,115,117,123,130,131,135,],[51,-20,51,-21,-24,-34,-25,-26,-28,-30,-31,-27,-29,-32,-33,]),'TRUE':([40,45,47,48,50,51,55,59,60,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,87,88,102,103,114,115,117,119,120,123,126,129,130,131,135,],[53,-20,53,53,53,53,53,53,-21,-24,-34,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-25,53,-26,-28,53,-30,-31,53,53,-27,53,53,-29,-32,-33,]),'FALSE':([40,45,47,48,50,51,55,59,60,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,87,88,102,103,114,115,117,119,120,123,126,129,130,131,135,],[54,-20,54,54,54,54,54,54,-21,-24,-34,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-25,54,-26,-28,54,-30,-31,54,54,-27,54,54,-29,-32,-33,]),'DIFFER':([40,45,47,48,50,51,55,59,60,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,87,88,102,103,114,115,117,119,120,123,126,129,130,131,135,],[55,-20,55,55,55,55,55,55,-21,-24,-34,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-25,55,-26,-28,55,-30,-31,55,55,-27,55,55,-29,-32,-33,]),'NUMBER':([40,45,47,48,50,51,55,59,60,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,87,88,102,103,114,115,117,119,120,123,126,129,130,131,135,],[56,-20,56,56,56,56,56,56,-21,-24,-34,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-25,56,-26,-28,56,-30,-31,56,56,-27,56,56,-29,-32,-33,]),'FLOAT':([40,45,47,48,50,51,55,59,60,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,87,88,102,103,114,115,117,119,120,123,126,129,130,131,135,],[57,-20,57,57,57,57,57,57,-21,-24,-34,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-25,57,-26,-28,57,-30,-31,57,57,-27,57,57,-29,-32,-33,]),'STRING':([40,45,47,48,50,51,55,59,60,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,87,88,102,103,114,115,117,119,120,123,126,129,130,131,135,],[58,-20,58,58,58,58,58,58,-21,-24,-34,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-25,58,-26,-28,58,-30,-31,58,58,-27,58,58,-29,-32,-33,]),'ELSE':([45,60,102,],[-20,-21,113,]),'SUM':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[66,-55,-48,-49,-51,-52,-53,66,-55,66,66,66,66,-35,-36,-37,-38,-39,66,66,66,66,66,66,66,66,66,66,-59,66,-56,66,-54,-60,-54,66,66,66,-57,66,-58,]),'SUB':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[67,-55,-48,-49,-51,-52,-53,67,-55,67,67,67,67,-35,-36,-37,-38,-39,67,67,67,67,67,67,67,67,67,67,-59,67,-56,67,-54,-60,-54,67,67,67,-57,67,-58,]),'MULTIPLY':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[68,-55,-48,-49,-51,-52,-53,68,-55,68,68,68,68,68,68,-37,-38,-39,68,68,68,68,68,68,68,68,68,68,-59,68,-56,68,-54,-60,-54,68,68,68,-57,68,-58,]),'DIVIDE':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[69,-55,-48,-49,-51,-52,-53,69,-55,69,69,69,69,69,69,-37,-38,-39,69,69,69,69,69,69,69,69,69,69,-59,69,-56,69,-54,-60,-54,69,69,69,-57,69,-58,]),'RESTOF':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[70,-55,-48,-49,-51,-52,-53,70,-55,70,70,70,70,70,70,-37,-38,-39,70,70,70,70,70,70,70,70,70,70,-59,70,-56,70,-54,-60,-54,70,70,70,-57,70,-58,]),'SAMEAS':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[71,-55,-48,-49,-51,-52,-53,71,-55,71,71,None,71,-35,-36,-37,-38,-39,None,None,None,None,None,None,71,71,71,71,-59,71,-56,71,-54,-60,-54,71,71,71,-57,71,-58,]),'NEQUAL':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[72,-55,-48,-49,-51,-52,-53,72,-55,72,72,None,72,-35,-36,-37,-38,-39,None,None,None,None,None,None,72,72,72,72,-59,72,-56,72,-54,-60,-54,72,72,72,-57,72,-58,]),'HEQUAL':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[73,-55,-48,-49,-51,-52,-53,73,-55,73,73,None,73,-35,-36,-37,-38,-39,None,None,None,None,None,None,73,73,73,73,-59,73,-56,73,-54,-60,-54,73,73,73,-57,73,-58,]),'LEQUAL':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[74,-55,-48,-49,-51,-52,-53,74,-55,74,74,None,74,-35,-36,-37,-38,-39,None,None,None,None,None,None,74,74,74,74,-59,74,-56,74,-54,-60,-54,74,74,74,-57,74,-58,]),'HIGHER':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[75,-55,-48,-49,-51,-52,-53,75,-55,75,75,None,75,-35,-36,-37,-38,-39,None,None,None,None,None,None,75,75,75,75,-59,75,-56,75,-54,-60,-54,75,75,75,-57,75,-58,]),'LOWER':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[76,-55,-48,-49,-51,-52,-53,76,-55,76,76,None,76,-35,-36,-37,-38,-39,None,None,None,None,None,None,76,76,76,76,-59,76,-56,76,-54,-60,-54,76,76,76,-57,76,-58,]),'AND':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[77,-55,-48,-49,-51,-52,-53,77,-55,77,77,-50,77,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,77,77,-59,77,-56,77,-54,-60,-54,77,77,77,-57,77,-58,]),'OR':([49,52,53,54,56,57,58,63,64,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,108,109,111,112,118,121,122,124,127,132,133,134,136,],[78,-55,-48,-49,-51,-52,-53,78,-55,78,78,-50,78,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,78,78,-59,78,-56,78,-54,-60,-54,78,78,78,-57,78,-58,]),'LBRACK':([52,64,81,108,121,],[83,88,105,119,129,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programb':([0,],[1,]),'program':([0,5,7,],[2,9,11,]),'declaration':([3,],[5,]),'definition':([4,],[7,]),'dargument':([10,12,34,],[14,16,42,]),'types':([18,20,22,28,31,81,105,],[23,29,32,35,37,104,116,]),'block':([32,33,37,38,79,80,113,],[39,41,43,44,102,103,123,]),'block_content':([40,47,],[46,61,]),'statement':([40,47,],[47,47,]),'expression':([40,47,48,50,51,55,59,66,67,68,69,70,71,72,73,74,75,76,77,78,82,83,84,88,114,119,120,126,129,],[49,49,63,79,80,85,86,89,90,91,92,93,94,95,96,97,98,99,100,101,106,107,109,112,124,127,109,132,134,]),'argument':([84,120,],[110,128,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programb","S'",1,None,None,None),
  ('programb -> program','programb',1,'p_programb','casual.py',168),
  ('program -> DECLARATION declaration','program',2,'p_program','casual.py',172),
  ('program -> DEFINITION definition','program',2,'p_program','casual.py',173),
  ('program -> DECLARATION declaration program','program',3,'p_program','casual.py',174),
  ('program -> DEFINITION definition program','program',3,'p_program','casual.py',175),
  ('declaration -> NAME LPAR dargument RPAR COLON types','declaration',6,'p_declaration','casual.py',182),
  ('declaration -> NAME LPAR dargument RPAR COLON VOID','declaration',6,'p_declaration','casual.py',183),
  ('declaration -> NAME LPAR RPAR COLON types','declaration',5,'p_declaration','casual.py',184),
  ('declaration -> NAME LPAR RPAR COLON VOID','declaration',5,'p_declaration','casual.py',185),
  ('definition -> NAME LPAR dargument RPAR COLON types block','definition',7,'p_definition','casual.py',193),
  ('definition -> NAME LPAR RPAR COLON types block','definition',6,'p_definition','casual.py',194),
  ('definition -> NAME LPAR RPAR COLON VOID block','definition',6,'p_definition','casual.py',195),
  ('definition -> NAME LPAR dargument RPAR COLON VOID block','definition',7,'p_definition','casual.py',196),
  ('types -> INT','types',1,'p_types','casual.py',203),
  ('types -> FLOATTYPE','types',1,'p_types','casual.py',204),
  ('types -> BOOL','types',1,'p_types','casual.py',205),
  ('types -> STRINGTYPE','types',1,'p_types','casual.py',206),
  ('dargument -> NAME COLON types','dargument',3,'p_d_argument','casual.py',211),
  ('dargument -> NAME COLON types COMMA dargument','dargument',5,'p_d_argument','casual.py',212),
  ('block -> LCURLY RCURLY','block',2,'p_block','casual.py',222),
  ('block -> LCURLY block_content RCURLY','block',3,'p_block','casual.py',223),
  ('block_content -> statement','block_content',1,'p_block_content','casual.py',230),
  ('block_content -> statement block_content','block_content',2,'p_block_content','casual.py',231),
  ('statement -> RETURN SEMICOLON','statement',2,'p_return_statement','casual.py',238),
  ('statement -> RETURN expression SEMICOLON','statement',3,'p_return_statement','casual.py',239),
  ('statement -> IF expression block','statement',3,'p_ifelse_statement','casual.py',246),
  ('statement -> IF expression block ELSE block','statement',5,'p_ifelse_statement','casual.py',247),
  ('statement -> WHILE expression block','statement',3,'p_while_statement','casual.py',254),
  ('statement -> NAME COLON types EQUALS expression SEMICOLON','statement',6,'p_var_decl_statment','casual.py',258),
  ('statement -> NAME COLON types SEMICOLON','statement',4,'p_var_decl_statment','casual.py',259),
  ('statement -> NAME EQUALS expression SEMICOLON','statement',4,'p_var_assign_statment','casual.py',266),
  ('statement -> NAME COLON LBRACK types RBRACK SEMICOLON','statement',6,'p_array_decl_statment','casual.py',270),
  ('statement -> NAME LBRACK expression RBRACK EQUALS expression SEMICOLON','statement',7,'p_array_assign_statment','casual.py',274),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expr','casual.py',280),
  ('expression -> expression SUM expression','expression',3,'p_expression_binop','casual.py',284),
  ('expression -> expression SUB expression','expression',3,'p_expression_binop','casual.py',285),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binop','casual.py',286),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','casual.py',287),
  ('expression -> expression RESTOF expression','expression',3,'p_expression_binop','casual.py',288),
  ('expression -> expression SAMEAS expression','expression',3,'p_expression_binop','casual.py',289),
  ('expression -> expression NEQUAL expression','expression',3,'p_expression_binop','casual.py',290),
  ('expression -> expression HEQUAL expression','expression',3,'p_expression_binop','casual.py',291),
  ('expression -> expression LEQUAL expression','expression',3,'p_expression_binop','casual.py',292),
  ('expression -> expression HIGHER expression','expression',3,'p_expression_binop','casual.py',293),
  ('expression -> expression LOWER expression','expression',3,'p_expression_binop','casual.py',294),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','casual.py',295),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','casual.py',296),
  ('expression -> TRUE','expression',1,'p_expression_bool','casual.py',300),
  ('expression -> FALSE','expression',1,'p_expression_bool','casual.py',301),
  ('expression -> DIFFER expression','expression',2,'p_expression_nuo','casual.py',305),
  ('expression -> NUMBER','expression',1,'p_expression_int','casual.py',309),
  ('expression -> FLOAT','expression',1,'p_expression_float','casual.py',313),
  ('expression -> STRING','expression',1,'p_expression_string','casual.py',317),
  ('expression -> NAME LBRACK expression RBRACK','expression',4,'p_expression_array','casual.py',321),
  ('expression -> NAME','expression',1,'p_expression_name','casual.py',325),
  ('expression -> LPAR expression RPAR','expression',3,'p_expression_group','casual.py',329),
  ('expression -> NAME LPAR RPAR LBRACK expression RBRACK','expression',6,'p_expression_index_fun','casual.py',333),
  ('expression -> NAME LPAR argument RPAR LBRACK expression RBRACK','expression',7,'p_expression_index_fun','casual.py',334),
  ('expression -> NAME LPAR RPAR','expression',3,'p_expression_fun_invoc','casual.py',341),
  ('expression -> NAME LPAR argument RPAR','expression',4,'p_expression_fun_invoc','casual.py',342),
  ('argument -> expression','argument',1,'p_argument','casual.py',349),
  ('argument -> expression COMMA argument','argument',3,'p_argument','casual.py',350),
]
