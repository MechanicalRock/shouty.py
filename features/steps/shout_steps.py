from nose.tools import assert_equals

geo_locations = {
    "Leicester Square Station":  [51.5114242, -0.1287315],
    "Piccadilly Circus Station": [51.5101210, -0.1341683],
    "Heathrow Terminal 5":       [51.4715066, -0.4879044]
}
# @given(u'"I have {count}" cukes in my belly"')
# def i_have_some_cukes(context, count):
#     context.automation.cukes_in_the_belly(count)

@given(u'"{person_name}" is at "{location_name}"')
def step_impl(context, person_name, location_name):
    pass

@when(u'Sean shouts a message')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Sean shouts a message')

@then(u'Lucy does not receive the message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Lucy does not receive the message')
