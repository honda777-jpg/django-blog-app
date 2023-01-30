from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView # 一覧表示させるためのもの。今回に限らず汎用的に使用されるものなので、genericの中にある
from django.urls import reverse_lazy # 処理後画面遷移してくれる
from todo.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin # ログイン者以外、編集ページなどに入らせないようにする

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView): # taskを表示するためのListViewなので、TaskListViewというクラス名。一覧画面表示
    model = Task # models.pyのTaskクラスを使用
    template_name = "todo/task_list.html" # デフォルトは、task_list.htmlになってる。今回は設定しなくてもいいがわかりやすくするため記載

class TaskDetailView(LoginRequiredMixin, DetailView): # 詳細画面表示
    model = Task
    template_name = "todo/task_detail.html"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__" # ここでタスクの作成に使用する、title, description, deadlineのすべてを指定するのも良いんですけど、それは要するに全てのフィールドを使うということなので__all__と書けます。
    success_url = reverse_lazy("task-list") # urls.pyで設定した、name="task-list"の画面に飛ぶ
    template_name = "todo/task_form.html"

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")
    template_name = "todo/task_delete.html"

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")
    template_name = "todo/task_form.html"