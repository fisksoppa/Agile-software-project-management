import pandas as pd

df = pd.DataFrame()
data = [['Volvo Tuve, Göteborg','Norra Stenebyvägen 5', '19 oct', '8:30 - 15:00', '57.75793077168005', '11.885288966539886'],
        ['Hamnnplan, Öckerö','Lammholmsvägen 13' ,'28 nov, 29 nov','13:30 - 18:00, 13:30 - 18:00', '57.70528881808817', '11.657308891433228'],
        ['Torslanda, Göteborg', 'Gamla Flygplatsvägen 60', '-', '-', '57.71007251649718', '11.773084736917019'],
        ['Arendalsvarvet, Göteborg', 'Arendals Skans 2', '24 nov, 25 nov', '8:30 - 15:00, 11:00 - 15:00', '57.696924916214165', '11.82092758238937'],
        ['Volvo TK, Göteborg', 'Personalvägen 23', '-', '-', '57.71914107962158', '11.845346263780499'],
        ['Volvo SA, Göteborg', 'Gustaf Larssons väg 16', '21 sept, 22 sept, 23 sept, 2 nov, 3 nov, 4 nov, 14 dec, 15 dec, 16 dec', '08:30 - 15:00, 08:30 - 15:00,08:30 - 15:00,08:30 - 15:00,08:30 - 15:00,08:30 - 15:00,08:30 - 15:00,08:30 - 15:00, 11:00 - 15:00', '57.72667813349899', '11.861120535834463'],
        ['Volvo Lundby, Göteborg', 'Gropegårdsgatan 11', '29 sept, 30 sept, 7 nov, 8 nov, 22 dec, 23 dec', '8:30 - 15:00, 11:00 - 15:00, 10:30 - 17:00, 08:30 - 15:00, 08:30 - 15:00,8:30 - 15:00', '57.71769887958729','11.923120320486058'],
        ['GeBlod, Frölunda Torg', 'Frölunda torg, Hus A', 'Monday, Tuesday, Wednesday, Thursday, Friday', '7:30 - 15:30, 7:30 - 15:30, 10:30 - 18:30, 10:30 - 18:30, 7:30 - 15:30', '57.652359846794795', '11.913053572634718'],
        ['Lindholmen, Göteborg', 'Lärdomsgatan 5', '20 oct, 21 oct, 30 nov, 1 dec, 2 dec', '08:30 - 14:45, 08:30 - 14:45, 10:30  17:00, 08:30 - 14:45, 08:30 - 14:45', '57.70582762386454', '11.939202227329453'],
        ['GeBlod, Nordstan', 'Götgatan 16', 'Monday, Tuesday, Wednesday, Thursday, Friday', '7:30 - 18:30, 7:30 - 18:30, 7:30 - 18:30, 7:30 - 15:30, 9:30 - 15:00', '57.70800179359', '11.971467743766858' ],
        ['Ullevi, Göteborg', 'Ullevigatan/Skånegatan', '6 oct, 7 oct, 29 dec, 30 dec', '8:30 - 15:00, 8:15 - 15:00, 8:15 - 15:00, 8:15 - 15:00', '57.70776401591029', '11.985174337462219'],
        ['Götaplatsen, Göteborg', 'Götaplatsen', '-', '-', '57.69778390143244','11.978846907317626'],
        ['Chalmers, Göteborg', 'Chalmersplatsen', '9 nov', '8:30 - 15:00', '57.69004078962891', '11.973920991423189'],
        ['Sahlgrenska sjukhuset, Göteborg', 'Blå stråket 10', '12 oct, 13 oct, 14 oct', '8:00 - 15:00, 10:00 - 17:00, 8:00 - 15:00', '57.68298024337626', '11.964659505667566'],
        ['SKF Kristinedal, Göteborg', 'Byfogdegatan 4', '10 nov, 11 nov', '08:15 - 15:00, 08:15 - 15:00', '57.727557895346735', '12.011201675011469'],
        ['Kallebäcks Teknikpark, Göteborg','Solhusgatan 10', '17 nov, 18 nov', '08:15 - 15:00, 08:15 - 15:00', '57.675886078390924', '12.022765081828862'],
        ['Kulturhuset Möllan, Mölndal', 'Göteborgsvägen 19', '19 sept, 20 sept, 12 dec, 13 dec', '08:15 - 15:00, 08:15 - 15:00, 08:15 - 15:00, 08:15 - 15:00', '57.658468975926915', '12.016935035789865'],
        ['Bilprovningen, Mölndal', 'Argongatan 2', '15 sept, 16 sept, 8 dec, 9 dec', '08:15 - 15:00, 08:15 - 15:00, 08:15 - 15:00, 08:15 - 15:00', '57.642349315298645', '12.021205249481719'],
        ['Östra sjukhuset, Göteborg', 'Diagnosvägen 11', '27 oct, 28 oct', '10:30 - 17:00, 11:00 - 15:00', '57.72244192857445', '12.051274205146331'],
        ['Centrum, Partille', 'Gamla Kronvägen 9', '10 oct, 11 oct', '12:15 - 18:15, 12:15 - 18:15', '57.739683559462335', '12.106491905157677'],
        ['Kulturhuset, Mölnlycke', 'Biblioteksgatan 2', '26 sept, 27 sept, 28 sept, 19 dec, 20 dec, 21 dec', '11:30 - 18:00, 11:45 - 18:00, 8:30 - 15:00, 11:30 - 18:00, 11:45 - 18:00, 8:30 - 15:00', '57.658796454334784', '12.119747089762454'],
        ['Hulan, Lerum', 'Hulans Torg 1', '21 nov, 22 nov, 23 nov', '12:30 - 18:00, 12:30 - 18:00, 12:30 - 18:00', '57.75126419151909', '12.246686867082373'],
        ]
df = df.append(data) 
df.columns = ['Place', 'Street', 'Day', 'Time', 'Latitude', 'Longitude']

df