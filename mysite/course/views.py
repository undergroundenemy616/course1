from django.http import HttpResponse
from rest_framework.generics import GenericAPIView


class GroupView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        arch = request.FILES['archieve']
        # new_arch = change_sheet(arch)
        response = HttpResponse("das", content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename=archieve.zip'
        return response
