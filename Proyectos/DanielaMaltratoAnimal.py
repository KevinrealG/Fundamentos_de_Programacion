import random
from os import system
("cls")

prevencion = ["Aprende a reconocer el maltrato", "Denuncia", "Conoce las leyes", "Apoya organizaciones", "Educa a los niños", "Da un buen ejemplo", "No compres, adopta"]

while True:
    while True:
        print("***********************************************************************************")
        try:
            opcion = int(input("1/ Información sobre el maltrato en Cartagena \n2/ Prevención \n3/ Juego \n4/ Salir \nSeleccione una opción: "))
            break
        except ValueError:
            print("Error, ingrese un número")
        finally:
            print("***********************************************************************************")
    
    if opcion == 1:
        while True:
            while True:
                print("***********************************************************************************")
                try:
                    info = int(input("1/ Definición de maltrato \n2/ Maltrato en Cartagena \n3/ Acciones grubernamentales  \nSeleccione que información desea: "))
                    break
                except ValueError:
                    print("Error, ingrese un número")
                finally:
                    print("***********************************************************************************")
                    
            if info == 1:
                print("El maltrato animal es una conducta inadecuada en contra de los animales y que puede implicar el sufrimiento, estrés excesivo o la muerte de estos. Existen muchos tipos de maktrato animal, pero los más comunes son: \nAbandono \nsobreexplotación \nmaltrato físico \nmaltrato emociona \nnegligencia")
                break
            elif info == 2:
                while True:
                    while True:
                        print("***********************************************************************************")
                        try:
                            infoCartagena = int(input("1/ Maltrato en general en Cartagena \n2/ Por localidades  \nSeleccione la información que desea conocer del maltaro en Cartagena: "))
                            break
                        except ValueError:
                            print("Error, ingrese un número")
                        finally:
                            print("***********************************************************************************")
                        
                    if infoCartagena == 1:
                        print("En Cartagena aproximadamente entre el 30% y el 40% de los animales sufren algún tipo de maltrato como la negligencia, la sobreexplotación, el abandono y el maltrato físico. En esta ciudad el maltrato se da principalmente en los perros, gatos y caballos, pero sin olvidar que los animales silvestres también sufren estas condiciones.")
                        break
                    elif infoCartagena == 2:
                        while True:
                            print("***********************************************************************************")
                            try:
                                localidades = int(input("1/ Localidad 1 \n2/ Localidad 2 \n3/ Localidad 3 \nSeleccione la localidad de la cual desea conocer información: "))
                                break
                            except ValueError:
                                print("Error, ingrese un número")
                            finally:
                                print("***********************************************************************************")
                                    
                        if localidades == 1:
                            print("La localidad 1 cuenta con barrios como Bocagrande, Manga y el centro, lo cual hace que esta sea el sector turístico de la ciudad se ve menos este tipo de actos con un aproximado del 23% del maltrato en la ciudad, pero en los últimos años se ha visto un aumento el maltrato a los caballos, ya que estos son usados para el entretenimiento y traslado de los visitantes y una parte de los ciudadanos de la ciudad.")
                            break
                        elif localidades == 2:
                            print("Esta localidad cuenta con barrios como el Pozón, los Alpes y Chiquinquirá, en el cual abandono y el maltrato a los perros y gatos es muy común, al igual que la utilización de animales como caballos y burros para transportarse y hacer trabajos pesados, por lo cual en esta zona se encuentra el mayor índice de esta problemática con un aproximado del 55% del maltrato en la ciudad.")
                            break
                        elif localidades == 3:
                            print("Esta localidad cuenta con barrios como el Recreo, Ceballos y Vista Hermosa, en esta se encuentran los índices de maltrato más básicos con un aproximado del 22% del maltrato en la ciudad. En ese sector las personas suelen cuidar más a sus mascotas, por lo cual es nivel de maltrato no es nulo, pero si es más compensado.")
                            break
                        else:
                            print("Error, opción inexistente")
                            
                break
            elif info == 3:
                while True:
                    while True:
                        print("***********************************************************************************")
                        try:
                            acciones = int(input("1/ Ley de protección a nivel nacional \n2/ Estrategia de prevención en Cartagena  \nSeleccione la medida que desea conocer: "))
                            break
                        except ValueError:
                            print("Error, ingrese un número")
                        finally:
                            print("***********************************************************************************")
                        
                    if acciones == 1:
                        print("En Colombia existe la ley 1774 del 6 de Enero de 2016, la cual establece que los actos dañinos y de crueldad contra los animales que no causen la muerte o lesiones que afecten de manera grave su salud o integridad física serán sancionados con multas de 5 a 50 salarios mínimos legales mensuales vigentes. Tambien establece que si le provoca la muerte, podrían estar en prisión de 12 a 36 meses y una inhabilidad de estar en cualquier cargo profesional que implique el contacto con animales")
                        break
                    elif acciones == 2:
                        print("En Cartagena esta la Red de Protección Animal es una estrategia de participación ciudadana liderada por la Unidad Municipal de Asistencia Técnica Agropecuaria (Umata), la cual tiene como objetivo contribuir a la articulación de la acción institucional, sensibilizar y generar conciencia sobre la problemática del maltrato animal. Este proyecto tiene como función: \nDefender los derechos de los animales. \nApoyar campañas educativas contra el maltrato animal. \nPromover la adopción responsable. \nVelar por el bienestar y protección de los animales. \nDenunciar ante las autoridades competentes los presuntos casos de maltrato animal. \nSer gestores de la tenencia responsable de animales de compañía.")
                        break
                    else:
                        print("Error, opción inexistente")
                break
            else:
                print("Error, opción inexistente")
    elif opcion == 2:
        print("Para prevenir el maltrato animal puede: " + random.choice(prevencion))
    elif opcion == 3:
        while True:
            while True:
                print("***********************************************************************************")
                try:
                    juego = int(input("1/ Preguntas \n2/ Completar la frase \nSeleccione un juego: "))
                    break
                except ValueError:
                    print("Error, ingrese un número")
                finally:
                    print("***********************************************************************************")

            if juego == 1:
                correctas = 0
                incorrectas = 0
                
                print("Lea el enunciado y elija la opción correcta")
                
                while True:
                    print("***********************************************************************************")
                    try:
                        p1 = int(input("Pregunta #1 \n¿Qué se hace si presencia un acto de maltrato animal? \n1/ Ignorar \n2/ Unirme al maltrato \n3/ Denunciar \n"))
                    except ValueError:
                        print("Error, ingrese un número")
                    finally:
                        print("***********************************************************************************")

                    if p1 == 1:
                        print("Respuesta incorrecta. \nLa respuesta es incorrecta porque el ignorar un acto de maltrato animal te hace complice de este, ademas de que con este tipo de acciones no se acaba este acto atroz")
                        incorrectas += 1
                        break
                    
                    elif p1 == 2:
                        print("Respuesta incorrecta. \nLa respuesta es incorrecta porque unirse a este tipo de actos de convierte de manera inmediata en agresor, por lo cual el maltrato acaba y lo fomentas, sin olvidar que las autoridades te pueden multar tambien")
                        incorrectas += 1
                        break
                    elif p1 == 3:
                        print("Respuesta correcta.")
                        correctas += 1
                        break
                    else:
                        print("Error, opción inexistente")
                
                while True:
                    print("***********************************************************************************")
                    try:
                        p2 = int(input("Pregunta #2 \nSi tengo un perro y tiene cachoros y no los puedo tener conmigo, ¿qué debo hacer? \n1/ Venderlos \n2/ Abandonarlos en la calle \n3/ Darlos en adopción \n"))
                    except ValueError:
                        print("Error, opción inexistente")
                    finally:
                        print("***********************************************************************************")
                        
                    if p2 == 1:
                        print("Respuesta incorrecta. \nLa respuesta es incorrecta porque la venta de animales es la aceptar que una vida tiene precio, por lo cual toda persona que tiene el dinero puede hacerlo")
                        incorrectas += 1
                        break
                    elif p2 == 2:
                        print("Respuesta incorrecta. \nLa respuesta es incorrecta porque el abandono entra en una de las formas del maltrato")
                        incorrectas += 1
                        break
                    elif p2 == 3:
                        print("Respuesta correcta.")
                        correctas += 1
                        break
                    else:
                        print("Error, opción inexistente")
                        
                while True:
                    print("***********************************************************************************")
                    try:
                        p3 = int(input("Pregunta #3 \n¿Qué comportamientos pueden mostrar que un animal sufre de maltrato? \n1/ Miedo y desconfianza \n2/ Emoción al ver a una persona \n3/ Ganas constantes de jugar \n"))
                    except ValueError:
                        print("Error, opción inexistente")
                    finally:
                        print("***********************************************************************************")
                        
                    if p3 == 1:
                        print("Respuesta correcta.")
                        correctas += 1
                        break
                    elif p3 == 2:
                        print("Respuesta incorrecta \nLa respuesta es incorrecta porque la emoción por una persona es algo que solo se gana si esta trata bien al animal")
                        incorrectas += 1
                        break
                    elif p3 == 3:
                        print("Respuesta incorrecta \nLa respuesta es incorrecta porque al sufrir maltrato el animal sufre de ansiedad y miedo por persona como por animales")
                        incorrectas += 1
                        break
                    else:
                        print("Error, opción inexistente")
                
                print("Usted obtuvo",correctas,"preguntas correctas, y",incorrectas,"preguntas incorrectas")
                break
            
            elif juego == 2:
                correctasj2 = 0
                incorrectasj2 = 0
                
                print("Seleccione una opción para completar la frase")
                
                while True:
                    print("***********************************************************************************")
                    try:
                        f1 = int(input("Frase #1 \nLos __________ son seres realmente extraordinarios, que nos enseñan innumerables valores y el verdadero significado del respeto. \n1/ Animales \n2/ Humanos \n3/ Hombres \n"))
                    except ValueError:
                        print("Error, opción inexistente")
                    finally:
                        print("***********************************************************************************")
                    
                    if f1 == 1:
                        correctasj2 += 1
                        break
                    elif f1 == 2:
                        incorrectasj2 += 1
                        break
                    elif f1 == 3:
                        incorrectasj2 += 1
                        break
                    else:
                        print("Error, opción inexistente")
                        
                while True:
                    print("***********************************************************************************")
                    try:
                        f2 = int(input("Frase #2 \nCreo que los animales tienen derecho a que no les infligimos dolor, __________ o privación física. \n1/ Temor \n2/ Alegria \n3/ Atención \n"))
                    except ValueError:
                        print("Error, opción inexistente")
                    finally:
                        print("***********************************************************************************")
                        
                    if f2 == 1:
                        correctasj2 += 1
                        break
                    elif f2 == 2:
                        incorrectasj2 += 1
                        break
                    elif f2 == 3:
                        incorrectasj2 += 1
                        break
                    else:
                        print("Error, opción inexistente")
                
                while True:
                    print("***********************************************************************************")
                    try:
                        f3 = int(input("Frase #2 \nLa crueldad con los animales es lo opuesto al deber que el hombre con los animales que es la __________. \n1/ Felicidad \n2/ Crueldad \n3/ Protección \n"))
                    except ValueError:
                        print("Error, opción inexistente")
                    finally:
                        print("***********************************************************************************")
                    
                    if f3 == 1:
                        correctasj2 += 1
                        break
                    elif f3 == 2:
                        incorrectasj2 += 1
                        break
                    elif f3 == 3:
                        incorrectasj2 += 1
                        break
                    else:
                        print("Error, opción inexistente")
                print("Usted obtuvo",correctasj2,"preguntas correctas, y",incorrectasj2,"preguntas incorrectas")
                break
            else:
                print("Error, opción inexistente")
    elif opcion == 4:
        print("Vuelva pronto!!!")
        break
    else:
        print("Error, opción inexistente")