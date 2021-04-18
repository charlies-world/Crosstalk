from Crosstalk import Crosstalk
from Parameters import Parameters

p = Parameters()
#set parameters

ct = Crosstalk()
ct.set_parameters(p)
ct.perform()