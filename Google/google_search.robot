*** Settings ***
Library    SeleniumLibrary

***Test Cases ***
Test Case 1
    Log    "Test case to verify google search."
    Open Browser    https://www.google.com/    chrome
    Wait Until Element Is Visible    name:q
    Input Text    name:q    RFLint Report Generation