Feature: testing google

  Scenario: visit google and search
     When we visit google
     And search for "Selenium"
     Then it should have a title "Selenium"
