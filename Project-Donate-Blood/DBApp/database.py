import pandas as pd 

# All locations where costumer can give blood kept in a DataFrame[].
df = pd.DataFrame()
data = [['Volvo Tuve, Göteborg','Norra Stenebyvägen 5', 'Open: 8:30 - 15:00', '57.75793077168005', '11.885288966539886', 'Bus','-'],
        ['Hamnnplan, Öckerö','Lammholmsvägen 13' ,'Open: 13:30 - 18:00', '57.70528881808817', '11.657308891433228', 'Bus','-'],
        ['Torslanda, Göteborg', 'Gamla Flygplatsvägen 60', 'Open: 8:30 - 15:00', '57.71007251649718', '11.773084736917019', 'Bus','-'],
        ['Arendalsvarvet, Göteborg', 'Arendals Skans 2', 'Open: 8:30 - 15:00', '57.696924916214165', '11.82092758238937', 'Bus','-'],
        ['Volvo TK, Göteborg', 'Personalvägen 23', 'Open: 8:30 - 15:00', '57.71914107962158', '11.845346263780499', 'Bus','-'],
        ['Volvo SA, Göteborg', 'Gustaf Larssons väg 16', 'Open: 8:30 - 15:00', '57.72667813349899', '11.861120535834463', 'Bus','-'],
        ['Volvo Lundby, Göteborg', 'Gropegårdsgatan 11', 'Open: 8:30 - 15:00', '57.71769887958729','11.923120320486058', 'Bus','-'],
        ['GeBlod, Frölunda Torg', 'Frölunda torg, Hus A', 'Open: 10:30 - 18:30', '57.652359846794795', '11.913053572634718', 'Clinic','-'],
        ['Lindholmen, Göteborg', 'Lärdomsgatan 5', 'Open: 08:30 - 14:45', '57.70582762386454', '11.939202227329453', 'Bus','-'],
        ['GeBlod, Nordstan', 'Götgatan 16', 'Open: 7:30 - 18:30', '57.70800179359', '11.971467743766858' , 'Clinic','-'],
        ['Ullevi, Göteborg', 'Ullevigatan/Skånegatan', 'Open: 8:30 - 15:00', '57.70776401591029', '11.985174337462219', 'Bus','-'],
        ['Götaplatsen, Göteborg', 'Götaplatsen', 'Open: 8:30 - 15:00', '57.69778390143244','11.978846907317626', 'Bus','-'],
        ['Chalmers, Göteborg', 'Chalmersplatsen', 'Open: 8:30 - 15:00', '57.69004078962891', '11.973920991423189', 'Bus','-'],
        ['Sahlgrenska sjukhuset, Göteborg', 'Blå stråket 10', 'Open: 8:00 - 15:00', '57.68298024337626', '11.964659505667566', 'Bus','-'],
        ['SKF Kristinedal, Göteborg', 'Byfogdegatan 4', 'Open: 8:15 - 15:00', '57.727557895346735', '12.011201675011469', 'Bus'],
        ['Kallebäcks Teknikpark, Göteborg','Solhusgatan 10', 'Open: 08:15 - 15:00', '57.675886078390924', '12.022765081828862', 'Bus','-'],
        ['Kulturhuset Möllan, Mölndal', 'Göteborgsvägen 19', 'Open: 08:15 - 15:00', '57.658468975926915', '12.016935035789865', 'Bus','-'],
        ['Bilprovningen, Mölndal', 'Argongatan 2', 'Open: 08:15 - 15:00', '57.642349315298645', '12.021205249481719', 'Bus','-'],
        ['Östra sjukhuset, Göteborg', 'Diagnosvägen 11', 'Open: 10:30 - 17:00', '57.72244192857445', '12.051274205146331', 'Bus','-'],
        ['Centrum, Partille', 'Gamla Kronvägen 9', 'Open: 12:15 - 18:15','57.739683559462335', '12.106491905157677', 'Bus','-'],
        ['Kulturhuset, Mölnlycke', 'Biblioteksgatan 2', 'Open: 11:30 - 18:00', '57.658796454334784', '12.119747089762454', 'Bus','-'],
        ['Hulan, Lerum', 'Hulans Torg 1', 'Open: 12:30 - 18:00', '57.75126419151909', '12.246686867082373', 'Bus','-'],
        ]
df = df.append(data) 
df.columns = ['Place', 'Street', 'Opening Hours', 'Latitude', 'Longitude', 'Clinic or Bus', 'Distance (km)']