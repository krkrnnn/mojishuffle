#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

html_body = """
<html><head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
</head>
<body>
%s
</body></html>"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

        form = cgi.FieldStorage()
        m1 = form.getvalue('moji1', '')
        m2 = form.getvalue('moji2', '')
        shufflemoji = ''

        for index in range(0, min(len(s1), len(s2))-1):
            shufflemoji += m1[index]
            shufflemoji += m2[index]


        if len(s1) > len(s2):
            shufflemoji += s1[len(s2):len(s1)-1]
        elif  len(s2) > len(s1):
            shufflemoji += s2[len(s1):len(s2)-1]

        print "Content-type: text/html\n"
        print html_body % shufflemoji


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
