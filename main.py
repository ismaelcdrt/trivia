#aplicando lo aprendido, hare una trivia similar a la del ejemplo
#tuve problemas creando una libreria asi que no la hare.
#solo le dare unos puntos de inicio de 7, los cuales los almacenare en la variable 'puntosiniciales'
puntosiniciales = 7

#presentacion de mi trivia
print( 'Te doy la bienvenida querido amigo a mi trivia sobre el libro del genesis.' )
print( 'Atraves de esta trivia pondre a prueba tus conocimientos sobre cuanto sabes de lo que cuenta el libro del genesis' )
print( 'Ahora mismo tienes' ,puntosiniciales, 'puntos' )
#antes de empezar con las preguntas le pregunto su nombre para interactuar con el jugador
nameplayer = input('ingresa tu nombre: ')
ageplayer = int(input( 'ingresa tu edad: '))
print('Hola' ,nameplayer, ',el momento ah llegado.')

if ageplayer >= 18:
    print('Valla ,ya eres todo un  muchachon.Es hora de darle con todo.')
else:
    print('Hola amiguito, empecemos')


#pregunta 1
print('1) ¿Cual es el nombre que Dios le dio a Jacob despues de someterlo a El a causa autosuficiencia arrogante?')
print('a)Israel')
print('b)Matusalen')
print('c)Ismael')
print('d)Samuel')

#almacenare su respuesta en una variable llamada 'respuesta1' la cual utilizare tambien para que este no pase a la siguiente pregunta si intenta saltarsela de alguna manera poniendo una respuesta ajena a las que yo establecere
respuesta1 = input('tu respuesta: ')

while respuesta1 not in ('a' , 'b' , 'c' , 'd'):
    respuesta1 = input('Ah si??? ,agil te crees causa ;debes responder a, b, c o d para pasar a la siguiente pregunta.Ingresa nuevamente tu respuesta: ')
#ahora dependiendo de lo que responda el juegador le saldran los repectivos mensajes y se le añadiran y/o agregara cierta cantidad de puntpos.
if respuesta1 == 'a':
    puntosiniciales += 10
    print('Muy bien hecho' ,nameplayer, ',vamos por el siguiente!!?')
else:
    puntosiniciales -= 11
    print('Que pena' ,nameplayer, 'n hay tiempo para lamentos, continuemos.')

print(nameplayer, 'ya llevas' ,puntosiniciales, 'puntos ,NO PARES!!!.')



#pregunta 2
print('2) ¿Con cuantas mujeres el hijo de jacob tuvo sus 12 hijos?')
print('a) 4')
print('b) 2')
print('c) 3')
print('d) 1')

#hacemos lo mismo que en el anterior solo que esta vez seremos versatiles en cuanto a las respuestas que de el jugador dentro de las alternativas que puede estan permitidas.
respuesta2 = input('tu respuesta: ')

while respuesta2 not in ('a' , 'b' , 'c' , 'd'):
    respuesta2 = input('Ah si??? ,agil te crees causa ;debes responder a, b, c o d para pasar a la siguiente pregunta.Ingresa nuevamente tu respuesta: ')

if  respuesta2 == 'b':
    puntosiniciales -= 11
    print('incorrecto!' ,nameplayer)
elif  respuesta2 == 'c':
    puntosiniciales -= 11
    print('uy que mal ,pero estuviste cerca ')
elif respuesta2 == 'd':
    puntosiniciales -= 11
    print('jajaj no era tan santo xD')
else:
    puntosiniciales += 10
    print('muy bien hecho, en resumen; israel tuvo originalmente una mujer pero tras engaños por parte de su tio Laban y porque en poca fructividad y empuje por parte de sus primeras dos esposas ,jacob se vio obligado a tener hijos con potras dos mujeres que eran sirvientas de sus dos primeras esposas.')

print(nameplayer, 'ya llevas' ,puntosiniciales, 'puntos ,sigue asi!!!.')



#Pregunta 3
print('3)¿Antes de llegar con su tio Laban y ser engañado ,que llevo a jacob ir con su tio Laban??')
print('a)Su reveldia para con su padre Isaac.')
print('b)El haver suplantado a su hermano Esau para recibir la bendicion completa de su padre al momento de su muerte.')
print('c)Su espiritu aventurero.')
print('d)El hechp de que ya tenia edad para conseguir mujer y presentarla ante sus padres.')

#hare exactamente lo mismo que hice en el problema anterior solo que ahora jugare con las operaciones aritmeticas
respuesta3 = input('Tu respuesta: ')

while respuesta3 not in ('a' , 'b' , 'c' , 'd'):
    respuesta3 = input('Vamos bro, es la ultima no te rajes debes responder con a, b, c o d.Ingresa tu respuesta: ')

if respuesta3 == 'a':
    puntosiniciales = puntosiniciales / 2
    print('jacon no era revelde con sus Padres.')
elif respuesta3 == 'c':
    puntosiniciales = puntosiniciales + 11 / 3
    print('No puedo asegurar que no le gustara explorar las tierras que le heredaron y las que tendria posteriormente gracias al pacto de Dios con el pero no es la respuesta xD')
elif respuesta3 == 'd':
    puntosiniciales = puntosiniciales - 11
    print('Posteriormente jacob si se casaria con las hijas de Laban pero no fue por eso que fue junto con Laban.')
else:
    puntosiniciales = puntosiniciales * 3
    print('muy bien ;tras haber suplantado a su hermano mayor para recibir la bendicion de su padre isac y con ella tmbn heredar el pacto de DIos que isaac habia heredado de su padre Abraham ,SUS PADRE ISAAC Y SU MADRE LE ORDENARON QUE HUYERA A DONDE SU TIO LABAN PORQUE ESAU QUERIA MATARLO POR LO QUE HABIA HECHO.')

  

print('Gracias por jugar mi trivia' ,nameplayer, 'sos tremendo,llegaste aqui con' ,puntosiniciales, 'puntos')
if puntosiniciales >= 20:
    print('sos mas pro todavia entonces awueo')
else:
    print('wueno ,ya habra una proxima.')