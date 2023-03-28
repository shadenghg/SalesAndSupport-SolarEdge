Feature: SolarEdge Sales and support staff test cases
  Scenario: Create sales request
    Given Navigate to the website "https://fa-evzi-test-saasfaprod1.fa.ocs.oraclecloud.com/"
    Then Insert in "Username": "QA.001"
    And Insert in "Password": "SeFusionTestOC00#@!@&"
    And Choose "English language" option
    And Click on "Login" button
    And Click on "Home" button
    When "Sales" button is visible
    Then  Click on "Sales" button
    And Click on "Service Request" button
    And  Click on "Create Service Request" button
    And Insert in "Title": "Sales and Support 2023"
    And  Click on "Save and Close" button
    Then Click on "list arrow" button
    And Choose "Open Service Requests Created By Me" option
    And Verify that the Service Request has been created

#  Scenario: Permission to create an appointment
#    And Click on "Home" button
#    When "Sales" button is visible
#    Then  Click on "Sales" button
#    And Click on "Create Appointment" button
#    And Insert in "Subject": "Sales and Support 2023"
#    And  Click on "Save and Close" button
#    And A message is displayed to the user

