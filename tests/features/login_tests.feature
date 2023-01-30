Feature: Log in as automation user

	Scenario: I register as random user
		Given I close the welcome banner
		When I navigate to the registration page
		Then the registration page has loaded
		When I register as random user
		Then the login page has loaded
		When I log in as random user
		Then I should be logged in

	Scenario: I can log in as the newly-registered user
		When I navigate to the login page
		Then the login page has loaded
		When I log in as random user
		Then I should be logged in