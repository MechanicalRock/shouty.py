from nose.tools import assert_equals

from shouty.api import Api
from shouty.coordinate import Coordinate

ARBITARY_MESSAGE = 'Hello, world'

@given(u'Lucy is at {x}, {y}')
def step_impl(context, x, y):
    context.shouty.set_location('Lucy', Coordinate(x, y))


@given(u'Sean is at {x}, {y}')
def step_impl(context, x, y):
    context.shouty.set_location('Sean', Coordinate(x,y))


@when(u'Sean shouts')
def step_impl(context):
    context.shouty.shout('Sean', ARBITARY_MESSAGE)

@then(u'Lucy should hear Sean')
def step_impl(context):
    assert len(context.shouty.get_shouts_heard_by('Lucy')) == 1

@then(u'Lucy should hear nothing')
def step_impl(context):
    assert len(context.shouty.get_shouts_heard_by('Lucy')) == 0