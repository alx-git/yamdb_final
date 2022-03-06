from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.permissions import IsAdminOrSuper
from .serializers import (
    SignUpSerializer,
    ConfirmationSerializer,
    UserSerializer,
)

User = get_user_model()


def send_token(email):
    user = User.objects.get(email=email)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='Confirmation code',
        message=f'Your confirmation code: {confirmation_code}',
        from_email=settings.EMAIL_HOST_ADDRESS,
        recipient_list=(email,),
        fail_silently=False)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def sign_up(request):
    username = request.data.get('username')
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    if User.objects.filter(email=email).exists():
        send_token(email)
        return Response(
            {'Error': 'User/email already exist.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    if (
        username == 'me'
        or User.objects.filter(username=username).exists()
    ):
        return Response(
            {'Error': 'You can\'t choise this username.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    User.objects.create_user(username=username, email=email)
    send_token(email)
    return Response(
        request.data,
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def sign_confirm(request):
    serializer = ConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    confirmation_code = serializer.data.get('confirmation_code')
    user = get_object_or_404(User, username=username)
    if not default_token_generator.check_token(user, confirmation_code):
        return Response(
            {'confirmation_code': 'bad confirmation code'},
            status=status.HTTP_400_BAD_REQUEST
        )
    refresh = RefreshToken.for_user(user)
    return Response(
        {'access': str(refresh.access_token)},
        status=status.HTTP_200_OK
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsAdminOrSuper,
    )
    pagination_class = PageNumberPagination
    lookup_field = 'username'
    filter_backends = (
        filters.SearchFilter,
    )
    search_fields = ('username',)

    @action(
        detail=False,
        methods=('get', 'patch'),
        url_path='me',
        permission_classes=(
            permissions.IsAuthenticated,
        ),
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        serializer = self.get_serializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
