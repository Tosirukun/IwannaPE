class IndentError(Exception):
    print('コードの書き方がおかしいです')
    pass
    
class VariableError(Exception):
    print('渡す値が異常です')
    pass

def get(clss, valiable):
    if valiable == "SURFACE" or valiable == "surface":
        return clss.SURFACE
    
def valiable_get(clss, valiable_name):
    eval('return {0}.{1}'.format(str(clss), str(valiable_name)))
