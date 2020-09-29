Feature: register

  Scenario: Register as new user
    Given user has open the site
    When user in page header clicks link 'Sign up'
    Then system opens 'Authentification' page
    When user on 'Authentification' page in 'Create an account' from types 'email' in input field 'Email address'
    And user on 'Authentification' page in 'Create an account' from clicks button 'Create an account'
    Then system opens 'Create an Account' page
    When user on 'Create an Account' page on "Your personal information" form chooses "Mr." radiobutton
    And user on 'Create an Account' page on "Your personal information" form types "John" in input field "First name"
    And user on 'Create an Account' page on "Your personal information" form types "Smith" in input field "Last name"
    And user on 'Create an Account' page on "Your personal information" form types "12345" in input field "Password"
    And user on 'Create an Account' page on "Your personal information" form in 'Date of Birth' parameter in combobox "Day" choose "1"
    And user on 'Create an Account' page on "Your personal information" form in 'Date of Birth' parameter in combobox "Month" choose "January"
    And user on 'Create an Account' page on "Your personal information" form in 'Date of Birth' parameter in combobox "Year" choose "2000"
    And user on 'Create an Account' page on "Your personal information" form set checkbox "Sign up for our newsletter!"
    And user on 'Create an Account' page on "Your address" form types "John" in input field "First name"
    And user on 'Create an Account' page on "Your address" form types "Smith" in input field "First name"
    And user on 'Create an Account' page on "Your address" form types "Google LLC." in input field "Company"
    And user on 'Create an Account' page on "Your address" form types "1600 Amphitheatre Parkway" in input field "Address"
    And user on 'Create an Account' page on "Your address" form types "Mountain View" in input field "City"
    And user on 'Create an Account' page on "Your address" form in combobox "State" choose "California"
    And user on 'Create an Account' page on "Your address" form types "94043" in input field "Zip/Postal Code"
    And user on 'Create an Account' page on "Your address" form types "No additional info" in text area "Additional information"
    And user on 'Create an Account' page on "Your address" form types "0800 328 6081" in input field "Mobile phone"
    And user on 'Create an Account' page clicks on button 'Register'
    Then system opens 'My account' page



