import math
kb = {
        'na2co3':1.659586e-4, # from wikipedia, where they say pka = 10.22
}
kbn = kb['na2co3']
ph = lambda c: 14 + 0.5 * math.log(kb['na2co3'] * c,10)

ph_from_mass = lambda m,V: 14 + 0.5 * math.log(kbn * m / (105.99 * V),10)

v0 = 3 #liters
m = lambda pH: 10 ** (2 * (pH - 14) - math.log(kb['na2co3']/(105.99 * v0),10))
m1 = lambda pH: 10 ** (2 * (pH - 14)) * 105.99 * v0 / kbn
