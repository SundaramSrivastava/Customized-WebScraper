import webbrowser

def launchBrowser ( content ):
    file = open('test.html','w', encoding="utf-8")
    file.write(content)
    file.close()

    webbrowser.open_new_tab( 'test.html' )