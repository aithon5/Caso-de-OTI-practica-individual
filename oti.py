class Matricula_general ():
    def __init__(self, nombre_estudiante:str, costo_base:float=60.00):
        self.__nombre_estudiante = nombre_estudiante
        self.__costo_base = costo_base
    @property 
    def costo_base(self):
        return self.__costo_base
    
    @property 
    def nombre_estudiante(self):
        return self.__nombre_estudiante

    @costo_base.setter
    def costo_base(self,valor:float):
        if valor != 60.00:
            raise ValueError(f"EL precio de s/.{valor} no es admitido")
        self.__costo_base = valor
    
    def calcular_costo(self):
        return self.costo_base
    
class Matricula_extemporanea(Matricula_general):
    def __init__(self, nombre_estudiante:str, costo_base:float=60.00, 
                recargo_extemporaneo:float=15.00):
        super().__init__( nombre_estudiante, costo_base)
        self.__recargo_extemporaneo = recargo_extemporaneo
    
    @property 
    def recargo_extemporaneo(self):
        return self.__recargo_extemporaneo
    
    def calcular_costo(self):
        return super().calcular_costo() + self.recargo_extemporaneo
    
class Matricula_indice_desaprobatorio(Matricula_general):
    def __init__(self, nombre_estudiante:str, costo_base:float=60.00, 
                recargo_indice_desaprobatorio:float=15.00):
        super().__init__( nombre_estudiante, costo_base)
        self.__recargo_indice_desaprobatorio = recargo_indice_desaprobatorio
    
    @property 
    def recargo_indice_desaprobatorio(self):
        return self.__recargo_indice_desaprobatorio
    
    def calcular_costo(self):
        return super().calcular_costo() + self.recargo_indice_desaprobatorio

class Matricula_beca_violencia(Matricula_general):
    def calcular_costo(self) -> float:
        return super().calcular_costo() * 0.5

estudiante1 = Matricula_extemporanea("Ana", 60.00, 20.00)
estudiante2 = Matricula_indice_desaprobatorio("Luis", 60.00, 10.00)
estudiante3 = Matricula_beca_violencia("sebastian", 60.00)

print(estudiante1.calcular_costo())  
print(estudiante2.calcular_costo()) 
print(estudiante3.calcular_costo()) 

