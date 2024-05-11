import justpy as jp

class Home:

    path = '/home'
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, text="We are home, finally", classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="""
        Blabliblup
        """, classes="text-lg")

        return wp

jp.Route(Home.path, Home.serve)
jp.justpy()