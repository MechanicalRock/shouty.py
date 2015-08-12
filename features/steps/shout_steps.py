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
    geo_location = geo_locations[location_name]
    context.automation.person_is_at_geo_location(person_name, geo_location)

@when(u'"{person_name}" shouts a message')
def step_impl(context, person_name):
    context.automation.person_shouts_message(person_name, "baaaa")

@when(u'"{person_name}" shouts "{message}"')
def step_impl(context, person_name, message):
    context.automation.person_shouts_message(person_name, message)

@then(u'"{person_name}" does not hear anything')
def step_impl(context, person_name):
    assert_equals([], context.automation.messages_heard_by(person_name))

@then(u'"{person_name}" hears "{expected_message}"')
def step_impl(context, person_name, expected_message):
    assert_equals([expected_message], context.automation.messages_heard_by(person_name))

@then(u'"{person_name}" should hear')
def step_impl(context, person_name):
    expected_messages = []
    for row in context.table.rows:
        expected_messages.append(row[0])

    assert_equals(expected_messages, context.automation.messages_heard_by(person_name))
