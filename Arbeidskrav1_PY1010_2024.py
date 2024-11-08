# -*- coding: utf-8 -*-
"""
-------------------------------
PY1010 - Arbeidskrav 1

Av: Nur Ismail (212381@usn.no)

Oppdatert 2024 11 08
--------------------------------
Oppgave
Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.
Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. 
Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like uansett om de kjøper elbil eller bensinbil). 
Verdiene skal presenteres som heltall, dvs. tall uten desimaler. Bruk da f-strengformatering som demonstrert i kodeeksempelet print(f'x4 = {x4:.3f} og y4 = {y4:.1f}') 
i dette programmet i læreboka http://techteach.no/python/files/prog_print_format.py. 
Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)
1. Antall kjørte km/år skal angis i konsollen og registreres av programmet vha. input-funksjonen. (Angi f.eks. 10.000 km.)
2. Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
3. Trafikkforsikringsavgift (gjeldende fra mars 2021): Elbil: 5,85 kr/dag. Bensinbil: 8,40 kr/dag.
4. Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
5. Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km. 

"""

# %% Inisialiering av varibler

ElBilTotalKostnad = 0.0                             # Totalkostnadene for elbil
BensinBilTotalKostnad = 0.0                         # Totalkostnadene for bensinbil 

ElOgBensinBilKostnadDiv = 0.0                       # Kostnadsdifferansen mellom elbil og bensinbil

AntallKjortKmPerAar = 0                             # Antall kjørte km/år. 

ForsikringElBil = 5000                              # Forsikring elbil per år
ForsikringBensinBil = 7500                          # Forsikring bensinbil per år

AntallDagerIaar = 365                               # Antalldager i et år
TrafikkAvgiftElbil = 5.85 * AntallDagerIaar         # Trafikkforsikringsavgift elbil      [kr/dag]
TrafikkAvgiftBensinbil = 8.38 * AntallDagerIaar     # Trafikkforsikringsavgift bensinbil  [kr/dag]

StrømPrisElbil = 2.00                               # 2.00kr/kW

ElBilForbrukKostnad = 0.2 * StrømPrisElbil          # Drivstoffbruk for elbil, 0,2 kWh/km, strømpris (antar kun hjemmelading): 2.00 kr/kWh.
BensinBilForbruk = 1.0                              # Drivstoffbruk for bensinbil, bensinbil: 1,0 kr/km. 

BomAvgiftElbil = 0.1                                # Bomavgift for elbil, 0,1 kr/km.
BomAvgiftBensinbil = 0.3                            # Bomavgift for elbil, 0,3 kr/km.

# %% Beregninger: 

# Skal angis i konsollen og registreres av programmet vha. input-funksjonen.   
AntallKjortKmPerAar = int(input("Tast inn antall kjørelengde i km per år for å sammenligne de årlige kostnadene ved elbil sammenlignet med bensinbil? : "))

#Beregning av kostnadene til Elbil og Bensin bil, så å finne kostnad differensen mellom dem.     
ElBilTotalKostnad       = ( AntallKjortKmPerAar * ( BomAvgiftElbil     + ElBilForbrukKostnad ) + ( ForsikringElBil     + TrafikkAvgiftElbil      ))
BensinBilTotalKostnad   = ( AntallKjortKmPerAar * ( BomAvgiftBensinbil + BensinBilForbruk   )) + ( ForsikringBensinBil + TrafikkAvgiftBensinbil   )
ElOgBensinBilKostnadDiv =   BensinBilTotalKostnad - ElBilTotalKostnad

#Skriver ut resultater av beregning til konsollen.
print ( 'Årlig totalkostnadene for elbil =                ', f'{ElBilTotalKostnad:.0f},-kr'       )
print ( 'Årlig totalkostnadene for bensinbil =            ', f'{BensinBilTotalKostnad:.0f},-kr'   )
print ( 'Kostnadsdifferansen mellom elbil og bensinbil =  ', f'{ElOgBensinBilKostnadDiv:.0f},-kr' )