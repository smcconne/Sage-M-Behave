Feature: Log in as automation user

	Scenario: I log in as standard user
		Given I close the welcome banner
		When I navigate to the login page
		Then the login page has loaded
		When I log in as standard user
		Then I should be logged in