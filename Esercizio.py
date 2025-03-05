# Abbiamo 25 studenti;  
# memorizzare questo dato in una variabile. Utilizzeremo:  l'operatore di assegnazione =

#Esercizio Abbiamo 25 studenti; memorizzare questo dato in una variabile e stamparla a video.
#  Utilizzeremo:  l'operatore di assegnazione =  la funzione print()
students = 25

print(students)



#Esercizio Abbiamo 25 studenti; memorizzare questo dato in una variabile. Arrivano altri 3 studenti;
#  memorizzare questo dato in un'altra variabile.
students = 25

students_arrivati = 3

students_total = students + students_arrivati

print(students_total) 



#Esercizio Creare una variabile che contiene la stringa "Epicode", quindi stamparla a video.
school = "Epicode"

print(school)   


#Esercizio Verificare, per ognuna delle seguenti stringhe,
#  se il numero di caratteri è compreso tra 5 e 8:
#   str1 = "Windows"  str2 = "Excel"  str3 = "Powerpoint"  str4 = "Word"
str1 = "Windows"
str2 = "Excel"
str3 = "Powerpoint"
str4 = "Word"


print(len(str1)) # è compreso tra 5 e 8
print(len(str2)) # è compreso tra 5 e 8
print(len(str3)) # non è compreso tra 5 e 8
print(len(str4)) # non è compreso tra 5 e 8



#Esercizio Calcolare e stampare a video quanti secondi
#  ci sono in un anno non bisestile.

# Calcolo dei secondi in un anno non bisestile
giorni_anno = 365
ore_giorno = 24
minuti_ora = 60
secondi_minuto = 60

# Calcolo totale secondi
secondi_anno = giorni_anno * ore_giorno * minuti_ora * secondi_minuto

print(secondi_anno)  # Stamperà 31536000



#Esercizio Abbiamo la seguente stringa: my_string = "I am studying Python" 
#  Trasformarla in modo che tutti i caratteri siano maiuscoli (uppercase) 
#  Trasformarla in modo che tutti i caratteri siano minuscoli (lowercase) 
#  Sostituire la sottostringa "Python" con la stringa "a lot" 
#  Usare il metodo .strip(); cambia qualcosa? Perché?
my_string = "I am studying Python"

print(my_string.upper()) # Tutti i caratteri maiuscoli
print(my_string.lower()) # Tutti i caratteri minuscoli
print(my_string.replace("Python", "a lot")) # Sostituzione della sottostringa
print(my_string.strip()) # Rimozione degli spazi iniziali e finali
#Risultati:
#I AM STUDYING PYTHON
#i am studying python
#I am studying a lot
#I am studying Python
        
