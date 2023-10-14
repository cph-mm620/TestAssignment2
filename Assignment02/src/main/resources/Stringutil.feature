Feature: String Utility

  Scenario: Reverse string
    Given a string "aBc"
    When I reverse the string
    Then the result should be "cBa"

  Scenario: Capitalize string
    Given a string "aBc"
    When I capitalize the string
    Then the result should be "ABC"

  Scenario: Lowercase string
    Given a string "aBc"
    When I lowercase the string
    Then the result should be "abc"