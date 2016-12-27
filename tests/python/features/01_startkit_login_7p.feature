Feature: StartKit login page
  In order to do further actions
  As a user
  I need to login the StartKit

  @complete
  Scenario: Login failed 1 on 7 plus
    Given Setup the environment for "7p"
    And Start the app on "7p"
    When Clear username and password
    And Input the username: "aaaaaa" and password: "aaaaaa"
    And Tap "Login"

  @complete
  Scenario: Login failed 2 on 7 plus
    Given Setup the environment for "7p"
    And Start the app on "7p"
    When Clear username and password
    And Input the username: "bbbbbb" and password: "bbbbb"
    And Tap "Login"
