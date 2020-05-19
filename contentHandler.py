def replaceStringInHtml (content, tag, newTag):
    return content.replace( tag, newTag)

def addFiles ( content, files ):
    for fileName in files:
        tag = '</'+fileName+'>'
        with open('./__html__/'+fileName+'.txt', 'r') as file:
            fileContent = file.read()
        file.close()
        content = replaceStringInHtml(content, tag, fileContent)
    return content

def addEvents ( content, elementList ):
    event=" onclick='selectThisTag(event)'>"
    content = content
    for element in elementList:
        replaceStringInHtml(content, '<'+element+'>',
                                  "<"+element+ event )
    return content