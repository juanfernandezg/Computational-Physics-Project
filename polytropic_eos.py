# polytopic_eos.py contains function that returns the value of the specific internal energy of a polytopic fluid
# outlined as e = P / (y - 1)*rho , where P is some constant, y is the polytopic constant

# return specific energy from pressure p , density rho and gamma constant
def sp_energy_eos(p, rho, gamma):
    return p / ( (gamma - 1)*rho ) 

### may want to add more EoS in the future