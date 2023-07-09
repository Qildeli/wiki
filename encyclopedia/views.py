from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse

import random
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        raise Http404("Encyclopedia entry does not exist.")
    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })


def search(request):
    query = request.GET.get('q')
    exact_match = util.get_entry(query)
    if exact_match is not None:
        return redirect('entry', title=query)
    else:
        # Get all entries
        all_entries = util.list_entries()
        # Filter entries to only include ones that contain the query as a substring
        matching_entries = [entry for entry in all_entries if query.lower() in entry.lower()]
        # Render index template with matching entries
        return render(request, 'encyclopedia/index.html', {'entries': matching_entries})


def new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if util.get_entry(title) is not None:
            # An entry with this title already exists
            return render(request, "encyclopedia/error.html", {
                "message": "An entry with this title already exists."
            })

        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry", kwargs={'title': title}))
    else:
        return render(request, "encyclopedia/new.html")


def edit(request, title):
    if request.method == "POST":
        # Handle form submission
        content = request.POST["content"]
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry", args=[title]))
    else:
        # Display form for editing
        content = util.get_entry(title)
        if content is None:
            return render(request, "encyclopedia/error.html", {
                "error_message": f"Entry {title} does not exist."
            })
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "content": content
            })


def random_entry(request):
    entries = util.list_entries()
    random_title = random.choice(entries)
    return HttpResponseRedirect(reverse("entry", args=[random_title]))
