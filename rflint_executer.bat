rem Below command will perform code check by executing rflint
rflint .\ > "rflint_result.txt" & 

rem Convert rflint result log to .html
python rflint_convert_text_to_html.py & 

rem Open chrome with result
start chrome "rflint_result.html"