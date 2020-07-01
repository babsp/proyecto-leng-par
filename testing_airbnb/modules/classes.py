class Hosting():
    def __init__(self, name, location, url, category, rooms, superhost, services, nightly_price, total_price, rating, description):
        self.name = name
        self.location = location
        self.url = url
        self.category = category
        self.rooms = rooms
        self.superhost = superhost # clase hija
        self.services = services
        self.nightly_price = nightly_price
        self.total_price = total_price
        self.rating = rating
        self.description = description

    def __str__(self):
        text = (
            "nombre de la oferta: "+self.name
            +"\nlugar: "+self.location
            +"\nurl: "+self.url
            +"\ncategoría: "+self.category
            +"\nhabitaciones: "+str(self.rooms)
            +"\nes superanfitrión: "+str(self.superhost)
            +"\nservicios: "+str(self.services)
            +"\nprecio por noche: "+str(self.nightly_price)
            +"\nprecio total: "+str(self.total_price)
            +"\ncalificación: "+str(self.rating)
            +"\ndescripción: "+self.description
            +"\n"
        )

        return text