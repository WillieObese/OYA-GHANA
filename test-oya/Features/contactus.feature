Feature: ContactUs

  Scenario: ContactUS Form
    Given Launch chrome browser
    When Navigate to contact us page
    And Phen Enter  fullname "William Obese", second "williamgyau248@gmail.com", phone"0208033577", message "test"
    Then Click Submit
    Then Message Sent