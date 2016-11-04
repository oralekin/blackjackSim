import random

deste = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13",
         "K01", "K02", "K03", "K04", "K05", "K06", "K07", "K08", "K09", "K10", "K11", "K12", "K13",
         "Q01", "Q02", "Q03", "Q04", "Q05", "Q06", "Q07", "Q08", "Q09", "Q10", "Q11", "Q12", "Q13",
         "M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"]
# Sinek Karo Kupa Maça

distaki = []
class Kart:
    @staticmethod
    def kartcek(self):

def karistir(listt, ite):
    for _ in range(1, ite):
        i = 0
        for kart in listt:
            if random.randint(0, 1) == 1:
                del listt[i]
                distaki.append(kart)
            i += 1
    return listt + distaki

deste = karistir(deste, 7)
