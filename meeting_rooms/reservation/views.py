from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, reverse
from reservation.models import Room, Booking, BookingRooms
from django.template import loader
from datetime import datetime


# Create your views here.
class AddRoom(View):
    def get(self, request):
        return HttpResponse(render(request, "add_room.html"))

    def post(self, request):
        template = loader.get_template('add_room.html')
        context = {
            'message': ("Dodano nową salę"),
        }
        name = request.POST.get('room_name')
        if not name:
            return HttpResponse(template.render({'message': "Nie podano nazwy sali"}, request))
            # return render(request, 'add_room.html', {'message':"Nie podano nazwy sali"})

        size = request.POST.get('room_size')
        if not size:
            return HttpResponse(template.render({'message': "Nie podano wielkosci sali"}, request))
            # return render(request, 'add_room.html', {'message':"Nie podano wielkosci sali"})

        if request.POST.get('room_projector'):
            projector = True
        else:
            projector = False

        Room.objects.create(name=name, room_size=size, projector=projector)

        return render(request, 'add_room.html', context=context)

gi
class AllRooms(View):
    def get(self, request):
        rooms = Room.objects.all()
        response = {'rooms': rooms}

        return render(request, "base.html", context=response)


class Modify(View):
    def get(self, request, id):
        get_id = Room.objects.get(pk=id)
        # get_reservation = Booking.objects.filter(reserv_date= id)
        context = {
            'room': get_id,

        }

        return render(request, 'modifi.html', context)


class Delete(AllRooms):
    def get(self, request, id):
        room_delete = Room.objects.get(pk=id)
        room_delete.delete()

        v = AllRooms()
        return v.get(request)


class ReserveRoom(View):
    def get(self, request, id):
        get_id = Room.objects.get(pk=id)
        context = {
            'room': get_id
        }
        return render(request, 'reserve_room.html', context)

    def post(self, request, id):
        template = loader.get_template('reserve_room.html')

        context = {
            'message': ("Zarezerwowano salę"),
        }

        room_id = Room.objects.get(pk=id)
        my_date = request.POST.get('reservation_date')
        comment = request.POST.get('coment')

        if not my_date:
            return HttpResponse(template.render({'message': "Nie wybrano daty"}, request))

        checks = Booking.objects.filter(reserv_date=my_date)
        for i in checks:
            if my_date == i:
                return HttpResponse(template.render({'message': "Sala zostałą już zarezerwowana"}, request))

        rev = Booking.objects.create(reserv_date=my_date, comment=comment, room_id=room_id)

        return redirect(reverse('reserve', args=[rev.id]))
       # return render(request, 'reserve_room.html', context)
