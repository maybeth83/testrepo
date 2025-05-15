import random


class CuentaCorreo:

    def __init__(self, name="NULL", lastName="NULL", year="NULL"):
        self.__name = name
        self.__lastName = lastName
        self.__year = year
        self.__password = self.generatePass()
        self.__mail = self.generateMail()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, value):
        self.__lastName = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, value):
        self.__mail = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def generatePass(self):
        return ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))

    def generateMail(self):
        return self.name+"."+self.lastName+self.year+"@mysoft.com"

    def imprimir(self):
        print("\nNombre: ", self.name)
        print("Apellido: ", self.lastName)
        print("Año de nacimiento: ", self.year)
        print("Correo: ", self.mail)
        print("Contraseña: ", self.password)
