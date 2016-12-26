Feature: StartKit login page
  In order to do further actions
  As a user
  I need to login the StartKit

  @complete
  Scenario: Login successfully
    Given Start the app on "7p"
    When Clear username and password
    And Input the username: "phoebusliang" and password: "111111a"
    And Tap "Login"