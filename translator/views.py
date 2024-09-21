from django.shortcuts import render
from deepl.main import DeeplAPI
from .forms import DeeplForm

# Create your views here.
async def home(request):
    form = DeeplForm()

    if request.method == "POST":
        text = request.POST.get('text')
        target_language = request.POST.get('target_language').upper()

        deepl =  DeeplAPI('c14910ea-0957-59fa-7c09-8dc8757d11db:fx')

        trans = await deepl.translate(text, target_language)

        return render(request, "translator/index.html", context={"text": trans, "form": form})
    
    else:
        return render(request, "translator/index.html", context={"text": "", "form": form})
