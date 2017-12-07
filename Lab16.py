"""
Lab 16
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

    except IOError as io_error:
        print("Wrong file or file path ", io_error)
    except UnicodeDecodeError as decode_err:
        print('Error decoding url: ', url, decode_err)

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


def get_nine_titles():
    """
    gets nine from all the headlines
    :return: nine headlines
    """

    all_titles = get_all_titles()

    new_index = 0
    nine_titles = ''
    for i in xrange(len(all_titles)):
        if all_titles[i:i + 14] == 'JASON SCHWARTZ':
            new_index = i
            break
    for j in range(new_index, len(all_titles)):
        if all_titles[j:j + 12] == 'LOUIS NELSON':
            nine_titles += all_titles[j - 1]
            break
        nine_titles += all_titles[j]

    return replace_achii_code(nine_titles)


def replace_achii_code(str):
    """
    coverts two ascii codes that appear in the file to their characters
    :param str:
    :return:
    """

    str = str.replace("&#039;", "'")
    str = str.replace("&amp;", "&")
    return str


def makePage():
    """
    creates a html file in the local drive that displays the nine
    headlines extracted from the file
    :return: the index.html file
    """
    file = open("/Users/pavlosp1967/Desktop/index.html", "wt")

    html = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01
    Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">

    <html>
    <head><title>Lab16</title>
    </head>
    <body align="center">
    <h1>CNN HEADLINES NOVEMBER 2017 </h1>
    <h3>These Are the Most Important News</h3>
    <hr>
    <p>{code}</p>

  </body>
  </html>""".format(code=get_nine_titles().replace('\n', '<br/>'))

    file.write(html)
    file.close()


makePage()
