from django.http import HttpResponse
from django.shortcuts import render
import string

def capitalize(s):
    a=''
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            a += chr(ord(s[i])-32)
        else:
            a+=s[i]
    return a


def small(s):
    a=''
    for i in range(len(s)):
        if s[i] >= 'A' and s[i] <= 'Z':
            a += chr(ord(s[i])+32)
        else:
            a +=s[i]
    return a


def removepunc(s):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    p = ''
    for i in range(len(s)):
        if s[i] not in punc:
            p += s[i]
    return p


def countword(s):
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            count += 1
    return f'Total no. of words:{count+1}'


def capalternate(s):
    a=''
    for i in range(0, len(s), 2):
        if ((s[i] and s[i+1]) >= 'A' and (s[i] and s[i+1]) <= 'Z'):
            a += chr(ord(s[i+1]+32))
        elif (s[i] >= 'a' and s[i] <= 'z'):
            a += chr(ord(s[i])-32)
        elif (s[i+1] >= 'a' and s[i+1] <= 'z'):
             a += chr(ord(s[i+1])-32)
        else:
            a+=s[i]
    return a
'''===========================================================================================================
    =========================================================================================================='''

def index(request):
    return render(request,'textanalyzer1.html')

'''=========================================TEXT ANALYZE FUNCTION====================================================================='''

def txtanalyze(request):
    rqstlist = {'text':request.POST.get('textfield', 'default'),
                'allcapital':request.POST.get('capitalize', 'off'),
                'removepunction':request.POST.get('removepunc', 'off'),
                'allsmall':request.POST.get('small', 'off'),
                'wordcount':request.POST.get('countWord', 'off'),
                'capitalalternate':request.POST.get('capitalAlternate', 'off')}

    print(f'''
        TextData:{rqstlist['text']}
        AllCapital:{rqstlist['allcapital']}
        RemovePunctuation:{rqstlist['removepunction']}
        AllSmall:{rqstlist['allsmall']}
        WordCount:{rqstlist['wordcount']}
        AlternateCapital:{rqstlist['capitalalternate']}''')



    if rqstlist['allcapital']=='on':
        cap=capitalize(rqstlist['text'])
        para={'purpose':'All Letters Are Capitalized.','analyzedtext':cap}
        return render(request,'analyzed.html',para)
    elif rqstlist['removepunction']=='on':
        rmv=removepunc(rqstlist['text'])
        para = {'purpose': 'All Punctuations Are Removed.', 'analyzedtext': rmv}
        return render(request, 'analyzed.html', para)
    elif rqstlist['allsmall']=='on':
        sm=small(rqstlist['text'])
        para = {'purpose': 'All Letters are smalized.', 'analyzedtext': sm}
        return render(request, 'analyzed.html', para)
    elif rqstlist['wordcount'] == 'on':
        cw = countword(rqstlist['text'])
        para = {'purpose': 'Number of Words Contains In Your Text.', 'analyzedtext': cw}
        return render(request, 'analyzed.html', para)
    elif rqstlist['capitalalternate'] == 'on':
        ca = capalternate(rqstlist['text'])
        para = {'purpose': 'All Alternate Letters are Capitalized', 'analyzedtext': ca}
        return render(request, 'analyzed.html', para)


    
    
