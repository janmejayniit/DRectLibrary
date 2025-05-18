from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BorrowViewSet, BorrowDetailViewSet

router = DefaultRouter()
router.register(r'borrows', BorrowViewSet, basename='borrow')

urlpatterns = [
    # path('', include(router.urls)),
    # path('<int:user>/<int:book>/', BorrowDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='borrow-detail'),
    # path('<int:user>/<int:book>/return/', BorrowDetailViewSet.as_view({'post': 'return_book'}), name='borrow-return'),
    # path('<int:user>/<int:book>/renew/', BorrowDetailViewSet.as_view({'post': 'renew_book'}), name='borrow-renew'),
    # path('<int:user>/<int:book>/issue/', BorrowDetailViewSet.as_view({'post': 'issue_book'}), name='borrow-issue'),

    path('', include(router.urls)),
    path('<int:user>/<int:book>/', BorrowDetailViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    }), name='borrow-detail'),

    path('<int:user>/<int:book>/return/', BorrowDetailViewSet.as_view({
        'post': 'return_book'
    }), name='borrow-return'),

    path('<int:user>/<int:book>/renew/', BorrowDetailViewSet.as_view({
        'post': 'renew_book'
    }), name='borrow-renew'),

    path('<int:user>/<int:book>/issue/', BorrowDetailViewSet.as_view({
        'post': 'issue_book'
    }), name='borrow-issue'),
]
