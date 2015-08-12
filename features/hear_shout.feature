Feature: Hear Shout

  Rules:
  - Listeners within 1km will hear messages
  - All messages are UTF-8 text
  - Max message length is 140 characters

  Questions:
  - Do we really need to know who shouted something?
  - Will I hear my neighbour's message when I come home from work?
  - Will my neighbour's message disappear when I go to work?
  - Do users need to be registered to shout?

  Persona:
  - Sean the shouter
  - Lucy the listener

  Scenario: Lucy hears a message from Sean within range
    Given "Sean" is at "Leicester Square Station"
    And "Lucy" is at "Piccadilly Circus Station"
    When "Sean" shouts "hello"
    Then "Lucy" hears "hello"

  Scenario: Lucy does not hear a message from Sean outside range
    Given "Sean" is at "Leicester Square Station"
    And "Lucy" is at "Heathrow Terminal 5"
    When "Sean" shouts a message
    Then "Lucy" does not hear anything
