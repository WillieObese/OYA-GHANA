Feature: Register

 Scenario Outline: Registration new user
  Given Launch chrome browser
  When Open register page
  And Enter firstname "William" and lastname "Obese"
  And Select Ghana
  And Enter Phone number
  And Enter PIN
  And Click on Enter
  Then Enter first "<first>" and second "<second>"
  Then Click on Submit
  Then Redirection to Login page

  Examples:
  | first | second |
  |    0208033577   |  0208033577      |
  |    0508038271   | 0277718147       |

