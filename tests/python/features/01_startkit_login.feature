Feature: StartKit login page
  In order to do further actions
  As a user
  I need to login the StartKit

  @complete
  Scenario: Login failed 1
    Given Setup the environment for "7p"
    And Start the app on "7p"
    When Clear username and password
    And Input the username: "phoebusliang" and password: "aaaaaa"
    And Tap "Login"

  @complete
  Scenario: Login failed 2
    Given Setup the environment for "6sp"
    And Start the app on "6sp"
    When Clear username and password
    And Input the username: "fakeuser" and password: "bbbbbb"
    And Tap "Login"