import pyproj


geod = pyproj.Geod(ellps="WGS84")


class DistSet():
    def __init__(self, data):
        name1 = data[0]["name"]
        lat1 = data[0]["lat"]
        lon1 = data[0]["lon"]
        name2 = data[1]["name"]
        lat2 = data[1]["lat"]
        lon2 = data[1]["lon"]
        self.desc = f"{name1} to {name2}"
        self.bear_to, self.bear_from, self.dist = geod.inv(lon1, lat1, lon2, lat2)
        if self.dist < 800:
            self.code = "1"
        elif self.dist < 1200:
            self.code = "2"
        elif self.dist < 1800:
            self.code = "3"
        else:
            self.code = "4"
        print(self.dist, self.bear_to, self.bear_from, self.code)
