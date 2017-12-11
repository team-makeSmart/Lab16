"""
Lab 16: Opens a web-page and collects 6 headlines along with the 6 journalists that wrote them
team members: Pavlos Papadonikolakis, Maco Dousias, Jake McGhee
source website: https://www.politico.com/news/cnn
"""

import urllib

def get_html_file():
    """
       opens a web page and copies the html content
       :return the content of html file
    """
    html_file = ''
    url = ''
    try:
        url = 'https://www.politico.com/news/cnn'
        html_file = urllib.urlopen(url).read()

    except IOError:
        print("Wrong file or file path ")
    except UnicodeDecodeError:
        print('Error decoding url: ', url)

    return html_file

def get_all_titles():
    """
    gets all headlines from the file
    :return all the headlines

    """
    html_file = get_html_file()
    all_titles = ''
    start = 'target="_top">'
    end = '</a>'

    start_length = len(start)
    end_length = len(end)

    for i in xrange(len(html_file)):

        if html_file[i:i + start_length] == start:
            j = i + start_length

            if not html_file[j].isupper():
                pass

            else:
                while True:
                    all_titles += html_file[j]
                    j += 1

                    if html_file[j:j + end_length] == end:
                        all_titles += '\n'
                        break

    return all_titles

def get_headlines():
    """
    gets six out of all the headlines
    :return: six headlines
    """
    all_titles = get_all_titles()

    new_index = 0
    six_titles = ''
    for i in xrange(len(all_titles)):
        if all_titles[i:i + 14] == 'JASON SCHWARTZ':
            new_index = i
            break
    for j in range(new_index, len(all_titles)):
        if all_titles[j:j + 13] == 'STEVEN OVERLY':
            six_titles += all_titles[j - 1]
            break
        six_titles += all_titles[j]

    return six_titles.replace('\n','<br>')

def makePage():
    """
    creates a html file in the local drive that displays the nine
    headlines extracted from the file
    :return: the index.html file
    """
    file = open("/Users/pavlosp1967/Desktop/index.html", "wt")

    html = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01
    Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

    <html>
    <head><title>Lab16</title>
    </head>
    <body align="left">
    <h1>CNN HEADLINES NOVEMBER 2017</h1>
    <h3>These Are The Most Important News</h3>
    <hr>
    <p>"""+get_headlines()+"""</p>
    <hr>

    </body>
    </html>"""

    file.write(html)
    file.close()
    print 'index.html is created'

makePage()
