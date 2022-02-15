# --> MÉTODO 1
#import pygeocoder

#endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
#print(pygeocoder.Geocoder('AIzaSyD_nqcLnfL00Ea_DTFAqIZV1WmzK829Wrg').geocode(endereco).coordinates)

# --> MÉTODO 2
#from geopy.geocoders import Nominatim

#locator = Nominatim(user_agent="myGeocoder")
#location = locator.geocode("Parque Nacional da Tijuca - Alto da Boa Vist, Rio de Janieor - RJ")
#print(location)

# --MÉTODO 3
from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
resultado = Geocoder('AIzaSyD_nqcLnfL00Ea_DTFAqIZV1WmzK829Wrg').geocode(endereco) # ---------------------> endereço
#resultado = Geocoder('AIzaSyD_nqcLnfL00Ea_DTFAqIZV1WmzK829Wrg').geocode(endereco).state # ---------------> estado
#resultado = Geocoder('AIzaSyD_nqcLnfL00Ea_DTFAqIZV1WmzK829Wrg').geocode(endereco).postal_code # ---------> cep
#resultado = Geocoder('AIzaSyD_nqcLnfL00Ea_DTFAqIZV1WmzK829Wrg').geocode(endereco).postal_country # ------> pais
#resultado = Geocoder('AIzaSyD_nqcLnfL00Ea_DTFAqIZV1WmzK829Wrg').geocode(endereco).postal_coordinates # --> coordenadas (latitude e longitude)
#resultado = Geocoder('AIzaSyD_nqcLnfL00Ea_DTFAqIZV1WmzK829Wrg').reverse_geocode(-23.5703022, -46.6451267) # --> encontrar eendereço a partir da latitude e longitude
print(resultado)