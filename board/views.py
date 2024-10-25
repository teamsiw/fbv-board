from django.shortcuts import render, redirect, reverse
from .models import Board
from django import forms

# Board 모델을 기반으로 한 폼 클래스 정의
class BoardForm(forms.ModelForm):
    # 내부 클래스 Meta를 사용하여 모델 및 필드 정의
    class Meta:
        # 사용할 모델 지정
        model = Board  # Board 모델을 폼의 데이터 소스로 사용
        
        fields = ['title', 'writer', 'content']  # 폼에서 사용할 필드 목록 지정
        
def regist(request):
    # 요청 메서드가 POST인지 확인
    if request.method == 'POST':
        
        form = BoardForm(request.POST)  # 제출된 POST 데이터로 BoardForm 인스턴스를 생성
        # 폼이 유효한지 검사
        if form.is_valid():
            # 유효한 경우, 데이터베이스에 저장
            form.save()
            # 목록 페이지로 리다이렉트
            return redirect(reverse('board:list'))
    else:
        # GET 요청인 경우 빈 폼을 생성
        form = BoardForm()
    
    # 'board/regist.html' 템플릿을 렌더링하고, 폼을 컨텍스트로 전달
    return render(request, 'board/regist.html', {'form': form})

def edit(request, id):
    
    board = Board.objects.get(pk=id)

    if request.method == 'POST':
        board.title = request.POST['title']
        board.writer = request.POST.get('writer')
        board.content = request.POST['content']
        board.save()
        return redirect(reverse('board:read', args=(id,)))
    else:
        return render(request, 'board/edit.html', {'board': board})

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

def list(request):
    board_list = Board.objects.all().order_by('-id')
    context = {
        'board_list': board_list,
    }       
    return render(request, 'board/list.html', context)

def read(request, id):
    board = Board.objects.get(pk=id)
    board.incrementReadCount()
    return render(request, 'board/read.html', {'board':board})

def remove(request, id):
    board = Board.objects.get(pk=id)

    if request.method == 'POST':
        board.delete()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/remove.html', {'board': board})