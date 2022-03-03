"""
    Make a dictionary called cities. Use the names of three cities as 
    keys in your dictionary. Create a dictionary of information about each city 
    and include the country that the city is in, its approximate population, and
    one fact about that city. The keys for each city’s dictionary should be 
    something like country, population, and fact. Print the name of each city
    and all of the information you have stored about it.
"""

cities = {
    'madrid': {
        'country': "espania",
        'population': "3.223 millones",
        'fact': """
            Madrid es una ciudad que sabe vivir. Es una ciudad que ofrece una 
            arquitectura asombrosa, galerías de clase mundial, mucha historia, 
            comida increíble y una vida nocturna épica. Si te gustan todas estas 
            cosas mencionadas, sin duda te enamorarás de Madrid.
            """,
        },
    'tokio': {
        'country': "japon",
        'population': "13.96 millones",
        'fact': """
            1 of 10 Tokyo is the world's most populous metropolitan area.
            2 of 10 The Cherry Blossom is the unofficial national flower.
            3 of 10 Tokyo was originally named Edo.
            4 of 10 Tokyo first held the Olympics in 1964.
            5 of 10 Shinjuku Station is the busiest train station in the world.
            """,
        },
    'guayaquil': {
        'country': "ecuador",
        'population': "2.698 millones",
        'fact': """
            En general, solo hay dos estaciones en Ecuador: seca y húmeda.
            La estación seca (junio-septiembre) se considera invierno. 
            Esta época del año es más seca y fresca que la temporada de lluvias. 
            La temporada de lluvias (octubre-mayo) se considera verano. 
            Esta época del año es ligeramente más cálida con más precipitaciones 
            (lluvias) que la estación seca.""",
        },
    }

for name_city, details in cities.items():
    print("\nCaracteristicas de la ciudad de " + name_city.title())
    for type_data, data in details.items():
        td = "pais de origen" if type_data == 'country' else 'hecho' if type_data == 'fact' else 'nivel de poblacion'
        print("\t", td.title())
        print("\t\t", data.title())
