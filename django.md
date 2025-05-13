#### 三种路由匹配模式

```python
urlpatterns = [
    path("hello/", hello),
    path('article/create/', article_create, name="article_create"),
    path('article/<int:article_id>/', article_detail, name="detail"),
    re_path(r'^phone/(?<phone_number>1[3456789]\d{9})/$', phone_detail, name="phone_detail"),
    path("admin/", admin.site.urls),
]
```

