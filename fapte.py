class OperaDeArtaDigitala:
    def __init__(self, nume, artist, tehnica, culori_calde, stil_impresionist, format_salvare, software, rezolutie,
                 lumini_umbre, distributie_online, anonimat, modificabilitate, comunitati_online, animatie,
                 luminare, realitate_virtuala, stil_minimalist, tehnici_variate, artefacte_digitale, multimedia):
        self.nume = nume
        self.artist = artist
        self.tehnica = tehnica
        self.culori_calde = culori_calde
        self.stil_impresionist = stil_impresionist
        self.format_salvare = format_salvare
        self.software = software
        self.rezolutie = rezolutie
        self.lumini_umbre = lumini_umbre
        self.distributie_online = distributie_online
        self.anonimat = anonimat
        self.modificabilitate = modificabilitate
        self.comunitati_online = comunitati_online
        self.animatie = animatie
        self.luminare = luminare
        self.realitate_virtuala = realitate_virtuala
        self.stil_minimalist = stil_minimalist
        self.tehnici_variate = tehnici_variate
        self.artefacte_digitale = artefacte_digitale
        self.multimedia = multimedia


class EvaluareArtaDigitala:
    def __init__(self, opera):
        self.opera = opera
        self.nota_finala = 0.0

    def evaluare_culori_calde(self):
        if self.opera.culori_calde:
            self.nota_finala += 0.2
            print("Utilizarea culorilor calde poate transmite o atmosferă călduroasă - Evaluat pozitiv.")
        else:
            print("Utilizarea culorilor calde poate transmite o atmosferă călduroasă - Evaluat negativ.")

    def evaluare_stil_impresionist(self):
        if self.opera.stil_impresionist:
            self.nota_finala += 0.2
            print("Stilul impresionist poate folosi tușe mari și texturi abstracte - Evaluat pozitiv.")
        else:
            print("Stilul impresionist poate folosi tușe mari și texturi abstracte - Evaluat negativ.")

    def evaluare_rezolutie(self):
        if self.opera.rezolutie >= 2000:
            self.nota_finala += 0.3
            print(
                "Dacă rezoluția operei de artă digitală este mare, atunci detaliile vor fi mai vizibile - Evaluat pozitiv.")
        else:
            print(
                "Dacă rezoluția operei de artă digitală este mare, atunci detaliile vor fi mai vizibile - Evaluat negativ.")

    def evaluare_efecte_vizuale(self):
        if self.opera.luminare and self.opera.stil_minimalist:
            self.nota_finala += 0.2
            print(
                "Dacă opera de artă digitală utilizează efecte vizuale puternice, atunci aceasta poate transmite mesaje emoționale mai puternice - Evaluat pozitiv.")
        else:
            print(
                "Dacă opera de artă digitală utilizează efecte vizuale puternice, atunci aceasta poate transmite mesaje emoționale mai puternice - Evaluat negativ.")

    def evaluare_distributie_online(self):
        if self.opera.distributie_online:
            self.nota_finala += 0.2
            print(
                "Dacă opera de artă digitală este distribuită online, atunci accesul la ea va fi mai extins - Evaluat pozitiv.")
        else:
            print(
                "Dacă opera de artă digitală este distribuită online, atunci accesul la ea va fi mai extins - Evaluat negativ.")
    def evaluare_efecte(self):
        if self.evaluare_culori_calde and self.evaluare_efecte_vizuale:
            self.nota_finala += 0.2
            print("Daca opera de arta digitala contine ambele efecte, atunci opera va avea un efect vizual mai puternic - Efect pozitiv.")
        else:
            print(
                "Daca opera de arta digitala contine ambele efecte, atunci opera va avea un efect vizual mai puternic - Efect negativ.")
    def calculeaza_nota_finala(self):
        print(f"Nota finală pentru {self.opera.nume} de către {self.opera.artist}: {self.nota_finala * 10}/10")



opera_digitala1 = OperaDeArtaDigitala(
    nume="Diversitate Digitală",
    artist="Alice Digital",
    tehnica="Grafică vectorială",
    culori_calde=True,
    stil_impresionist=False,
    format_salvare="PNG",
    software="Adobe Illustrator",
    rezolutie=1920,
    lumini_umbre=True,
    distributie_online=True,
    anonimat=True,
    modificabilitate=True,
    comunitati_online=True,
    animatie=False,
    luminare=True,
    realitate_virtuala=False,
    stil_minimalist=True,
    tehnici_variate=True,
    artefacte_digitale=False,
    multimedia=True
)

opera_digitala2 = OperaDeArtaDigitala(
    nume="Reflectare Urbană",
    artist="Alex Pixel",
    tehnica="Ilustrație digitală",
    culori_calde=False,
    stil_impresionist=True,
    format_salvare="TIFF",
    software="Adobe Illustrator",
    rezolutie=3000,
    lumini_umbre=True,
    distributie_online=True,
    anonimat=True,
    modificabilitate=False,
    comunitati_online=True,
    animatie=False,
    luminare=True,
    realitate_virtuala=False,
    stil_minimalist=False,
    tehnici_variate=True,
    artefacte_digitale=False,
    multimedia=False
)

opera_digitala3 = OperaDeArtaDigitala(
    nume="Efemerida Virtuală",
    artist="Max DigiArt",
    tehnica="Arte digitală abstractă",
    culori_calde=True,
    stil_impresionist=True,
    format_salvare="PNG",
    software="Coral Painter",
    rezolutie=2048,
    lumini_umbre=False,
    distributie_online=True,
    anonimat=True,
    modificabilitate=True,
    comunitati_online=True,
    animatie=True,
    luminare=False,
    realitate_virtuala=False,
    stil_minimalist=False,
    tehnici_variate=True,
    artefacte_digitale=False,
    multimedia=True
)

opera_digitala4 = OperaDeArtaDigitala(
    nume="Minimalism Digital",
    artist="Mia Pixela",
    tehnica="Design minimalist digital",
    culori_calde=False,
    stil_impresionist=False,
    format_salvare="SVG",
    software="Inkscape",
    rezolutie=1200,
    lumini_umbre=False,
    distributie_online=True,
    anonimat=True,
    modificabilitate=True,
    comunitati_online=True,
    animatie=False,
    luminare=False,
    realitate_virtuala=False,
    stil_minimalist=True,
    tehnici_variate=False,
    artefacte_digitale=False,
    multimedia=False
)

opera_digitala5 = OperaDeArtaDigitala(
    nume="Explorare Digitală",
    artist="Oliver TechArt",
    tehnica="Fotomanipulare digitală",
    culori_calde=True,
    stil_impresionist=False,
    format_salvare="Gif",
    software="Adobe Illustrator",
    rezolutie=1600,
    lumini_umbre=True,
    distributie_online=True,
    anonimat=False,
    modificabilitate=True,
    comunitati_online=True,
    animatie=True,
    luminare=True,
    realitate_virtuala=False,
    stil_minimalist=False,
    tehnici_variate=False,
    artefacte_digitale=True,
    multimedia=True
)

sistem_evaluare_arta_digitala1 = EvaluareArtaDigitala(opera_digitala1)
print("")
sistem_evaluare_arta_digitala1.evaluare_culori_calde()
sistem_evaluare_arta_digitala1.evaluare_stil_impresionist()
sistem_evaluare_arta_digitala1.evaluare_efecte_vizuale()
sistem_evaluare_arta_digitala1.evaluare_rezolutie()
sistem_evaluare_arta_digitala1.evaluare_distributie_online()
sistem_evaluare_arta_digitala1.evaluare_efecte()
print("")
sistem_evaluare_arta_digitala1.calculeaza_nota_finala()
print("")

sistem_evaluare_arta_digitala2 = EvaluareArtaDigitala(opera_digitala2)
print("")
sistem_evaluare_arta_digitala2.evaluare_culori_calde()
sistem_evaluare_arta_digitala2.evaluare_stil_impresionist()
sistem_evaluare_arta_digitala2.evaluare_efecte_vizuale()
sistem_evaluare_arta_digitala2.evaluare_rezolutie()
sistem_evaluare_arta_digitala2.evaluare_distributie_online()
sistem_evaluare_arta_digitala2.evaluare_efecte()
print("")
sistem_evaluare_arta_digitala2.calculeaza_nota_finala()
print("")

sistem_evaluare_arta_digitala3 = EvaluareArtaDigitala(opera_digitala3)
print("")
sistem_evaluare_arta_digitala3.evaluare_culori_calde()
sistem_evaluare_arta_digitala3.evaluare_stil_impresionist()
sistem_evaluare_arta_digitala3.evaluare_efecte_vizuale()
sistem_evaluare_arta_digitala3.evaluare_rezolutie()
sistem_evaluare_arta_digitala3.evaluare_distributie_online()
sistem_evaluare_arta_digitala3.evaluare_efecte()
print("")
sistem_evaluare_arta_digitala3.calculeaza_nota_finala()
print("")

sistem_evaluare_arta_digitala4 = EvaluareArtaDigitala(opera_digitala4)
print("")
sistem_evaluare_arta_digitala4.evaluare_culori_calde()
sistem_evaluare_arta_digitala4.evaluare_stil_impresionist()
sistem_evaluare_arta_digitala4.evaluare_efecte_vizuale()
sistem_evaluare_arta_digitala4.evaluare_rezolutie()
sistem_evaluare_arta_digitala4.evaluare_distributie_online()
sistem_evaluare_arta_digitala4.evaluare_efecte()
print("")
sistem_evaluare_arta_digitala4.calculeaza_nota_finala()
print("")

sistem_evaluare_arta_digitala5 = EvaluareArtaDigitala(opera_digitala5)
print("")
sistem_evaluare_arta_digitala5.evaluare_culori_calde()
sistem_evaluare_arta_digitala5.evaluare_stil_impresionist()
sistem_evaluare_arta_digitala5.evaluare_efecte_vizuale()
sistem_evaluare_arta_digitala5.evaluare_rezolutie()
sistem_evaluare_arta_digitala5.evaluare_distributie_online()
sistem_evaluare_arta_digitala5.evaluare_efecte()
print("")
sistem_evaluare_arta_digitala5.calculeaza_nota_finala()



