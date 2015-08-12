Feature: Hear Shout

  Rules:
  - Listeners within 1km will hear messages
  - All messages are UTF-8 text
  - Max message length is 140 characters
  - Geo location must be on
  - Messages delievered in chronological order

  Questions:
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

  Scenario: Sean shouldn't hear himself
    When "Sean" shouts a message
    Then "Sean" does not hear anything

  Scenario: Lucy receives messages in chronological order
    Given "Sean" is at "Leicester Square Station"
    Given "Sally" is at "Leicester Square Station"
    And "Lucy" is at "Piccadilly Circus Station"
    When "Sean" shouts "This is Sean"
    And "Sally" shouts "I am Sally"
    Then "Lucy" should hear
      | message      |
      | This is Sean |
      | I am Sally   |
