rem Executing rflint command and publishing result to rflint_result.txt file
rflint . > "rflint_result.txt" & 

rem Converting rflint_result.txt to rflint_result.html
python rflint_convert_text_to_html.py & 

rem Launching chrome with result file
start chrome "rflint_result.html"