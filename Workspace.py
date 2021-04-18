from Crosstalk import Crosstalk
from Parameters import Parameters

p = Parameters()
p.set_directory_for_files("C:\\Users\\ewatts3\\Documents\\ImaginaryLandscape\\Audio\\Bass Communion II")
#set parameters

ct = Crosstalk()
ct.set_parameters(p)
ct.perform()
