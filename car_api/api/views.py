from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
import requests


@api_view()
def test(request):
    return Response({"message": "test"})

@api_view(['POST'])
def cars_post(request):
    make = request.data.get('make')
    model = request.data.get('model')
    serializer = CarSerializer(data={'make': make, 'model': model})


    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make.lower()}?format=json"
    response = requests.get(url)
    print('response:', response.text)
    if response.status_code == 200:
        data = response.json()
        results = data.get('Results', [])
        car_exists = any(result['Make_Name'].lower() == make.lower() and result['Model_Name'].lower() == model.lower() for result in results)
        if car_exists:
            # If the make exists, proceed with saving the car
            serializer = CarSerializer(data={'make': make, 'model': model})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': f'No models found for make {make}'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Failed to retrieve data from external API'}, status=response.status_code)




    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


