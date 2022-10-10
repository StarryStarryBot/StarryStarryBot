import csv
from astropy import units as u
from astropy.coordinates import SkyCoord

class NightSky:
    def __init__(self):
        self.db = None
        self.load_db()
    
    def load_db(self):
        with open('hygdata_v3.csv', newline='') as reader:
            self.db = [{k: v for k, v in row.items()} for row in csv.DictReader(reader, skipinitialspace=True)]
    
    def find_star(self, id):
        for star in self.db:
            if star["proper"] == id:
                return star

mySky = NightSky()
print(mySky.find_star("Rigel"))
        

