from django.shortcuts import render, HttpResponse

topics = [
    {'id':1, 'title':'Routing', 'body':'Routing is ..'},
    {'id':2, 'title':'View', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(
        f'''
        <html>
            <body>
                <h1>Django</h1>
                <ol>
                    {ol}
                </ol>
                <h2>Hello, Django</h2>
            </body>
        </html>
        '''
    )

def create(request):
    return HttpResponse('Create')

def read(request):
    return HttpResponse('Read')