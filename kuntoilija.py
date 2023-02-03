# KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
# =====================================

# KIRJASTOT JA MODUULIT (LIBRARIES AND MODULES)
# ---------------------------------------------

import fitness

# LUOKKAMÄÄRITYKSET (CLASS DEFINITIONS)
# -------------------------------------

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
    
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
    
    #Metodi painoindeksin laskemiseen
    def painoindeksi(self):
        bmi = fitness.laske_bmi(self.paino, self.pituus)
        print(bmi)

if __name__ == "__main__":

    # Luodaan olio luokasta Kuntoilija
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 180, 80, 30, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    kuntoilija.painoindeksi()


    