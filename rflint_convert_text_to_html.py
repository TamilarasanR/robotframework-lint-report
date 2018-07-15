from bs4 import BeautifulSoup
import string
import os

soup = BeautifulSoup('''\<html><head><title>RF-Lint Result Dashboard</title></head></html>''')

html = soup.new_tag('html')
soup.insert(0, html)

metatag = soup.new_tag('meta')
metatag.attrs["name"] = "viewport"
metatag.attrs["content"] = "width=device-width, initial-scale=1"
soup.head.append(metatag)

link = soup.new_tag('link')
link.attrs["rel"] = "stylesheet"
link.attrs["href"] = "https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css"
soup.head.append(link)

script = soup.new_tag('script')
script.attrs["src"] = "https://code.jquery.com/jquery-1.11.3.min.js"
soup.head.append(script)

script = soup.new_tag('script')
script.attrs["src"] = "https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"
soup.head.append(script)

# Labels CSS files
link = soup.new_tag('link')
link.attrs["rel"] = "stylesheet"
link.attrs["href"] = "https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
soup.head.append(link)

script = soup.new_tag('script')
script.attrs["src"] = "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"
soup.head.append(script)

script = soup.new_tag('script')
script.attrs["src"] = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"
soup.head.append(script)

script = soup.new_tag('script')
script.attrs["src"] = "https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"
soup.head.append(script)

body = soup.new_tag('body',style="display: block;border: 1px solid transparent;font-family:sans-serif;float:left")
soup.insert(0, body)

h2 = soup.new_tag('h1',style="display: block;font-size: 2em;padding: 10px;")
h2.string = "RF-Lint Result Dashboard"
soup.insert(0, h2)

current_path = os.getcwd()
text_file = os.path.join(os.path.curdir, 'rflint_result.txt')
result_file = os.path.join(os.path.curdir, 'rflint_result.html')

warning = ['FileTooLong','InvalidTable','LineTooLong','PeriodInSuiteName',
            'PeriodInTestName','RequireSuiteDocumentation','TooFewKeywordSteps',
            'TooFewTestSteps','TooManyTestCases','TooManyTestSteps','TrailingBlankLines']

with open(text_file) as infile:   

    for line in infile:

        CONTENT = line.split("/n")
        for coltext in CONTENT: # important that you reverse order            
            
            if ".robot" in coltext:
                
                parent_div = soup.new_tag('div')
                parent_div["class"] = "ui-content"
                parent_div["data-role"] = "main"
                body.insert(0, parent_div)

                child_div = soup.new_tag('div')
                child_div["data-role"] = "collapsible"
                parent_div.insert(0, child_div)

                file_name = soup.new_tag('h4')
                file_name.string = coltext.strip().replace('+', '')
                child_div.insert(0, file_name)

                ol = soup.new_tag('ol',style="background: #ff9999; padding: 5px;border: 1px solid")
                child_div.insert(0, ol)
            
            else:

                li = soup.new_tag('li',style="background: #ffe5e5;padding: 5px;margin-left: 35px;;border: 1px solid;border-color: #ccc")
                ol.insert(1, li)

                if any(label in coltext for label in warning):  
                    
                    label = soup.new_tag('span',style="width: 5em;border: 1px solid black;font-weight: bold;")
                    label["class"] = "badge badge-warning"
                    label.string = "Warning"
                    text = coltext.strip().replace('W: ', 'Line No:')
                    li.insert(0, label)

                else :

                    label = soup.new_tag('span',style="width: 5em;border: 1px solid black;font-weight: bold;")
                    label["class"] = "badge badge-danger"
                    label.string = "Error"
                    text = coltext.strip().replace('E: ', 'Line No:')
                    li.insert(0, label)

                message = soup.new_tag('span')
                message.string = text
                li.insert(1, message)

with open(result_file, 'w') as outfile:
    outfile.write(soup.prettify())