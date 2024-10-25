from django.shortcuts import render, redirect, reverse
from .models import Board


# Create your views here.
def index(request):
    return render(request, 'board/index.html')

def list(request):
    board_list = Board.objects.all()
    context = {
        'board_list': board_list,
    }       
    return render(request, 'board/list.html', context)

def read(request, id):
    board = Board.objects.get(pk=id)
    board.incrementReadCount()
    return render(request, 'board/read.html', {'board':board})

def regist(request):
    if request.method == 'POST':
        title = request.POST['title']
        writer = request.POST.get('writer')
        content = request.POST['content']
        Board(title=title, writer=writer, content=content).save()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/regist.html')