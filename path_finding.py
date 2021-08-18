import numpy as np


def make_grid():
    """ The thought here is to take a current position, and to make a grid that includes the next checkpoint we need to hit.
        Then we can apply weights (eventually power gains) to each coordinate, and run a path finding algorithm"""
#    main.get_current_location()
#    coordinates = current_location.coords
    coordinates = (51.523659,-0.158541)
#    height = current_location.height

    # Step is how many degrees to add to each coordinate - 0.015060 is 1km.
    step = 0.015060
    grid =[(coordinates[0] + i*step, coordinates[1] + j*step) for i in range (-20, 21) for j in range (-20, 21)]
    
    
make_grid()