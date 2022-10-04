from unittest.util import _MAX_LENGTH
from django.db import models
import pandas as pd
import folium


# All locations where costumer can give blood kept in a DataFrame[].
df = pd.DataFrame()
data = [['Volvo Tuve, Göteborg','Norra Stenebyvägen 5', '19 oct: 8:30 - 15:00', '57.75793077168005', '11.885288966539886', 'bus'],
        ['Hamnnplan, Öckerö','Lammholmsvägen 13' ,'28 nov: 13:30 - 18:00 <br>29 nov: 13:30 - 18:00', '57.70528881808817', '11.657308891433228', 'bus'],
        ['Torslanda, Göteborg', 'Gamla Flygplatsvägen 60', '-', '57.71007251649718', '11.773084736917019', 'bus'],
        ['Arendalsvarvet, Göteborg', 'Arendals Skans 2', '24 nov: 8:30 - 15:00<br>25 nov: 11:00 - 15:00', '57.696924916214165', '11.82092758238937', 'bus'],
        ['Volvo TK, Göteborg', 'Personalvägen 23', '-', '57.71914107962158', '11.845346263780499', 'bus'],
        ['Volvo SA, Göteborg', 'Gustaf Larssons väg 16', '21 sept: 08:30 - 15:00<br>22 sept: 08:30 - 15:00<br>23 sept: 08:30 - 15:00<br>2 nov: 08:30 - 15:00<br>3 nov: 08:30 - 15:00<br>4 nov: 08:30 - 15:00<br>14 dec: 08:30 - 15:00<br>15 dec: 08:30 - 15:00<br>16 dec: 11:00 - 15:00', '57.72667813349899', '11.861120535834463', 'bus'],
        ['Volvo Lundby, Göteborg', 'Gropegårdsgatan 11', '29 sept: 08:30 - 15:00<br>30 sept: 11:00 - 15:00<br>7 nov: 10:30 - 17:00<br>8 nov: 08:30 - 15:00<br>22 dec: 08:30 - 15:00<br>23 dec: 08:30 - 15:00', '57.71769887958729','11.923120320486058', 'bus'],
        ['GeBlod, Frölunda Torg', 'Frölunda torg, Hus A', 'Monday: 7:30 - 15:30<br>Tuesday: 7:30 - 15:30<br>Wednesday: 10:30 - 18:30<br>Thursday: 10:30 - 18:30<br>Friday: 7:30 - 15:30', '57.652359846794795', '11.913053572634718', 'clinic'],
        ['Lindholmen, Göteborg', 'Lärdomsgatan 5', '20 oct: 08:30 - 14:45<br>21 oct: 08:30 - 14:45<br>30 nov: 10:30  17:00<br>1 dec: 08:30 - 14:45<br>2 dec: 08:30 - 14:45', '57.70582762386454', '11.939202227329453', 'bus'],
        ['GeBlod, Nordstan', 'Götgatan 16', 'Monday: 7:30 - 18:30<br>Tuesday: 7:30 - 18:30<br>Wednesday: 7:30 - 18:30<br>Thursday: 7:30 - 15:30<br>Friday:  9:30 - 15:00', '57.70800179359', '11.971467743766858' , 'clinic'],
        ['Ullevi, Göteborg', 'Ullevigatan/Skånegatan', '6 oct: 8:30 - 15:00<br>7 oct: 8:15 - 15:00<br>29 dec: 8:15 - 15:00<br>30 dec: 8:15 - 15:00', '57.70776401591029', '11.985174337462219', 'bus'],
        ['Götaplatsen, Göteborg', 'Götaplatsen', '-', '57.69778390143244','11.978846907317626', 'bus'],
        ['Chalmers, Göteborg', 'Chalmersplatsen', '9 nov: 8:30 - 15:00', '57.69004078962891', '11.973920991423189', 'bus'],
        ['Sahlgrenska sjukhuset, Göteborg', 'Blå stråket 10', '12 oct: 8:00 - 15:00<br>13 oct: 10:00 - 17:00<br>14 oct: 8:00 - 15:00', '57.68298024337626', '11.964659505667566', 'bus'],
        ['SKF Kristinedal, Göteborg', 'Byfogdegatan 4', '10 nov: 08:15 - 15:00<br>11 nov: 08:15 - 15:00', '57.727557895346735', '12.011201675011469', 'bus'],
        ['Kallebäcks Teknikpark, Göteborg','Solhusgatan 10', '17 nov: 08:15 - 15:00<br>18 nov: 08:15 - 15:00', '57.675886078390924', '12.022765081828862', 'bus'],
        ['Kulturhuset Möllan, Mölndal', 'Göteborgsvägen 19', '19 sept: 08:15 - 15:00<br>20 sept: 08:15 - 15:00<br>12 dec: 08:15 - 15:00<br>13 dec: 08:15 - 15:00', '57.658468975926915', '12.016935035789865', 'bus'],
        ['Bilprovningen, Mölndal', 'Argongatan 2', '15 sept: 08:15 - 15:00<br>16 sept: 08:15 - 15:00<br>8 dec: 08:15 - 15:00<br>9 dec: 08:15 - 15:00', '57.642349315298645', '12.021205249481719', 'bus'],
        ['Östra sjukhuset, Göteborg', 'Diagnosvägen 11', '27 oct: 10:30 - 17:00<br>28 oct: 11:00 - 15:00', '57.72244192857445', '12.051274205146331', 'bus'],
        ['Centrum, Partille', 'Gamla Kronvägen 9', '10 oct: 12:15 - 18:15<br>11 oct: 12:15 - 18:15','57.739683559462335', '12.106491905157677', 'bus'],
        ['Kulturhuset, Mölnlycke', 'Biblioteksgatan 2', '26 sept: 11:30 - 18:00<br>27 sept: 11:45 - 18:00<br>28 sept: 8:30 - 15:00<br>19 dec: 11:30 - 18:00<br>20 dec: 11:45 - 18:00<br>21 dec: 8:30 - 15:00', '57.658796454334784', '12.119747089762454', 'bus'],
        ['Hulan, Lerum', 'Hulans Torg 1', '21 nov: 12:30 - 18:00<br>22 nov: 12:30 - 18:00<br>23 nov: 12:30 - 18:00', '57.75126419151909', '12.246686867082373', 'bus'],
        ]
df = df.append(data) 
df.columns = ['Place', 'Street', 'Day and Time', 'Latitude', 'Longitude', 'Clinic or bus']


# Defines attribute and method for the search
class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address