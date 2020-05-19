import requests
import contentHandler
import browserHandler

url="https://isha.sadhguru.org/mahashivratri/hi/shiva-adiyogi/shiv-tandav-stotram-lyrics-meaning/"

responseFromUrl = requests.get(url)

content = responseFromUrl.text

content = contentHandler.addFiles(content, ['body','head'])
content = contentHandler.addEvents(content, ['h1','H1','h2','H2','P','p','H3','h3'])

browserHandler.launchBrowser( content )