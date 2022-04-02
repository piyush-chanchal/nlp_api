
import imp


import json
from tkinter.tix import ExFileSelectBox

def validate_in(request):
    in_nlp = json.loads(request.data.decode('utf8').replace("'", '"'))
    
    case_1 = None
    case_2 = None
    case_3 = None
    if len(in_nlp.keys())==1:
        case_1 = True
    if list(in_nlp)[0].upper()=='TEXT':
        case_2 = True
    if type(in_nlp[list(in_nlp)[0]])==str:
        case_3 = True
    
    if case_1==True and case_2==True and case_3==True:
        return True
    else:
        return False