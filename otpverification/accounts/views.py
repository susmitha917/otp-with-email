from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .emails import *

# Create your views here.
class RegisterAPI(APIView):
    
    def post(self,request):
     try:
         data=request.data
         serializer=UserSerializer(data=data)
         if serializer.is_valid():
            serializer.save()
            send_email(serializer.data['email'])
            return Response({
                'status':200,
                'message':'registration sucessfully check email',
                'data':serializer.data
            })
         return Response({
            'status':400,
            'message':'Something went wrong ',
            'data':serializer.errors
        })
     except Exception as e:
        print(e)

class verifyuser(APIView):
   def post(self,request):
      try:
         data=request.data 
         serializer=VerifyaccountSerializer(data=data)
         if serializer.is_valid():
            email=serializer.data['email']
            otp=serializer.data['otp']
            user=User.objects.filter(email=email)
            if not user.exists():
               return Response({
            'status':400,
            'message':'Something went wrong ',
            'data':'invalid email'
             })
            if user[0].otp !=otp:
               return Response({
            'status':400,
            'message':'Something went wrong ',
            'data':'invalid otp'
             })
            user[0].is_verified=True
            user[0].save()
               
            return Response({
                'status':200,
                'message':'Account Verified',
                'data':{}
            })
         return Response({
            'status':400,
            'message':'Something went wrong ',
            'data':serializer.errors
        })

      except Exception as e:
         print(e)      
