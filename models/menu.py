# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# This minimal constant menu is extended in the controller model folders
# so that it changes by the controller context

response.logo = IMG(_src=URL('static','images/imperial_white.png'), _height='70px')
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

response.menu = [
    (T('Marking'), False, URL('marking_reports', 'index'), []),
    (T('Timetabler'), False, URL('timetabler', 'index'), []),
    (DIV(_style='border-left: 3px solid #FFFFFF80; height: 40px;margin:0px 10px'), False, False, [])]

