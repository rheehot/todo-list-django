from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
# 단순 HTML 문저 내용의 비교라면 해당함수를 이용할 수 도 있다.
from django.template.loader import render_to_string  
from .views import index  # 아직 만들진 않았지만, 추후에 만들 view함수
# Create your tests here.

class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_correct_html(self):
        response = self.client.get('/')
        
        # 아! 호우! 해당 테스트는, mark-up 상태에서의 html과, response로 들어온 html을 비교하는 작업이다.
        # ecpected_html = render_to_string('todolist/index.html')
        # self.assertEqual(html, ecpected_html)
        # 위 두 코드를 합친 것이 아래 코드와 같다.  
        self.assertTemplateUsed(response, 'todolist/index.html')
        # 일부로 잘못된 template를 가져와보기도 하자.
        self.assertTemplateNotUsed(response, 'todolist/wrong.html')


class TodoModelTest(TestCase):
    def test_read_todo_model_with_empty_db(self):
        todos = Todo.objects.all()
        self.assertEqual(todos, None)
    
    def test_create_todo_model_with_empty_db(self):
        todo = Todo()
        todo.content  = '시장에서 미역 사기'
        todo.save()
        self.assertEqual(todo.content, '시장에서 미역 사기')
        self.assertEqual(todo.pk, 1)
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.is_completed, False)

    def test_delete_todo_model_with_a_todo(self):
        # create first
        todo = Todo()
        todo.content  = '시장에서 미역 사기'
        todo.save()
        
        # 빈 공간에서 새로 만들었으니, pk는 1
        todo = Todo.objects.get(pk=1)
        todo.delete()

        self.assertTrue(Todo.objects.all(), None)
        self.assertTrue(Todo.objects.get(pk=1), None)
        