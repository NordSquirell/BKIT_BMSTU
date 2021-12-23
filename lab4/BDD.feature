Feature: testing the function get_roots
	Scenario: get roots of BQ
		Given I put roots [1, -2, 1] into the function
		Then I get roots [-1.0, 1.0]

	Scenario: get roots of BQ
		Given I put roots [1, -10, 9] into the function
		Then I get roots [3.0, -3.0, 1.0, -1.0]
