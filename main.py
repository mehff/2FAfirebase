import pyrebase
import time
import random
import mailing

firebaseConfig = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "databaseURL": "https://" + "" + ".firebaseio.com",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

tempinfo = {}

def signup():
    print("Registrar uma Conta")
    email = input("Digite um e-mail: ")
    pwd = input("Digite uma senha: ")
    try:
        user = auth.create_user_with_email_and_password(email,pwd)
        print("Conta criada com sucesso!")
        print("Enviando e-mail de verificação")
        tokenid = user["idToken"]
        auth.send_email_verification(tokenid)
        print("Você tem 15 segundos para verificar sua conta.")
        time.sleep(15)
        isverified1 = (auth.get_account_info(user["idToken"]))
        isverified2 = isverified1["users"]
        isverified3 = isverified2[0]["emailVerified"]
        print('sou isverified3:', isverified3)
        if isverified3 == True:
            valnum = random.randrange(1111,9999)
            tomail = email
            mailing.sendvalmail(valnum, tomail)
            inputnum = int(input(print('Agora enviaremos um número de quatro dígitos para seu e-mail. Insira-o aqui quando recebê-lo:')))
            if inputnum == valnum:
                tologin = int(input("Deseja realizar login agora?\n1 para Sim\n2 para Não"))
                if tologin == 1:
                    login()
                elif tologin == 2:
                    print('Adios!')
                    exit()
            else:
                auth.delete_user_account(user["idToken"])
                print('Número incorreto. Cadastre-se novamente.')
        if isverified3 == False:
            auth.delete_user_account(user["idToken"])
            print('A conta não foi verificada. Cadastre-se novamente.')
            signup()
    except:
        print("E-mail já registrado. Tente novamente.")
        signup()

def login():
    print("Logar em uma Conta")
    email = input("Digite seu e-mail: ")
    pwd = input("Digite sua senha: ")
    try:
        gologin = auth.sign_in_with_email_and_password(email, pwd)
        print("Logado com sucesso!")
        print("Informações: ", auth.get_account_info(gologin['idToken']))
    except:
        print("E-mail ou senha inválidos. Tente novamente.")
        login()

options = int(input("Você é um usuário novo?\n1 para Sim\n2 para Não"))
if options == 1:
    signup()
elif options == 2:
    login()