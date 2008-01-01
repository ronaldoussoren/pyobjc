This project will one day be used to replace the PyObjC website by something
new and shiny, but is pretty useless in its current state.

Usage::

   python setup.py build
  
This will recreate the website in 'htdocs'. The website is a collection of 
static (html) files.

Done:
- Regenerate online examples from the source tree

Todo:
- Update all examples to have a summary.txt (short description for 
  the lists of examples) and readme.txt (a longer description). The readme.txt
  is optional.
- (Examples) The summary should be extracted from the readme file
- (Examples) Somehow create an RSS feed with the most recent samples 
  (the last month, adding older examples so ensure there are at least 10
  samples in the feed)
- Use the current website to create better template files
  (WIP, a problem is that the current site sucks: it uses table-based layout)
- Home page and news
- RSS feed for news items
- Extract documentation for pyobjc-core and framework wrappers
- Download page
- The current L&F on pyobjc.sf.net sucks, find something better
