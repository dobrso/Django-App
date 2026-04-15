from django.urls import path

from .views import RoomsListView, RoomCreateView, RoomDetailView, RoomUpdateView, RoomDeleteView, RoomJoinView, \
    RoomLeaveView

app_name = 'rooms'

urlpatterns = [
    path('', RoomsListView.as_view(), name='rooms_list'),
    path('create/', RoomCreateView.as_view(), name='room_create'),
    path('<int:room_id>/', RoomDetailView.as_view(), name='room_detail'),
    path('<int:room_id>/update/', RoomUpdateView.as_view(), name='room_update'),
    path('<int:room_id>/delete/', RoomDeleteView.as_view(), name='room_delete'),
    path('<int:room_id>/join/', RoomJoinView.as_view(), name='room_join'),
    path('<int:room_id>/leave/', RoomLeaveView.as_view(), name='room_leave'),
]