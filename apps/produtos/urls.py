from django.urls import path
from . import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955

urlpatterns = [
    path('cadastrar_produto/', views.cadProduto, name ='cadProduto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos')
<<<<<<< HEAD
]

=======
]
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955
