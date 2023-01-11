class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
moscow = Coordinate(55.76, 37.62)
print(moscow)
location = Coordinate(55.76, 37.62)
print(moscow == location)

print((moscow.lat, moscow.lon) == (location.lat, location.lon))