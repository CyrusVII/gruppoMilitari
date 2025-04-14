import DbConnetion as db
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
        self.rossi = {}
        self.blu = {}

    def getData(self):
        myDb = db.db_connection("esercito")
        cursor = myDb.cursor()
        query = "SELECT id, nome, numero_soldati, tipo, specialita FROM unitamilitare"
        cursor.execute(query)
        righe = cursor.fetchall()

        for riga in righe:
            id_unita, nome, numero_soldati, tipo, specialita = riga

            # Crea l'oggetto in base alla specialità
            if specialita == "Fanteria":
                unita = Fanteria(nome, numero_soldati, tipo)
            elif specialita == "Artiglieria":
                unita = Artiglieria(nome, numero_soldati, tipo)
            elif specialita == "Cavalleria":
                unita = Cavalleria(nome, numero_soldati, tipo)
            elif specialita == "SupportoLogistico":
                unita = SupportoLogistico(nome, numero_soldati, tipo)
            elif specialita == "Ricognizione":
                unita = Ricognizione(nome, numero_soldati, tipo)
            else:
                print(f"Specialità sconosciuta: {specialita}")
                continue

            # Inserisci l'unità nel dizionario corrispondente
            if nome.lower() == "rosso":
                self.rossi[specialita] = unita
            elif nome.lower() == "blu":
                self.blu[specialita] = unita
        print(self.rossi)
        print(self.blu)
        cursor.close()
        myDb.close()
    



# ▶️ Avvio programma
if __name__ == "__main__":
  cm = ControlloMilitare()
  cm.getData()