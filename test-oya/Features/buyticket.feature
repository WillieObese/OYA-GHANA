Feature: Buy Ticket

 Scenario: Buy Ticket for a trip
  Given Launch chrome browser
  When Open ticket page
  And Select who you are buying for
  And Enter origin, destination, date, minors
  Then Click on Submit
  Then Proceed to next page