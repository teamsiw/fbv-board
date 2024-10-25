import subprocess

# Django 셸에서 실행할 스크립트를 작성
script = """
from board.views import list  # list 뷰 함수 임포트
from board.models import Board
from django.test import RequestFactory

# 임시 데이터 생성 (데이터가 없을 경우에만)
if Board.objects.count() == 0:
    Board.objects.create(id=1, title="Sample Title", writer="Sample Writer", readcount=0)

# 가상의 GET 요청 생성 및 list 뷰 함수 호출
request = RequestFactory().get('/list/')
response = list(request)

# 응답과 쿼리셋의 내용 출력
print("응답 상태 코드:", response.status_code)
print("응답 내용:", response.content.decode())

# 쿼리셋 데이터 출력
board_list = Board.objects.all()
for board in board_list:
    print(board.id, board.title, board.writer, board.readcount)
"""

# Django 셸 실행
subprocess.run(['python', 'manage.py', 'shell'], input=script, text=True)