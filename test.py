#funkonen search_file brukes til å søke etter ordet i filen
def search_file():
    # input spør brukeren om filnavn og ordet den vil søke etter, etter det lagrer det i variablen filenavn og ordet
    filename = input('hvilken fil vill du åpne?')
    ord = input('Hvilke ord vill du finne? ')
    #konverterer søkordet til små bokstaver med .lower()og lagrer det i search_term slik søker blir skiftuavhengig
    search_term = ord.lower()
    
    
                
    #try hjelper deg med å håndtere feil uten at programmet krasjer
    try:
        # med with åpner en fil som heter (den som kommer fra search_file)i lesmodus ("r")med UTF 8 koding
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
             
        linjen = 1
        gangerord = 0

        # søker etter ordet i filen
        for line in lines:
            if search_term in line:
                print("Ordet finnes i teksten")
                display = input("vill du se hvor? (ja/nei)")
                if display == 'ja':
                    print("på linje ", linjen, " står det:")
                    print(line)
                else:
                    print("ok")
                
                gangerord += 1
            linjen += 1
        
        print("Totalt", gangerord, "ganger ble ordet", ord, " funnet.")
                
                

      
         
    # error message hvis det finner ikke ord/filen du letter etter
    except FileNotFoundError:
        print("File not found. Please make sure 'tekstfil.txt' exists in the same directory.")





def restart():
    print("Restarting script...")
    search_file()

def main():
    while True:
        search_file()
        
        choice = input("Vil du gjøre det igjen? (ja/nei): ").lower()
        
        if choice != 'ja':
            break
        
        restart()  # Antatt at innhold er definert noen steder
        
        restart_choice = input("Vil du starte om programmet? (ja/nei): ").lower()
        
        if restart_choice != 'ja':
            break

if __name__ == "__main__":
    main()
