Feature: Keyword search
  Scenario: Searching for a keyword on google web site
    Given I launch Chrome browser
	When I go on google web site
	And I enter the keyword "Publicis Sapient" in the search bar
	And I click on Google search button
	Then The google web site displays the results of the search containing the keyword Publicis Sapient

