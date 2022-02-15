from pygeocoder import Geocoder

endereco = 'Avenida Paulista, 100 São Paulo'
resultado = Geocoder('AIzaSyAIY0coggbHzTCe5rGF86FLUKXWKw2yPMM').reverse_geocode(-23.5703022, -46.6451267)
print(resultado)