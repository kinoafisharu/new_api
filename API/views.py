from django.shortcuts import render

# -/ Александр Караваев
# Рендеринг главной страницы API с документацией и ссылками
def index(request):
    return render(request, 'index.html')
