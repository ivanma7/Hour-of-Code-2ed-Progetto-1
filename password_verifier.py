import re

while True:

    password = input("Dammi la password da testare:   ")              
    
    #la password deve essere lunga 8 caratteri
    if len(password) < 8: 
       print("La password deve essere lunga almeno 8 caratteri") 
       continue
  
    #la password deve contenere almeno un carattere maiuscolo
    if not re.search("[A-Z]+",password):
         print("La password deve contenere almeno un carattere maiuscolo")
         continue

     
    # La password deve contenere almeno un carattere minuscolo
    if not re.search("[a-z]+",password):
         print("La password deve contenere almeno un carattere minuscolo")
         continue

    # La password deve contenere almeno un numero
    if not re.search("[0-0]+",password):
        print("La password deve contenere almeno un numero")
        continue
    

    # La password deve contenere almeno un carattere speciale: .,_-
    if not re.search("[\.,_-]+",password):
        print("La password deve contenere almeno un carattere speciale: .,_-")
    
    pass


print("Chiudo il programma.")