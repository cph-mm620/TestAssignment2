Feature: Bowling Game

  Scenario: Perfect game
    Given there is a game to join
    When only strikes are made
    Then the result should be 300

  Scenario: Gutter game
    Given there is a game to join
    When no pins are knocked down
    Then the result should be 0

  Scenario: All spares
    Given there is a game to join
    When only spares are made
    Then the result should be 150

  Scenario: Mixed strikes and spares
    Given there is a game to join
    When a combination of strikes and spares are made
    Then the result should be the calculated total

  Scenario: Random game
    Given there is a game to join
    When a random sequence of rolls are made
    Then the result should be the calculated total

  Scenario: 7 strikes and 3 open frames
    Given there is a game to join
    When 7 strikes and 3 open frames are made
    Then the result should be the calculated total