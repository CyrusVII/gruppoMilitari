class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def __str__(self):
        return f"Unità: {self.nome}, Numero di soldati: {self.numero_soldati}"

    def muovi(self, distanza):
        print(f"L'unità {self.nome} si muove di {distanza} km.")

    def attacca(self, obiettivo):
        print(f"L'unità {self.nome} attacca l'obiettivo {obiettivo}.")

    def ritira(self):
        print(f"L'unità {self.nome} si ritira strategicamente.")


class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_arma):
        super().__init__(nome, numero_soldati)
        self.tipo_arma = tipo_arma

    def __str__(self):
        return f"Fanteria: {self.nome}, Soldati: {self.numero_soldati}, Arma: {self.tipo_arma}"

    def attacca(self, obiettivo):
        print(f"La fanteria {self.nome} attacca {obiettivo} con {self.tipo_arma}.")

    def costruisci_trincea(self):
        print(f"La fanteria {self.nome} costruisce una trincea per difesa temporanea.")


class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_cannone):
        super().__init__(nome, numero_soldati)
        self.tipo_cannone = tipo_cannone

    def __str__(self):
        return f"Artiglieria: {self.nome}, Soldati: {self.numero_soldati}, Cannone: {self.tipo_cannone}"

    def attacca(self, obiettivo):
        print(f"L'artiglieria {self.nome} attacca {obiettivo} con {self.tipo_cannone}.")

    def calibra_artiglieria(self):
        print(f"L'artiglieria {self.nome} calibra i pezzi per una maggiore precisione.")


class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_veicolo):
        super().__init__(nome, numero_soldati)
        self.tipo_veicolo = tipo_veicolo

    def __str__(self):
        return f"Cavalleria: {self.nome}, Soldati: {self.numero_soldati}, Veicolo: {self.tipo_veicolo}"

    def attacca(self, obiettivo):
        print(f"La cavalleria {self.nome} attacca {obiettivo} con {self.tipo_veicolo}.")

    def esplora_terreno(self):
        print(f"La cavalleria {self.nome} esplora il terreno per informazioni sul nemico.")


class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_supporto):
        super().__init__(nome, numero_soldati)
        self.tipo_supporto = tipo_supporto

    def __str__(self):
        return f"Supporto Logistico: {self.nome}, Soldati: {self.numero_soldati}, Supporto: {self.tipo_supporto}"

    def attacca(self, obiettivo):
        print(f"Il supporto logistico {self.nome} assiste l'attacco a {obiettivo} con {self.tipo_supporto}.")

    def rifornisci_unita(self):
        print(f"Il supporto logistico {self.nome} rifornisce e manutiene le unità sul campo.")


class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_veicolo):
        super().__init__(nome, numero_soldati)
        self.tipo_veicolo = tipo_veicolo

    def __str__(self):
        return f"Ricognizione: {self.nome}, Soldati: {self.numero_soldati}, Veicolo: {self.tipo_veicolo}"

    def attacca(self, obiettivo):
        print(f"La ricognizione {self.nome} sorveglia {obiettivo} con il veicolo {self.tipo_veicolo}.")

    def conduci_ricognizione(self):
        print(f"La ricognizione {self.nome} conduce una missione di sorveglianza.")


class ControlloMilitare(Fanteria, Cavalleria, Artiglieria, SupportoLogistico, Ricognizione):
    def __init__(self):
        self.unita_registrate = {}

    def mostra_menu(self):
        print("\n=== Menu Controllo Militare ===")
        print("1. Mostra unità militari")
        print("2. Aggiungi unità militare")
        print("3. Dettagli di un'unità")
        print("4. Attacca un obiettivo")
        print("5. Esci")

    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Unità '{unita.nome}' registrata con successo!")

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

    def aggiungi_unita(self):
        print("Tipi disponibili: Fanteria, Cavalleria, Artiglieria, SupportoLogistico, Ricognizione")
        tipo = input("Tipo di unità: ").strip().lower()
        nome = input("Nome unità: ")
        numero = int(input("Numero soldati: "))

        if tipo == "fanteria":
            arma = input("Tipo di arma: ")
            unita = Fanteria(nome, numero, arma)
        elif tipo == "cavalleria":
            veicolo = input("Tipo di veicolo: ")
            unita = Cavalleria(nome, numero, veicolo)
        elif tipo == "artiglieria":
            cannone = input("Tipo di cannone: ")
            unita = Artiglieria(nome, numero, cannone)
        elif tipo == "supportologistico":
            supporto = input("Tipo di supporto: ")
            unita = SupportoLogistico(nome, numero, supporto)
        elif tipo == "ricognizione":
            veicolo = input("Tipo di veicolo: ")
            unita = Ricognizione(nome, numero, veicolo)
        else:
            print("Tipo non valido.")
            return

        self.registra_unita(unita)

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


# ▶ Avvio programma
if __name__ == "__main__":
    controllo = ControlloMilitare()
    controllo.esegui()
