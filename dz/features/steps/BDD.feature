Feature: testing bot
	Scenario: raise to power digit
		Given I send bot message /start
		When I send bot first message 2
		When I send bot second message 5
		Then I send bot operation ^ and get answer 32
	Scenario: sum two digits
		Given I send bot message /start
		When I send bot first message 5
		When I send bot second message 12
		Then I send bot operation <> and get answer 13
