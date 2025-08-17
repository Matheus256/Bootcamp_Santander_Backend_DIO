#Verifique as regras do e-mail:
def verifica_email(email):   
    if(email[0] == "@" or email[-1] == "@"):
      return False
    else:
      for i in range(len(email)):
        if(email[i] == " "):
          return False
        elif(email[i] == "@"):
          if(email[i + 1:len(email)] == "gmail.com" or email[i + 1:len(email)] == "outlook.com"):
            return True
      else: 
        print("E-mail inválido")

# Entrada do usuário
email = input().strip()

if(verifica_email(email)):
    print("E-mail válido")
else:
    print("E-mail inválido")
