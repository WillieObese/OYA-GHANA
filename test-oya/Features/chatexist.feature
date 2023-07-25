Feature: Chat Feature

  Scenario: Check if chat feature exist
    Given Launch chrome browser
    When Go to homepage
    And open chat
    Then check if chat opens
