from Crosstalk import Crosstalk
from Parameters import Parameters

p = Parameters()
p.set_directory_for_files("C:\\Users\\ewatts3\\Documents\\ImaginaryLandscape\\Audio\\Bass Communion II")
p.set_minimum_length_of_piece(20) #in seconds
p.set_maximum_length_of_piece(30)
p.set_number_of_tracks(5)
p.set_chance_that_next_track_will_play(5)
p.set_minimum_length_of_clip(5)
p.set_maximum_length_of_clip(20)
p.set_minimum_length_between_checks(1)
p.set_maximum_length_between_checks(2)

ct = Crosstalk(p)