class vehicle:#parent class
    engine_capacity='0HP'
    no_tyres=0
    def set_engine_capacity(self,ec,ty):#ec=engine capacity,ty=no of tyres,self is importent keyword
        self.engine_capacity=ec
        self.no_tyres=ty
class Car(vehicle):#class:car-->code for inheriting
    brand='No Brand'
    def set_brand(self,brand_name):#brand=property
        self.brand=brand_name
    def display_car(self):
        print(self.engine_capacity)#-->inherited from class
        print(self.no_tyres)
        print(self.brand)
maruthi=Car()#maruthi-->object
maruthi.set_engine_capacity('900HP',4)
maruthi.set_brand('Suzuki')
maruthi.display_car()
        