from cotxe import Cotxe
from rectangle import Rectangle
from estudiant import Estudiant
from comptebancari import CompteBancari
from producte import Producte 
from punt import Punt
from animal import Animal
from llibre import Llibre
from cercle import Cercle
from persona import Persona

#1. Crea dos cotxes amb la classe Cotxe i imprimeix-ne la informació.

cotxe1 = Cotxe("Toyota", "Corolla", 2020)
cotxe2 = Cotxe("Honda", "Civic", 2019)
cotxe2.mostrar_info()
cotxe1.mostrar_info()

#2. Crea 3 rectangles amb diferents mides. Mostra l’àrea de cadascun.

rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 4)    
rectangle3 = Rectangle(6, 7)
area1 = rectangle1.area()
perimetre1 = rectangle1.perimetre() 
area2 = rectangle2.area()
perimetre2 = rectangle2.perimetre() 
area3 = rectangle3.area()
perimetre3 = rectangle3.perimetre()

#3. Crea una llista d’estudiants. Mostra només els que han aprovat.

estudiant1 = Estudiant("Alice", 8.5)
estudiant2 = Estudiant("Bob", 4.0)  
estudiant3 = Estudiant("Charlie", 6.0)  
estudiant1.ha_aprovat()
estudiant2.ha_aprovat() 
estudiant3.ha_aprovat()

#4. Crea un compte bancari i simula 3 operacions: ingrés, retirada vàlida i retirada superior al saldo.

compte1 = CompteBancari(100)
compte1.ingressar(50)   
compte1.retirar(30)  
compte1.retirar(170)
saldo_final = compte1.veure_saldo() 

#5. Fes una funció que rebi una llista de productes i apliqui un descompte del 10% a tots.

producte1 = Producte("Portàtil", 1000)
nou_preu1 = producte1.aplicar_descompte(10) 
producte2 = Producte("Telèfon", 500)
nou_preu2 = producte2.aplicar_descompte(10)
producte3 = Producte("Tauleta", 300)
nou_preu3 = producte3.aplicar_descompte(10)

#6. Crea dos punts i calcula la distància entre ells.

punt1 = Punt(2, 3)
punt2 = Punt(5, 7)  
distancia = punt1.calcular_distancia(punt2) 

#7. Crea una classe Gos que hereti d’Animal i sobreescrigui fer_soroll() per dir “Bup bup!”.

animal1 = Animal("Rex", "Gos")
animal1.fer_soroll()
 
#8. Fes una classe Biblioteca que pugui afegir llibres (objectes Llibre) i mostrar-los tots.

llibre1 = Llibre("El Quixot", "Cervantes", 1605)
llibre1.mostrar_info()  

# Crea un llistat de cercles i mostra quins tenen àrea superior a 50.

cercle1 = Cercle(4)
cercle2 = Cercle(3) 
cercle3 = Cercle(5)
area1 = cercle1.calcular_area() 
area2 = cercle2.calcular_area() 
area3 = cercle3.calcular_area() 

#10. Fes una funció que rebi una llista de persones i imprimeixi només les que tenen més de 30 anys.

persona1 = Persona("Anna", 25)
persona2 = Persona("Bernat", 35)    
persona3 = Persona("Carla", 40)
if persona1.edat > 30:
    persona1.presentar_se()
if persona2.edat > 30:
    persona2.presentar_se() 
if persona3.edat > 30:
    persona3.presentar_se() 




