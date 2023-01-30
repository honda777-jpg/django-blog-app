from django.urls import path

from todo.views import TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView, TaskUpdateView

urlpatterns = [path("", TaskListView.as_view(), name="task-list"), # 画面表示した際に開かれる画面
               path("task/new/", TaskCreateView.as_view(), name="task-new"),
               path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"), # ユニークな値になるのはid、つまりPrimary Key。もし1つ目のタスクを開きたかったら、task/1/にアクセスすれば確認できる
               path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
               path("task/<int:pk>/edit", TaskUpdateView.as_view(), name="task-edit")
              ]
