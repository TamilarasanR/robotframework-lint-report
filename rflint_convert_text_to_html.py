from bs4 import BeautifulSoup
import os

soup = BeautifulSoup('''\<html><head><title>RFLint Result</title></head></html>''')

# Create html tag
html = soup.new_tag('html')
soup.insert(0, html)

# Create meta tag
metatag = soup.new_tag('meta')
metatag.attrs["name"] = "viewport"
metatag.attrs["content"] = "width=device-width, initial-scale=1"
soup.head.append(metatag)

# Create link tag
link = soup.new_tag('link')
link.attrs["rel"] = "stylesheet"
link.attrs["href"] = "https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css"
soup.head.append(link)

# Create script tag - responsive button
script = soup.new_tag('script')
script.attrs["src"] = "https://code.jquery.com/jquery-1.11.3.min.js"
soup.head.append(script)

# Create script tag - responsive button
script = soup.new_tag('script')
script.attrs["src"] = "https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"
soup.head.append(script)

# Create link tag - badges
link = soup.new_tag('link')
link.attrs["rel"] = "stylesheet"
link.attrs["href"] = "https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
soup.head.append(link)

# Create script tag - badges
script = soup.new_tag('script')
script.attrs["src"] = "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"
soup.head.append(script)

# Create script tag - badges
script = soup.new_tag('script')
script.attrs["src"] = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"
soup.head.append(script)

# Create script tag - badges
script = soup.new_tag('script')
script.attrs["src"] = "https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"
soup.head.append(script)

body = soup.new_tag('body',style="display: block;border: 1px solid transparent;font-family:sans-serif;float:left")
soup.insert(0, body)

# Create header tag and title
h2 = soup.new_tag('h1',style="display: block;font-size: 2em;padding: 10px;")
h2.string = "Robot Framework Lint Result"
soup.insert(0, h2)

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

# Open rflint result text file
with open(text_file) as infile:

    # Iterate for every line
    for line in infile:

        # Split new line 
        CONTENT = line.split("/n")

        # Iterate for every line
        for coltext in CONTENT: # important that you reverse order
            
            # If line is file name then add responsive-button
            if ".robot" in coltext:
                
                # create div tag with responsive
                parent_div = soup.new_tag('div')
                parent_div["class"] = "ui-content"
                parent_div["data-role"] = "main"
                body.insert(0, parent_div)

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
                ol = soup.new_tag('ol',style="background: #ff9999; padding: 5px;border: 1px solid")
                child_div.insert(0, ol)
            
            else:

                # create li tag, all the warnings, errors will be added
                li = soup.new_tag('li',style="background: #ffe5e5;padding: 5px;margin-left: 35px;;border: 1px solid;border-color: #ccc")
                ol.insert(1, li)

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