import api.configuration.globalVars as globalVars

def auth(uname, passwd):
    globalVars.init()
    if uname == globalVars.apiUserName:
        if passwd == globalVars.apiPassword:
            return True
    return False
