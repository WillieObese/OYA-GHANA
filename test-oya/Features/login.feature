Feature: Login

  Scenario: Login Authentication, single paramters
    Given Launch chrome browser
    When Open login page
    And Enter phone "0208033577" and pin "1996"
    And Click on Enter
    Then successful login

Scenario Outline: Login Authentication, Multiple paramters
   Given Launch chrome browser
    When Open login page
    And Enter phone "<phone_number>" and pin "<pin>"
    And Click on Enter
    Then successful login

Examples:
  | phone_number  | pin |
  | 0208033577 | 1996 |
  | 0208033578 | 1997 |

