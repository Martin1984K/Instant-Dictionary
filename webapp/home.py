import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the Home page', classes='text-4xl m-2')
        jp.Div(a=div, text="""
        Welcome, dear lover of definitions. We hope you enjoy the enlargement of your knowledge on a daily basis.
        """, classes='text-lg')
        return wp


