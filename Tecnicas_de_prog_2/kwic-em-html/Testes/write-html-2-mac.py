import webbrowser

f = open('helloworld.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

#Change path to reflect file location
filename = '/home/guileb/Faculdade/Tecnicas_de_programacao_2/' + 'helloworld.html'
webbrowser.open_new_tab(filename)