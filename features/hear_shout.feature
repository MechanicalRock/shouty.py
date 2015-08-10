Feature: Hear Shout

  Rules:
  - Within 1 km
  - Displayed in chronological order

  Questions:
  - Do users need to be registered?
  - Should we receive own messages?

  Locations:
  - Piccadilly Circus Station: 51.5101210,-0.1341683
  - Leicester Square Station:  51.5114242,-0.1287315
  - Heathrow Terminal 5:       51.4715066,-0.4879044

  @focus
  Scenario: Lucy can't hear Sean
    Given "Sean" is at "Piccadilly Circus Station"
    And "Lucy" is at "Heathrow Terminal 5"
    When "Sean" shouts "hello"
    Then "Lucy" should not hear anything

  Scenario: Lucy can hear Sean
    Given "Sean" is at "Piccadilly Circus Station"
    And "Lucy" is at "Leicester Square Station"
    When "Sean" shouts "hello"
    Then "Lucy" should hear "hello"
