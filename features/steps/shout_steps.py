from nose.tools import assert_equals

@given(u'"{person_name}" is at "{location_name}"')
def person_is_at(context, person_name, location_name):
    geo_location = [1,2]
    context.automation.person_is_at(person_name, geo_location)

@when(u'"{person_name}" shouts "{message}"')
def person_shouts(context, person_name, message):
    context.automation.person_shouts(person_name, message)

@then(u'"{person_name}" should not hear anything')
def person_should_hear_nothing(context, person_name):
    heard = context.automation.messages_heard_by(person_name)
    assert_equals([], heard)

@then(u'"{person_name}" should hear "{expected_message}"')
def person_should_hear(context, person_name, expected_message):
    heard = context.automation.messages_heard_by(person_name)
    assert_equals([expected_message], heard)
