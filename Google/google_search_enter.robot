*** Settings ***
Library    SeleniumLibrary

***Test Cases ***
Test Case 1
    [Tags]    tag with space
    Log    "Test case to verify google search."
    Open Browser    https://www.google.com/    chrome
    Wait Until Element Is Visible    name:q
    Input Text    name:q    RFLint Report Generation
    Press Key    name:q    \13

Test Case 1
    [Documentation]    Duplicate test case and documentation is to long to verify this is one more to verify

Test Case 2
    [Documentation]     This is a new documentation tool
    [Tags]    tag
    Log    Static
    Log    Static 1
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static

    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static
    Log    Static

Test Case A
    [Documentation]    This is a simple code to verify    
    No Operation

Test Case B
    [Documentation]    This is a simple code to verify    
    No Operation

Test Case c
    [Documentation]    This is a simple code to verify    
    No Operation

Test Case d
    [Documentation]    This is a simple code to verify    
    No Operation

Test Case e
    [Documentation]    This is a simple code to verify    
    No Operation

**Keywords***
Duplicate Keyword
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}

Duplicate Keyword
    [Arguments]    ${element}    ${value}
    Wait Until Element Is Visible    ${element}
    # Blank trailing space in next line
    Input Text    ${value}    


    