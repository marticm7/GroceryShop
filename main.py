hleb_cena = 30
jaja_cena = 14
secer_cena = 70

hleb_kolicina = int(input("Unesite kolicinu hleba: "))
jaja_kolicina = int(input("Unesite kolicinu jaja: "))
secer_kolicina = int(input("Unesite kolicinu secera: "))

trosak = hleb_cena * hleb_kolicina + jaja_cena * jaja_kolicina + secer_cena * secer_kolicina

print("Ukupan trosak je", trosak)

