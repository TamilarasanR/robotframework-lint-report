from bs4 import BeautifulSoup
import os

page_html="""
<!DOCTYPE html>
<html>
 <head>
 <link rel="shortcut icon" href="https://png.icons8.com/windows/50/000000/bot.png" type="image/x-icon" />
  <title>RFLint Result</title>
  <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" rel="stylesheet"/>
  <script src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
  <script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet"/>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
 </head>
</html>
"""

soup = BeautifulSoup(page_html,"html.parser")

body = soup.new_tag('body',style="font-family: Consolas,\"courier new\";float:left")
soup.insert(50, body)

# Create header tag and title
h1 = soup.new_tag('h1',style="display: block;font-size: 1em;padding: 10px;")
h1.string = "Robot Framework Lint Result"
body.insert(0, h1)

# Get rflint result - OS independent
current_path = os.getcwd()
# rflint text file location
text_file = os.path.join(os.path.curdir, 'rflint_result.txt')
# rflint result file location
result_file = os.path.join(os.path.curdir, 'rflint_result.html')

# RFlint supporrted warnings
warning = [
    'FileTooLong',
    'InvalidTable',
    'LineTooLong',
    'PeriodInSuiteName',
    'PeriodInTestName',
    'RequireSuiteDocumentation',
    'TooFewKeywordSteps',
    'TooFewTestSteps',
    'TooManyTestCases',
    'TooManyTestSteps',
    'TrailingBlankLines',
    ]

# Validate rflint result is not empty
if os.stat(text_file).st_size==0:
    # Create header tag and title
	div = soup.new_tag('div',style="padding: 20px;background-color: #ddffdd;border-left: 16px solid #4CAF50; width: 70%;")
	div['class'] = "w3-panel w3-note"
        div.string = "RF Lint Analysis Completed. You've All Caught Up"
	body.insert(52, div)
else:    
    files_count = 0
    error_count = 0
    warning_count = 0

    # Open rflint result text file
    with open(text_file,'r') as infile:
        # Iterate for line
        for line in infile:
            # Split new line 
            CONTENT = line.split("/n")
            # Iterate for every new line
            for coltext in CONTENT: # important that you reverse order            
                if ".robot" in coltext:
                    #global files_count
                    files_count+=1
                elif "W" in coltext:
                    #global error_count
                    error_count+=1
                elif "E" in coltext:
                    #global warning_count
                    warning_count +=1

    dashboard_content="""
    <div class="tabcontent" id="dashboard" style="padding: 20px;">
        <h6><b><i class="fa fa-dashboard"></i> Statistics</b></h6>
        <div class="w3-row-padding w3-margin-bottom" style="padding: 20px;">
        <div class="w3-quarter col-sm-4">
            <div class="w3-container w3-teal" style="text-align:center;">Files: <b>%s</b></div>
        </div>
        <div class="w3-quarter col-sm-4">
            <div class="w3-container w3-red" style="text-align:center;">Errors: <b>%s</b></div>
        </div>
        <div class="w3-quarter col-sm-4">
            <div class="w3-container w3-brown" style="text-align:center;">Warnings: <b>%s</b></div>
        </div>
        </div>
        <div class="tabcontent" id="analysis" >
        <h6><b><i class="fa fa-th-list"></i> Analysis</b></h6>
    """ % (files_count,error_count,warning_count)
    body.append(BeautifulSoup(dashboard_content, 'html.parser'))

# Open rflint result text file
with open(text_file,'r') as infile:

    # Iterate for line
    for line in infile:

        # Split new line 
        CONTENT = line.split("/n")

        # Iterate for every new line
        for coltext in CONTENT: # important that you reverse order
            
            # If line is file name then add responsive-button
            if ".robot" in coltext:
                
                # create div tag with responsive
                parent_div = soup.new_tag('div')
                parent_div["class"] = "ui-content"
                parent_div["data-role"] = "main"
                body.insert(55, parent_div)

                # create div tag with responsive
                child_div = soup.new_tag('div')
                child_div["data-role"] = "collapsible"
                parent_div.insert(0, child_div)
                
                # create h4 tag with responsive
                header = soup.new_tag('h4')
                child_div.insert(0, header)

                label = soup.new_tag('span',style="width: 5em;border: 1px solid black;font-weight: bold;")
                label["class"] = "badge badge-info"
                label.string = "FILE: "
                header.insert(0, label)

                file_name = soup.new_tag('span',style="font-weight: bold;")
                text = coltext.strip().replace('+ .', '')
                file_name.string = text
                header.insert(1, file_name)

                # create ol tag, all the warnings, errors will be added under this
                ol = soup.new_tag('ol',style="background: #ff9999; padding: 5px;border: 1px solid;")
                child_div.insert(0, ol)
            
            else:

                try:

                    # create li tag, all the warnings, errors will be added
                    li = soup.new_tag('li',style="background: #ffe5e5;padding: 5px;margin-left: 35px;;border: 1px solid;border-color: #ccc;")
                    ol.insert(1, li)

                except NameError:
                    print "Tag not found. Skipping result."
                    continue

                # IF message type is warning as 'WARNING' badge else, 'ERROR' badge
                if any(label in coltext for label in warning):  
                    
                    label = soup.new_tag('span',style="width: 7em;border: 1px solid black;font-weight: bold;")
                    label["class"] = "badge badge-warning"
                    label.string = "WARNING"
                    text = coltext.strip().replace('W: ', 'Line No:')
                    li.insert(0, label)

                else :

                    label = soup.new_tag('span',style="width: 7em;border: 1px solid black;font-weight: bold;")
                    label["class"] = "badge badge-danger"
                    label.string = "ERROR"
                    text = coltext.strip().replace('E: ', 'Line No:')
                    li.insert(0, label)

                message = soup.new_tag('span')
                message.string = text
                li.insert(1, message)

# Write output as html file
with open(result_file, 'w') as outfile:
    outfile.write(soup.prettify())