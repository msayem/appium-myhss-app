@test @mcg_pss
Feature: MCG Screen - Pre-Surgical Screening
  # Enter feature description here

  @x1
  Scenario: App displays a "PSS" task to remind user to schedule the appointment
    Given a user who is in "PRE_OP_PSS_NOT_SCHEDULED" state
    And a user who is into the MyCareGuide Screen
    Then "ToDoListTab" is selected
    And "PSS" task is displayed in To Do List
    When the user clicks the "TaskButton" from the "PSS" task
    Then it displays the "PSS" Screen
    And text "Call to Schedule Your Pre-surgical Screening Day Visit" is displayed into the "PSSTitle"


  @x2
  Scenario: App displays the "View Itinerary" task when PSS is scheduled
    Given a user who is in "PRE_OP_PSS_SCHEDULED" state
    And a user who is into the MyCareGuide Screen
    Then "ToDoListTab" is selected
    And "Itinerary" task is displayed in To Do List
    When the user clicks the "TaskButton" from the "Itinerary" task
    Then it displays the "Itinerary" Screen
    And text "Pre-Surgical Screening Day" is displayed into the "ItineraryTitle"
