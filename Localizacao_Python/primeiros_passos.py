import pygeocoder

endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(pygeocoder.Geocoder('AIzaSyD_nqcLnfL00Ea_DTFAqIZV1WmzK829Wrg').geocode(endereco).coordinates)

