from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'index.html')
def analyze(request):
    djtext=(request.GET.get('text',default=''))
    removepunc = (request.GET.get('removepunc', default='off'))
    uppercase = (request.GET.get('uppercase', default='off'))
    removenewline = (request.GET.get('removenewline', default='off'))
    extraspace = (request.GET.get('extraspace', default='off'))
    if (removepunc=='on'):
        punctation =''' !@#$%^&*()_+-=[]{}'";:\|?/.>,< '''
        analyzed=''
        for char in djtext:
            if char not in punctation:
                analyzed=analyzed+char

        print(analyzed)
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        return render(request,'analyze.html',params)

    if (uppercase=='on'):
        analyzed=''
        for char in djtext:
                analyzed = analyzed + char.upper()

        print(analyzed)
        params={'purpose':'UpperCase','analyzed_text':analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)

    if (removenewline == 'on'):
        analyzed = ''
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        print(analyzed)
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        return render(request, 'analyze.html', params)
    if (extraspace == 'on'):
        analyzed = ''
        for index,char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyzed = analyzed + char

        print(analyzed)
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Select at least one options")


