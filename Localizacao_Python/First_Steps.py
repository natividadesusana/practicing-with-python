from pygeocoder import Geocoder

endereco = '1222, Lins de Vasconcelos, São Paulo, SP'
print(Geocoder('AIzaSyAIY0coggbHzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco).coordinates)