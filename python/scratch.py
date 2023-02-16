import math

def pka_to_kb(pka):
    """
    wikipedia provides pka, but we want kb for our calculations
    convert pka to kb
    """
    return 10 ** (pka - 14)

def pH(c, kb = 2.1*10**-4):
    return 14 + 0.5 * math.log(kb * c,10)

def wt_percent_to_molarity(wt_percent):
    """
    because 1 wt% = 10g/L, return wt% * 10/molar_mass_na2co3
    input: wt_percent without the % sign. 1, 5, 10, etc. As opposed to 0.01, 0.05, 0.10, etc.
    """
    if type(wt_percent) == list:
        return [wt_percent_to_molarity(x) for x in wt_percent]
    return wt_percent * (10 / 105.99)


# according to pubchem, pH of solution at 25degC is as follows:

molarities = wt_percent_to_molarity([1, 5, 10])
pH_experimental = [11.37, 11.58, 11.70]
pH_aquion = [11.26, 11.38, 11.42]

def mse_error(vec, truth=pH_experimental):
    diffs_squared = []
    for i in range(len(vec)):
        diffs_squared.append((vec[i] - truth[i])**2)
    return sum(diffs_squared) ** 0.5

pH_stackexchange = lambda c0: pH(c0, 2.1 * 10 ** -4)
pH_wikipedia = lambda c0: pH(c0,pka_to_kb(10.22))
pH_vanderbilt = lambda c0: pH(c0,pka_to_kb(6.37))

print(molarities)
print(pH_experimental,mse_error(pH_experimental))
print(pH_aquion,mse_error(pH_aquion))
ph = [pH_stackexchange(c0) for c0 in molarities]; print(ph, mse_error(ph));
ph = [pH_wikipedia(c0) for c0 in molarities]; print(ph, mse_error(ph));
ph = [pH_vanderbilt(c0) for c0 in molarities]; print(ph, mse_error(ph));
