from django.shortcuts import render


def sampleFormView(request):
    if request.method == 'GET':
        return render(request, 'sample_page.html')
    else:
        city = request.POST.get('city_name')
        country = request.POST.get('country_name')
        # Делаем запрос на сервера openweathermap
        # Получаем lat, lon
        # Получаем по координатам погоду
        context = {
            'weather': response['main']['name'],
            'temp': response['sys']['temp']
        }
        return render(request, '', context)
