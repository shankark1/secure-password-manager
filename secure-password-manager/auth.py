import getpass
MASTER = "admin123"

def authenticate():
    password = getpass.getpass("Master Password: ")
    return password == MASTER
