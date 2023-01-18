# from nose.tools import assert_equals

from pytest_bdd import scenario, given, when, then,parsers
import pytest


from shouty.api import Api
from shouty.coordinate import Coordinate

ARBITARY_MESSAGE = 'Hello, world'


class Context(object):
    pass

@scenario('../../features/hear_shout.feature', 'In range shout is heard')
def test_in_range_shout():
    pass

@scenario('../../features/hear_shout.feature', 'Out of range shout is not heard')
def test_out_of_range():
    pass

@pytest.fixture
def context():
    ctx = Context()
    ctx.shouty = Api() 
    return ctx


@given(parsers.cfparse('Lucy is at {x:Number}, {y:Number}', extra_types={"Number": int}))
def lucy_at(context, x, y):
    context.shouty.set_location('Lucy', Coordinate(x, y))

@given(parsers.cfparse('Sean is at {x:Number}, {y:Number}', extra_types={"Number": int}))
def sean_at(context, x, y):
    context.shouty.set_location('Sean', Coordinate(x, y))

@when(u'Sean shouts')
def sean_shouts(context):
    context.shouty.shout('Sean', ARBITARY_MESSAGE)

@then(u'Lucy should hear Sean')
def lucy_hears_sean(context):
    assert len(context.shouty.get_shouts_heard_by('Lucy')) == 1

@then(u'Lucy should hear nothing')
def step_impl(context):
    assert len(context.shouty.get_shouts_heard_by('Lucy')) == 0