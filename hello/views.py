from django.shortcuts import render, redirect

key2 = 0

# Create your views here.
def increase(request):
    global key2
    key2 += 1

    return redirect(to="home")

def home(request):
    global key2

    key = request.session.get("key", 0)
 
    if request.method == "POST":
        key += 1
        request.session["key"] = key

        # return HttpResponseRedirect(request.path_info)

    return render(request, "hello/index.html", context={"key": key, "key2": key2})

def about(request):
    data = {"ids": [1, 2, 3, 4], "news": "qwerty", "asd": "zxc"}
    return render(request, "hello/about.html", data)

