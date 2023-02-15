import math
kb = {
        'na2co3':1.659586e-4, # from wikipedia, where they say pka = 10.22
}
ph = lambda c: 14 + 0.5 * math.log(kb['na2co3'] * c,10)
