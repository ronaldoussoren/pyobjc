"""
Support for news items
"""
import datetime, os

from docutils.core import publish_parts

def newsSelection(listing, maxAge=90, minitems=5):
    """
    Returns the news selection for the home page, defaults to the last
    quarter and at least 5 news items.
    """
    result = []
    mindate = datetime.date.today() - datetime.timedelta(maxAge)
    mindate = mindate.strftime('%Y-%m-%d')
    for item in listing:
        if len(result) < minitems:
            result.append(item)

        elif item['date'] >= mindate:
            result.append(item)

        else:
            break

    return result

def parseNews(sourcedir):
    """
    Returns an array of news items, sorted by date (newest item first)

    Very item is a dictionary with these keys:

    * date: the date for this item (YYYY-mm-dd)

    * headline: the headline

    * body: text of the message (in HTML format)

    * basename: basefile name for the news item
    """
    result = []
    for fn in os.listdir(sourcedir):
        if not fn[0].isdigit():
            continue

        basename = os.path.splitext(fn)[0]

        if '_' in basename:
            date = fn.split('_')[0]

        else:
            date = fn

        assert date.isdigit() and len(date) == 8

        date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]

        content = open(os.path.join(sourcedir, fn), 'r').read()


        parts = publish_parts(
            source=content,
            source_path=fn,
            writer_name='html',
            settings_overrides=dict(
                input_encoding='utf-8',
                initial_header_level=2,
            ))

        result.append(dict(
            basename = basename,
            date = date,
            headline = parts['title'],
            body = parts['body'],
        ))

    result.sort(key=lambda item: item['date'])
    result.reverse()
    return result


if __name__ == "__main__":
    print parseNews('../news')
