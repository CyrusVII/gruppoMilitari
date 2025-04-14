import DbConnetion as db
import random
import time

# ----------------------------- CLASSE BASE UNITA MILITARE -----------------------------
class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def __str__(self):
        return f"Unità: {self.nome}, Numero di soldati: {self.numero_soldati}"

    def attacca(self, obiettivo):
        print(f"L'unità {self.nome} attacca l'obiettivo {obiettivo}.")

    def ritira(self):
        print(f"L'unità {self.nome} si ritira strategicamente.")
        
    def probabilita_attacco(self):
        pass

# ----------------------------- FANteria -----------------------------
class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_arma):
        super().__init__(nome, numero_soldati)
        self.tipo_arma = tipo_arma

    def __str__(self):
        return f"Fanteria: {self.nome}, Soldati: {self.numero_soldati}, Arma: {self.tipo_arma}"

    def attacca(self, obiettivo):
        print(f"La fanteria {self.nome} attacca {obiettivo} con {self.tipo_arma}.")

    def probabilita_attacco(self):
        return 0.4 if self.tipo_arma.lower() == "ak47" else 0.2

# ----------------------------- ARTIGLIERIA -----------------------------
class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_cannone):
        super().__init__(nome, numero_soldati)
        self.tipo_cannone = tipo_cannone

    def __str__(self):
        return f"Artiglieria: {self.nome}, Soldati: {self.numero_soldati}, Cannone: {self.tipo_cannone}"

    def attacca(self, obiettivo):
        print(f"L'artiglieria {self.nome} attacca {obiettivo} con {self.tipo_cannone}.")

    def probabilita_attacco(self):
        return 0.35 if self.tipo_cannone.lower() == "granata" else 0.25

# ----------------------------- CAVALLERIA -----------------------------
class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_veicolo):
        super().__init__(nome, numero_soldati)
        self.tipo_veicolo = tipo_veicolo

    def __str__(self):
        return f"Cavalleria: {self.nome}, Soldati: {self.numero_soldati}, Veicolo: {self.tipo_veicolo}"

    def attacca(self, obiettivo):
        print(f"La cavalleria {self.nome} attacca {obiettivo} con {self.tipo_veicolo}.")

    def probabilita_attacco(self):
        return 0.3

# ----------------------------- SUPPORTO LOGISTICO -----------------------------
class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_supporto):
        super().__init__(nome, numero_soldati)
        self.tipo_supporto = tipo_supporto

    def __str__(self):
        return f"Supporto Logistico: {self.nome}, Soldati: {self.numero_soldati}, Supporto: {self.tipo_supporto}"

    def attacca(self, obiettivo):
        print(f"Il supporto logistico {self.nome} supporta l'attacco a {obiettivo} con {self.tipo_supporto}.")

    def probabilita_attacco(self):
        return 0.25 if self.tipo_supporto.lower() == "audi" else 0.4

# ----------------------------- RICOGNIZIONE -----------------------------
class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati, tipo_veicolo):
        super().__init__(nome, numero_soldati)
        self.tipo_veicolo = tipo_veicolo

    def __str__(self):
        return f"Ricognizione: {self.nome}, Soldati: {self.numero_soldati}, Veicolo: {self.tipo_veicolo}"

    def attacca(self, obiettivo):
        print(f"La ricognizione {self.nome} sorveglia {obiettivo} con il veicolo {self.tipo_veicolo}.")

    def probabilita_attacco(self):
        return 0.2 if self.tipo_veicolo.lower() == "camionetta" else 0.1


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

        for r in righe:
            nome = r[1]
            numero_soldati = r[2]
            tipo = r[3]
            specialita = r[4]
            
            # Crea l'oggetto in base alla specialità
            if tipo == "Fanteria":
                unita = Fanteria(nome, numero_soldati, specialita)
            elif tipo == "Artiglieria":
                unita = Artiglieria(nome, numero_soldati, specialita)
            elif tipo == "Cavalleria":
                unita = Cavalleria(nome, numero_soldati, specialita)
            elif tipo == "SupportoLogistico":
                unita = SupportoLogistico(nome, numero_soldati, specialita)
            elif tipo == "Ricognizione":
                unita = Ricognizione(nome, numero_soldati, specialita)
            else:
                print(f"Specialità sconosciuta: {tipo}")
                continue
            
            # Inserisci l'unità nel dizionario corrispondente
            if nome.lower() == "rosso":
                self.rossi[tipo] = unita
            elif nome.lower() == "blu":
                self.blu[tipo] = unita
        cursor.close()
        myDb.close()

    def calcola_successo(self, unita):
        return unita.probabilita_attacco()

    def attacco(self, attaccante, difensore):
        successo = self.calcola_successo(attaccante)
        if random.random() < successo:
            difensore.numero_soldati -= 1
            print(f"✅ {attaccante.nome} ha colpito {difensore.nome}!")
        else:
            print(f"❌ {attaccante.nome} ha fallito l'attacco contro {difensore.nome}.")

    def aggiorna_percentuali_resa(self):
        totale_rossi = sum(u.numero_soldati for u in self.rossi.values())
        totale_blu = sum(u.numero_soldati for u in self.blu.values())

        percentuale_rossi = (totale_rossi / 50) * 100  
        percentuale_blu = (totale_blu / 50) * 100  

        print(f"📉 Percentuale resa Rossi: {percentuale_rossi:.1f}%")
        print(f"📉 Percentuale resa Blu: {percentuale_blu:.1f}%")

        if percentuale_rossi >= 80:
            print("🟥 I Rossi si arrendono!")
            return "blu"
        elif percentuale_blu >= 80:
            print("🟦 I Blu si arrendono!")
            return "rosso"
        return None

    def turno(self, attaccanti, difensori):
        if not attaccanti or not difensori:
            return
        unita_attaccante = random.choice(list(attaccanti.values()))
        unita_difensore = random.choice(list(difensori.values()))
        print(f"\n⚔️ {unita_attaccante.nome} attacca {unita_difensore.nome}!")
        self.attacco(unita_attaccante, unita_difensore)

    def play(self):
        round = 1
        while self.rossi and self.blu:
            print(f"\n======= ROUND {round} =======")
            self.turno(self.rossi, self.blu)
            time.sleep(1)
            self.turno(self.blu, self.rossi)
            self.aggiorna_percentuali_resa()

            risultato = self.aggiorna_percentuali_resa()
            if risultato:
                print(f"🎉 Vittoria per la squadra {risultato.upper()}!")
                return
            round += 1
            time.sleep(1)

# ----------------------------- AVVIO PROGRAMMA -----------------------------
if __name__ == "__main__":
    cm = ControlloMilitare()
    cm.getData()
    cm.play()