
# Example of tup;es used as records
lax_coordiantes = (33.9425, -118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
traveler_ids = [("USA", '31195855'), ('BRA', "CE342567"), ("ESP", 'XDA205856')]

# For the tuples sorted by first item of tuples
# print tuplewith "/" inbetween
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# This is how I would do it
for country, info in traveler_ids:
    print(country, info, sep="/")

'''ouput of commands:
BRA/CE342567
ESP/XDA205856
USA/31195855
'''

# the "_" serves as a dummy variable
for country, _ in traveler_ids:
    print(country)

'''Output
USA
BRA
ESP
'''

# Unpacking nested tuples
metro_areas = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


#test format
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# assign our format to a variable
fmt = '{:15} | {:9.4f} | {:9.4f}'

# Assing variables according to the structure of var 
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

'''You can use the collections.namedtuple function to produce
 subclasses of tuple enhanced iwth field and class name'''

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo.population
tokyo.coordinates
