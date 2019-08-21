from shouty.coordinate import Coordinate
from nose.tools import assert_equals


# Define Coordinate 
def test_should_calculate_distance_from_itself():
    a = Coordinate(0,0)
    assert_equals(a.distance_from(a), 0)

def test_should_calculate_distance_from_another_coordinate_along_x_axis():
    a = Coordinate(0,0)
    b = Coordinate(600,0)
    assert_equals(a.distance_from(b), 600)