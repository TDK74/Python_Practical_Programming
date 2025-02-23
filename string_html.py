template = """<html>
<head>
    <title>%(title)s</title>
<head>
<body>
%(text)s
</body>
<html>"""

data = {"title": "My site",
       "text": "Content"}

print(template % data)