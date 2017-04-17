import ConfigParser

def init():
    get_config()

    global apiUserName
    apiUserName = config.get('GlobalInformation', 'apiUserName')

    global apiPassword
    apiPassword = config.get('GlobalInformation', 'apiPassword')

def get_config():
    global config
    config = ConfigParser.RawConfigParser()
    config.read('api/configuration/config.txt')
