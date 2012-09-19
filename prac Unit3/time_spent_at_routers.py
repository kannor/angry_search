total_time = 75 #ms
one_way_distance = 2500.0 # km
optic_speed = 200000.0 # km/s
ms_per_second = 1000.0

time_on_the_wires = 2*one_way_distance/optic_speed * ms_per_second
print time_on_the_wires 
total_time_at_outers = total_time - time_on_the_wires
print total_time_at_outers
    
