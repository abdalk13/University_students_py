import csv

def läs_data_från_fil(filnamn):
    """
    Funktionen läser in data från en CSV-fil och returnerar den som en lista av rader.

    """

    try:
        with open(filnamn, mode='r',encoding='utf-8') as fil: #funktionen öppnar filen och delar den i fält och varje fält slutar med semikolon
            läsare = csv.reader(fil, delimiter=';') 
            data = [rad for rad in läsare] 
        return data
    except FileNotFoundError as e:
        print(f"File not found: {filnamn}")
        print(f"Exception: {e}")
        return []
    
def skriv_data_till_fil(filnamn, data):
        """
        Funktionen skriver data till en CSV-fil och öppnar filen för att skriva i den

        """
        
        with open(filnamn,encoding='utf-8' ,mode='w', newline='\n') as fil:
            skrivare = csv.writer(fil, delimiter=';')#varje fält som skrivs, måste avslutas med semikolumn.
            skrivare.writerows(data)    

def hitta_namn(data, namn):
    """
    Funktionen söker efter personer och returnerar de matchande personerna som har samma för och efternamn
    
    """
    matchande_personer = []

    for person in data:
        if len(person) >= 2 and namn.lower() in f"{person[0]} {person[1]}".lower():
            matchande_personer.append(person)

    return matchande_personer


def valid_email(email):
    """
    kolla om epost innehåller '@' och '.'.

    """
    if '@' in email and '.' in email:
        return True
    else:
        return False     

def hitta_epost(data, epost):
        """
        Funktionen söker efter personer med matchande epost och returnerar pesoner med samma epost

        """
        matchande_personer = [person for person in data if len(person) > 3 and epost.lower() == person[3].lower()]#vi söker i email och vi ska se till att ta bort mellanrum för att match sökning 
        return matchande_personer
    
def hitta_telefon(data, telefon):
    """
    Funktionen söker efter personer med matchande telefonnummer 


    """
    matchande_personer = [person for person in data if len(person) > 2 and telefon == person[2].strip()]
    return matchande_personer

def hitta_adress(data, adress):
    """
    Funktionen söker efter personer med matchande adress


    """
    matchande_personer = [person for person in data if len(person) > 4 and adress == person[4].strip()]# vi söker i adress som är då fält nummer fyra
    return matchande_personer

class person:
    def __init__(self, filnamn):
        self.filnamn = filnamn
        self.data = läs_data_från_fil(filnamn)

    
    def skriv_data_till_fil(self):
        skriv_data_till_fil(self.filnamn, self.data)    
        

    def skriv_ut_person(self, person):
        """
        Funktionen skriver ut alla sparade kontakter

        """
        print(f"{person[0]} {person[1]} {person[2]} {person[3]} {person[4]}") 

    def lägg_till_person(self, ny_person):
        """
        Funktionen används för att lägga till personer

        """
        self.data.append(ny_person) #append används för att lägga till data på vår gamla data
        print("Personen är tillagd.\n", self.data)
        

    def ta_bort_person(self, namn):
        """
        Den här funktionen används för att ta söka efter kontakter och ta bort kontakten om den finns

    
        """
        matchande_personer = hitta_namn(self.data,namn)
        if matchande_personer: 
            for person in matchande_personer:
                self.data.remove(person)
            print("kontakten är borttagen.\n", self.data)
        else:
            print("kontakten hittades inte.")

    def uppdatera_person(self, matchande_personer, ny_telefon="", ny_epost="", ny_adress=""):
        """
        Den här funktionen används för att uppdatera kontakten 


        """
        for person in matchande_personer: 
            person[2] = ny_telefon if ny_telefon else person[2] #spara nytt telefonummer om den ska ändras
            person[3] = ny_epost if ny_epost else person[3]#spara ny epost om den ska ändras 
            person[4] = ny_adress if ny_adress else person[4]#spara ny adress om den ska ändras
            print("kontakten uppdaterad\n", self.data)
    
    def sorteringsnyckel(self, person):
        """
        sortera namn utan semikolumn i mellan.
        :return: för och efternamn
        """
        return person[0], person[1] 

    def skriv_ut_sorterad_data(self):
        """
        skriver ut data efter sortering utan semikolon


        """
        sorterad_data = sorted(self.data, key=self.sorteringsnyckel)
        for person in sorterad_data: 
            self.skriv_ut_person(person)


    def Sök_efter_namn(self):
        """
        val 1 för att söka efter kontakten via namn och returnerar matchande personer

    
        """
        while True:
            namn = input("Ange namn: ")
            if all(char.isalpha() or char.isspace() for char in namn):
                matchande_personer = hitta_namn(self.data,namn)
                if matchande_personer:
                    for person in matchande_personer:
                        self.skriv_ut_person(person)
                else:
                    print("Ingen matchande namn hittad.")
                break
            else:
                print("skriv bara bokstäver.")
        
    def Sök_efter_epost(self):
        """
        val 2 för att söka efter kontakten via epost.

        
        """
        while True:
            epost = input("Ange epost: ")
            if valid_email(epost):
                matchande_personer = hitta_epost(self.data, epost)
                if matchande_personer:
                    for person in matchande_personer:
                        self.skriv_ut_person(person)
                else:
                    print("Ingen matchande epost hittades.")
                break
            else:
                print("epost måste innehålla '.' punkt och '@' snabel-a")

    def Sök_efter_telefonnummer(self):
        """
        val 3 för att söka efter kontakten via telefonnummer.

    
        """
        while True:
            telefon = input("Ange telefonnummer: ") 
            if(telefon.isdigit()):
                matchande_personer = hitta_telefon(self.data, telefon)
                if matchande_personer:
                    for person in matchande_personer:
                        self.skriv_ut_person(person)
                else:
                    print("Ingen matchande telefonnumer hittades.")
                break
            else:
                print("din inmatning måste bara innehålla siffror")

    def Sök_efter_adress(self):
        """
        val 4 för att söka efter kontakten via adress.

        
        """
        adress = input("Ange adress: ")
        matchande_personer = hitta_adress(self.data, adress)
        if matchande_personer:
            for person in matchande_personer:
                self.skriv_ut_person(person)
                
        else:
            print("Ingen matchande adress hittad.")

    def person_tillägning(self):
        """
        val 5 för att lägga till en kontakt.

        
        """
        while True:
            efternamn = input("Ange efternamn: ")
            förnamn = input("Ange förnamn: ")
            telefonnummer = input("Ange telefonnummer: ")
            epost = input("Ange epost: ")
            adress = input("Ange adress: ")
            
            if (not efternamn.isalpha() or not förnamn.isalpha() or not telefonnummer.isdigit() or not valid_email(epost)):
                print("Namn måste bara innehålla bokstäver, telefonnummer måste bara innehålla siffror och epost måste innehålla '@' och '.' ")
            elif (not all([efternamn, förnamn, telefonnummer, epost, adress])):
                print("Alla fält måste vara ifyllda. Försök igen.")
            else:
                ny_person = [efternamn, förnamn, telefonnummer, epost, adress]
                self.lägg_till_person(ny_person)  
                break

    def uppdatera_kontakt(self):
        """
        val 7 för att söka efter kontakten och uppdatera den.
        
        """
        while True:
            namn = input("Ange namn att uppdatera:")
            if all(char.isalpha() or char.isspace() for char in namn):
                matchande_personer = hitta_namn(self.data, namn)
                if matchande_personer:
                    while True:
                        ny_telefon = input("Ange nytt telefonnummer (lämna tomt för att behålla befintligt): ")
                        ny_epost = input("Ange ny epost (lämna tomt för att behålla befintligt): ")
                        ny_adress = input("Ange ny adress (lämna tomt för att behålla befintligt): ")

                        if ny_telefon and not ny_telefon.isdigit():
                            print("Telefonnumret måste bara innehålla siffror.")
                            continue

                        if ny_epost and not valid_email(ny_epost):
                            print("Ogiltigt epost-format.")
                            continue
                        self.uppdatera_person(matchande_personer, ny_telefon, ny_epost, ny_adress)
                        break
                    break
                else:
                    print("Kontakten hittades inte.")
            else:
                print("Skriv bara bokstäver.")

def main():
    personer_loaded = person("person_register.txt")
    print(personer_loaded.data)
    while True:
        print(
            "\n1. Sök efter namn\n"
            "2. Sök efter epost\n"
            "3. Sök efter telefon\n"
            "4. Sök efter adress\n"
            "5. Lägg till ny person\n"
            "6. Ta bort person\n"
            "7. Uppdatera person\n"
            "8. Skriv ut sorterad data\n"
            "9. Avsluta"
        )

        val = input("Ange ditt val (1-9): ")

        if val == '1':
            personer_loaded.Sök_efter_namn()
        
        elif val == '2':
            personer_loaded.Sök_efter_epost()
        
        elif val == '3':
            personer_loaded.Sök_efter_telefonnummer()
        
        elif val == '4':
            personer_loaded.Sök_efter_adress()

        elif val == '5':
            personer_loaded.person_tillägning()

        elif val == '6':
            namn = input("Ange namn att ta bort: ")
            if all(char.isalpha() or char.isspace() for char in namn):
                personer_loaded.ta_bort_person(namn)
            else:
                print("skriv bara bokstäver.")

        elif val == '7':
            personer_loaded.uppdatera_kontakt()

        elif val == '8':
            personer_loaded.skriv_ut_sorterad_data()

        elif val == '9':
            personer_loaded.skriv_data_till_fil()
            print("Programmet avslutas. Data sparad.")
            break
        else:
            print("Ogiltigt val. Ange ett nummer mellan 1 och 9.")

# Kontrollera om skriptet körs direkt och inte importeras som ett modul

if __name__ == "__main__":
    main()
