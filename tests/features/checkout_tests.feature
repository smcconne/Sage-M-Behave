Feature: Checkout tests
	
	@smoke_test
	Scenario: I can add an item to the cart
		Given I close the welcome banner
		When I navigate to the login page
		Then the login page has loaded
		When I log in as standard user
		Then I should be logged in
		When I add Apple Juice to basket