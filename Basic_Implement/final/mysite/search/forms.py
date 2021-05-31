from django import forms
from search.models import Question, Answer, Book


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

        labels = {
            'title': '제목',
            'author': '저자',
        }
