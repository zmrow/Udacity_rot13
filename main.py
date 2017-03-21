import os
import jinja2
import webapp2
import codecs

# Jinja env setup taken from Googles sample app here:
# https://github.com/GoogleCloudPlatform/appengine-guestbook-python/blob/master/guestbook.py
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = JINJA_ENV.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class UserPage(Handler):
    def get(self, text=''):
        self.render("user_signup.html", text=text)

    def post(self):
        pass


class MainPage(Handler):
    def get(self, text=''):
        self.render("rot13.html", text=text)

    def post(self):
        text = self.request.get('text')
        rot13_text = codecs.encode(text, 'rot_13')
        self.render("rot13.html", text = rot13_text)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/user_signup', UserPage)],
                               debug=True)
