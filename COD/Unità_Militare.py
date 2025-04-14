class Unità_Militare:
    def __init__(self, nome, numero_militari):
        self.nome_unità = nome
        self.numero_militari = numero_militari

    def __str__(self):
        return f"Unità: {self.nome_unità}, Numero di militari: {self.numero_militari}"
    
    def muovi(self, distanza):
        print(f"L'unità {self.nome_unità} si muove di {distanza} km.")
        
    def attacca(self, obiettivo):
        print(f"L'unità {self.nome_unità} attacca l'obiettivo {obiettivo}.")
        
    def ritirati(self):
        print(f"L'unità {self.nome_unità} si ritira.")


class Fanteria(Unità_Militare):
    def __init__(self, nome, numero_militari, tipo_arma):
        super().__init__(nome, numero_militari)
        self.tipo_arma = tipo_arma

    def __str__(self):
        return f"Fanteria: {self.nome_unità}, Militari: {self.numero_militari}, Arma: {self.tipo_arma}"
    
    def attacca(self, obiettivo):
        print(f"La fanteria {self.nome_unità} attacca {obiettivo} con {self.tipo_arma}.")


class Cavalleria(Unità_Militare):
    def __init__(self, nome, numero_militari, tipo_veicolo):
        super().__init__(nome, numero_militari)
        self.tipo_veicolo = tipo_veicolo

    def __str__(self):
        return f"Cavalleria: {self.nome_unità}, Militari: {self.numero_militari}, Veicolo: {self.tipo_veicolo}"
    
    def attacca(self, obiettivo):
        print(f"La cavalleria {self.nome_unità} attacca {obiettivo} con {self.tipo_veicolo}.")


class Artiglieria(Unità_Militare):
    def __init__(self, nome, numero_militari, tipo_cannone):
        super().__init__(nome, numero_militari)
        self.tipo_cannone = tipo_cannone

    def __str__(self):
        return f"Artiglieria: {self.nome_unità}, Militari: {self.numero_militari}, Cannone: {self.tipo_cannone}"
    
    def attacca(self, obiettivo):
        print(f"L'artiglieria {self.nome_unità} attacca {obiettivo} con {self.tipo_cannone}.")


class Supporto_Logistico(Unità_Militare):
    def __init__(self, nome, numero_militari, tipo_supporto):
        super().__init__(nome, numero_militari)
        self.tipo_supporto = tipo_supporto

    def __str__(self):
        return f"Supporto Logistico: {self.nome_unità}, Militari: {self.numero_militari}, Supporto: {self.tipo_supporto}"
    
    def attacca(self, obiettivo):
        print(f"Il supporto logistico {self.nome_unità} supporta l'attacco a {obiettivo} con {self.tipo_supporto}.")


class Ricognizione(Unità_Militare):
    def __init__(self, nome, numero_militari, tipo_veicolo):
        super().__init__(nome, numero_militari)
        self.tipo_veicolo = tipo_veicolo

    def __str__(self):
        return f"Ricognizione: {self.nome_unità}, Militari: {self.numero_militari}, Veicolo: {self.tipo_veicolo}"
    
    def attacca(self, obiettivo):
        print(f"La ricognizione {self.nome_unità} sorveglia {obiettivo} con {self.tipo_veicolo}.")


class Controllo_Militare:
    def __init__(self):
        self.unita_registrate = {}

    def mostra_menu(self):
        print("\n=== Menu Controllo Militare ===")
        print("1. Mostra unità militari")
        print("2. Aggiungi unità militare")
        print("3. Dettagli di un'unità")
        print("4. Attacca un obiettivo")
        print("5. Esci")

    def aggiungi_unita(self):
        print("Tipi disponibili: Fanteria, Cavalleria, Artiglieria, Supporto_Logistico, Ricognizione")
        tipo = input("Tipo di unità: ").strip().lower()

        nome = input("Nome unità: ")
        numero = int(input("Numero militari: "))

        if tipo == "fanteria":
            arma = input("Tipo di arma: ")
            unita = Fanteria(nome, numero, arma)
        elif tipo == "cavalleria":
            veicolo = input("Tipo di veicolo: ")
            unita = Cavalleria(nome, numero, veicolo)
        elif tipo == "artiglieria":
            cannone = input("Tipo di cannone: ")
            unita = Artiglieria(nome, numero, cannone)
        elif tipo == "supporto_logistico":
            supporto = input("Tipo di supporto: ")
            unita = Supporto_Logistico(nome, numero, supporto)
        elif tipo == "ricognizione":
            veicolo = input("Tipo di veicolo: ")
            unita = Ricognizione(nome, numero, veicolo)
        else:
            print("Tipo non valido.")
            return

        self.unita_registrate[nome] = unita
        print(f"Unità '{nome}' registrata con successo!")

    def mostra_unita(self):
        if not self.unita_registrate:
            print("Nessuna unità registrata.")
            return
        for unita in self.unita_registrate.values():
            print(unita)

    def dettagli_unita(self):
        nome = input("Nome unità: ")
        unita = self.unita_registrate.get(nome)
        if unita:
            print(unita)
        else:
            print("Unità non trovata.")

    def attacca_unita(self):
        nome = input("Nome unità: ")
        obiettivo = input("Obiettivo: ")
        unita = self.unita_registrate.get(nome)
        if unita:
            unita.attacca(obiettivo)
        else:
            print("Unità non trovata.")

    def esegui(self):
        while True:
            self.mostra_menu()
            scelta = input("Scegli un'opzione: ")
            if scelta == "1":
                self.mostra_unita()
            elif scelta == "2":
                self.aggiungi_unita()
            elif scelta == "3":
                self.dettagli_unita()
            elif scelta == "4":
                self.attacca_unita()
            elif scelta == "5":
                print("Chiusura sistema.")
                break
            else:
                print("Scelta non valida.")


# ▶️ Avvio programma
if __name__ == "__main__":
    controllo = Controllo_Militare()
    controllo.esegui()
