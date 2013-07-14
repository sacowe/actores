#!/usr/bin/python
# -*- coding: utf-8 -*-
#Info para main_database.db
import datetime

actores = [["Jennifer Lawrence", datetime.date(1990,8,15), "Femenino", "images/1.jpg"],
		   ["Leonardo DiCaprio", datetime.date(1974,11,11), "Masculino", "images/2.jpg"],
		   ["Bruce Willis", datetime.date(1955,3,19),"Masculino","images/3.jpg"],
		   ["Joseph Gordon-Levitt", datetime.date(1981,2,17), "Masculino", "images/4.jpg"],
		   ["Ellen Page", datetime.date(1987,2,21), "Femenino", "images/5.jpg"],
		   ["Zooey Deschanel", datetime.date(1980, 1, 17), "Femenino", "images/6.jpg"],
		   ["Emma Thompson", datetime.date(1959, 4, 15), "Femenino", "images/7.jpg"],
		   ["Milla Jovovich", datetime.date(1975,12,17), "Femenino", "images/8.jpg"]]

peliculas = [["The Hunger Games", datetime.date(2012,3,23), "Gary Cross", "Katniss Everdeen voluntariamente toma el lugar de su hermana en los Juegos del Hambre, una pelea a la muerte televizada donde dos adolescentes de cada uno de los doce distritos de Panem son escogidos al azar para competir."],
		     ["Silver Linings Playbook", datetime.date(2013,1,25), "David O.Russell", "Después de un periodo en una clinica psiquiátrica, ex-profesor Pat Solitano vuelve a vivir con sus padres y trata de reconciliarse con su ex-esposa. Las cosas se complican cuando Pat conoce a Tiffany, una chica misteriosa con sus propios problemas."],
		     ["Inception", datetime.date(2010,8,6), "Christopher Nolan", "Un extractor hábil es ofrecido una oportunidad de recuperar su antigua vida como recompensa por una hazaña considerada imposible."],
		     ["Django Unchained", datetime.date(2013,1,18), "Quentin Tarantino", "Con la ayuda de un cazarrecompensas alemán, un esclavo liberado se dirige a rescatar a su esposa de un brutal dueño de una plantación en Mississippi."],
		     ["A Good Day to Die Hard", datetime.date(2013,2,15), "John Moore", "John McClane viaja a Rusia para ayudar a su hijo perdido, Jack, para luego descubrir que Jack es un agente de la CIA trabajando para prevenir un robo de armas nucleares, llevando a padre e hijo a unirse contra las fuerzas del bajo mundo."],
		     ["(500) Days of Summer", datetime.date(2009, 10,23), "Marc Webb", "An offbeat romantic comedy about a woman who doesn't believe true love exists, and the young man who falls for her."],
		     ["Nanny McPhee", datetime.date(2006, 4,7), "Kirk Jones", "Emma Thompson stars as a governess who uses magic to rein in the behavior of seven ne'er-do-well children in her charge."],
		     ["The Fifth Element", datetime.date(1997, 5, 30), "Luc Besson", "In the colorful future, a cab driver unwittingly becomes the central figure in the search for a legendary cosmic weapon to keep Evil and Mr Zorg at bay."],
		     ["Resident Evil: Retribution", datetime.date(2012,10,5), "Paul W.S. Anderson"],
		     ]

relaciones = [[1,1,"Katniss Everdeen","Katniss Everdeen (Jennifer Lawrence) es una joven de 16 años con pelo negro y liso, piel color oliva y ojos café. A ella y su mejor amigo, Gale (Liam Hemsworth), les encanta cazar. La mañana antes de la Cosecha, Gale y Katniss están cazando. La Cosecha llega pronto, y todos están esperando para ser llamados. La hermana menor de Katniss, Primrose (Willow Shields) acaba de cumplir 12 años, asi que su nombre entrará a la Cosecha por primera vez. Effie Trinket (Elizabeth Banks) saca el nombre de Primrose Everdeen! Prim empieza a enloquecer, igual que su hermana. Katniss se ofrece como tributo en reemplazo de su hermana. Por ende, es llevada a la competencia junto con el tributo masculino, Peeta (Josh Hutcherson). Katniss avanza en los juegos, eventualmente se encuentra con Peeta y forman una alianza."],
			  [1,2,"Tiffany","Tiffany es una veinteañera con muchos problemas y una mala niñez, que sabe como atraer hombres, al conocer a un extraño salido de una clinica psiquiatrica decide motivarlo, añadiendolo a sus potenciales admiradores. Pero él es una ayuda en una manera distinta, y ella empieza a desarrollar una atracción cuando el comienza rechazándola, ya que está casado (pero separado). Ella le hace un favor, contra sus propios deseos, y entonces usa ésto como chantaje para pedirle un favor de vuelta: ser su compañero en una competencia de baile. Con rencillas y problemas entre ambos, cada uno aprende a sobrellevarlo en diferentes maneras, y el resultado está en duda hasta el final. Sin embargo, Tiffany ayuda y recibe ayuda de la relación: soluciona bastante su vida y su problema mental."],
			  [2,3,"Cobb","Cobb es un extractor - entra en los sueños de la gente, se roba sus secretos y los vende a sus competidores. Solía tener un trabajo legal que involucraba extracción y compartir sueños, pero ahora es un hombre buscado y debe sustentarse por otros medios. Cobb es buscado por el gobierno por el asesinato de su esposa, Mal, en su aniversario. Él es inocente, pero el gobierno no le cree. Tiene dos hijos, James y Philippa, quienes fue forzado a dejar atrás cuando se fugó. Ellos viven con su abuela en EEUU. Cobb visita al abuelo de los niños en Paris, y les envía regalos a través de él. Todo lo que hace, es para encontrar una forma de volver a casa con sus hijos."],
			  [2,4,"Calvin Candie","Calvin Candie es el francófilo dueño de Candyland, la cuarta plantación mas notoria de todo Mississippi, quien adquirió la esposa de Django, Broomhilda, de una manera cuestionable."],
			  [3,5,"John McClane","John McClane, masculino, irlandés-americano, nacido el 11 de agosto de 1957 en Nueva York, EEUU. McClane trabaja como Teniente en el Departamento de Policía de Nueva York. Está casado con Holly Gennero McClane, de quien se divorció más tarde y con quien tiene dos hijos: John McClane Jr. y Lucy McClane."],
			  [4,3,"Arthur", "Arthur es la mano derecha de Cobb, y aparentemente su amigo más cercano. Se conocen desde la trágica muerte de la esposa de Cobb. Vive en EEUU, pero viaja por el mundo con Cobb. Arthur y Cobb solían trabajar con Eames, pero Artuhr y Eames ya no se llevan bien. Los tres nunca divulgan información sobre sus experiencias pasadas, por lo que no se pueden establecer más hechos al respecto."],
			  [5,3,"Ariadne", "Ariadne es una estudiante de arquitectura en Francia. Conoce a Cobb a través de uno de sus profesores, que es el suegro de Cobb. Después de un par de pruebas, es incorporada al equipo como su Arquitecto oficial. Al inicio ella es adversa a compartir sueños, pero no puede apartarse de la libertad que ello ofrece."],
			  [6,6,"Summer", "No Description"],
			  [4,6,"Tom", "No Description"],
			  [7,7,"Nanny McPhee", "No Description"],
			  [3,8,"Korben Dallas","A post-America taxi driver in New York City with a grand military background simply lives his life day to day, that is, before he meets Leeloo. Leeloo captures his heart soon after crashing into his taxi cab one day after escaping from a government-run laboratory. Korben soon finds himself running from the authorities in order to protect Leeloo, as well as becoming the center of a desperate ploy to save the world from an unknown evil."],
			  [8,8,"Leeloo", "Mondoshawans who was attacked and destroyed with only a hand holding a briefcase handle. Earth used reconstitution device to recreate the rest of the body, whereupon it takes the form of an apparently human woman named Leeloo, described as the perfect being."],
			  [9,8,"Alice", "Alice is an Umbrella security covert operative placed at the mansion to protect the Hive's emergency entrance. Alice is married to Spence Parks, however, their marriage is revealed to be a fake, in order to cover the operation's secrecy."]
			  ]
