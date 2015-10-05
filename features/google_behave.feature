Feature: testing google

  Scenario: visit google and search
     When we visit google
     And search for "Behave"
     Then it should have a title "Behave"
