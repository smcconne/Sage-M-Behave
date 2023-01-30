Feature: Login tests
	
	@register
	Scenario: I register the standard user
		Given I close the welcome banner
		When I navigate to the registration page
		Then the registration page has loaded
		When I register as standard user
		Then the login page has loaded
		When I log in as standard user
		Then I should be logged in
	
	Scenario: I can log in as the standard user
		Given I close the welcome banner
		When I navigate to the login page
		Then the login page has loaded
		When I log in as standard user
		Then I should be logged in