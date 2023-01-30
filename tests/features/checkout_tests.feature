Feature: Checkout tests
	
	@smoke_test
	Scenario: I can add an item to the cart
		Given I close the welcome banner
		When I navigate to the login page
		When I log in as standard user
		Then I should be logged in
		When I add Apple Juice to basket
		And I navigate to the create address page
		Then the create address page has loaded
		When I enter a new address
		Then the address select page has loaded