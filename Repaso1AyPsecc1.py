class Rental:
    def __innit__(self, idRental, idVehicle):
        self.idRental = idRental
        self.idVehicle = idVehicle

class Vehicle:
    def __innit__(self, idVehicle, model, brand, category, isAvailable):
        self.idVehicle = idVehicle
        self.model = model
        self.brand = brand
        self.category = category
        self.isAvailable = isAvailable
        isAvailable = True

    def GetVehicleData(self):
        print(f'El id del vehiculo es {self.idVehicle}, el modelo es {self.model}, la marca es {self.brand}, su categoria es {self.category}')

    def CheckAvailability(self):
        if self.isAvailable == True:
            print(f'El carro {self.idVehicle} sí está disponible')
        else:
            print(f'El carro {self.idVehicle} no está disponible')

class Client:
    def __innit__(self, name, idName):
        self.name = name
        self.idName = idName

    def ViewProfila(self):
        print(f'El nombre del cliente es {self.name}, y el ID es {self.idName}')

class StandardClient(Client):
    def __innit__(self, name, idName, licenseType, currRentals):
        super().__innit__(name, idName)
        self.licenseType = licenseType
        self.currRentals = currRentals
        currRentals = []

    def RentalVehicle(idVehicle):
        pass

    def FinishRental(RentalId):
        pass

class CorporateClient(Client):
    def __innit__(self, name, idName, companyName, currLoans):
        super().__innit__(name, idName)
        self.companyName = companyName
        self.currLoans = currLoans
        currLoans = []

    def RentalVehicle(self):
        pass

    def FinishLoan(self):
        pass