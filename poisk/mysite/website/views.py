from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'website/index.html')

def search(request):
    response = search_in_text(request.GET['q'])
    return render(request, 'website/index.html', {"result": response} if response else {"error": "0 результатов поиска"})

def word(word_in_text):
    for slovo in word_in_text:
        if count.get(slovo,None):
            count += 1
        else:
            count = 1
        print("Слово", slovo, "встречается", count, "раз")

def search_in_text(mumu):
    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read()

    marks = '''!()-[]{}:?@#$%:'"\,./^&amp;*_'''

    text = text.replace(marks, "")

    list_txt = []

    for i in text.split("."):
        if " "+mumu.lower()+" " in " "+i.strip().replace(",", "").lower()+" ":
            list_txt.append(i.strip())

    return list_txt


