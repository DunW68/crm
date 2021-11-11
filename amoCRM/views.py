from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CodeSave
import requests
from crmest.settings import TOKEN
from .scripts import create_lead, patch_contact


class GetAuth(APIView):
    # save auth_code on a server-side
    # requirement parameters: code. client_id (you can take it from vidget)
    def get(self, request):
        code = request.GET.get('code', None)
        client_id = request.GET.get('client_id', None)
        if code and client_id:
            if CodeSave.objects.filter(client_id=client_id):
                CodeSave.objects.filter(client_id=client_id).delete()
            CodeSave.objects.create(code=code, client_id=client_id)
        return Response(code)


class ContactView(APIView):

    def get(self, request):
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        phone = request.GET.get('phone', None)
        token = {'Authorization': f'Bearer {TOKEN}'}
        if name:
            response = requests.get(f'https://zolberg68.amocrm.ru/api/v4/contacts?filter[name]={name}',
                                    headers=token)
            if response.status_code == 200:
                response = patch_contact(response, token)
            else:
                response = create_lead(name, phone, email, token)
                return Response(response)
        elif email:
            response = requests.get(f'https://zolberg68.amocrm.ru/api/v4/contacts?filter[custom_fields_values][email]={email}',
                                    headers=token)
            if response.status_code == 200:
                response = patch_contact(response, token)
            else:
                response = create_lead(name, phone, email, token)
                return Response(response)
        elif phone:
            response = requests.get(f'https://zolberg68.amocrm.ru/api/v4/contacts?filter[custom_fields_values][phone]={phone}',
                                    headers=token)
            if response.status_code == 200:
                response = patch_contact(response, token)
            else:
                response = create_lead(name, phone, email, token)
                return Response(response)
        else:
            response = create_lead(name, phone, email, token)
            return Response(response)
        return Response(response)
