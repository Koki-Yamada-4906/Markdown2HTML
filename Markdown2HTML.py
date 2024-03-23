!pip install markdown
!pip install pyperclip
import markdown
import pyperclip

css = """<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap');

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
    color: #333;
}

h1, h2, h3, h4, h5, h6 {
    color: #333;
    border-bottom: 1px solid #ddd;
}

p {
    line-height: 1.6;
}

code {
    background-color: #f9f9f9;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: monospace;
    color: #c7254e;
}

table {
    border-collapse: collapse;
    width: 100%;
}

table, th, td {
    border: 1px solid #ddd;
    padding: 8px;
}

pre {
    background-color: #f9f9f9;
    padding: 10px;
    border-radius: 3px;
}

blockquote {
    border-left: 4px solid #ddd;
    padding-left: 10px;
    color: #666;
    background-color: #f9f9f9;
}

em {
    font-family: 'Noto Sans JP', sans-serif;
    font-style: italic;
    color: gray;
}
</style>
"""

md_text = '''

'''

html = markdown.markdown(md_text, extensions=['extra', 'abbr', 'codehilite', 'toc', 'tables', 'sane_lists', 'smarty', 'wikilinks', 'nl2br', 'fenced_code', 'meta'])

try:
    pyperclip.copy(css+html)
except pyperclip.PyperclipException:
    print(css+html)
