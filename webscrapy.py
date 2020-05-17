import requests
import bs4
import webbrowser

new = 2
modal = ''

responseFromUrl = requests.get('ENTER A URL HERE')

def replaceStringInHtml (content, tag, newTag):
    return content.replace( tag, newTag)

elements = ['h1','H1','h2','H2','P','p','H3','h3']

with open('modal.txt', 'r') as htmlTags:
    modal = htmlTags.read()

content = responseFromUrl.text

content = replaceStringInHtml(content, "</head>", "<link rel='stylesheet' href='./test.css' media='all'> <script type='text/javascript' src='./js/mainHandler.js'></script></head>")
content = replaceStringInHtml(content, "</body>", modal)

for element in elements:
    content = replaceStringInHtml(content, '<'+element+'>',
                                  "<"+element+" onclick='selectThisTag(event)'>" )

file = open('test.html','w', encoding="utf-8")
file.write(content)
file.close()

webbrowser.open('test.html', new=new)


