from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from random import randint

def index(request):
    if 'gold_earn' not in request.session and 'activities' not in request.session:
        request.session['gold_earn'] = 0
        request.session['activities'] = []
    return render(request, 'ninja_money/index.html')

def reset(request):
    request.session.clear()
    return redirect(index)

def process_money(request):
    
    if request.method != 'POST':
        return redirect(index)

    # set date
    time_now = strftime("%Y/%m/%d %H:%M %p", gmtime())
    # record the building values
    building = request.POST['building']
    temp_list = request.session['activities']

    # check what the user chose
    if building == 'farm':
        farm = randint(10, 20)
        request.session['gold_earn'] += farm
        temp_list.append("<p class='text-success'>Earned " + str(farm) + " goals from the farm! (" + time_now + ")</p>")
    
    elif building == 'cave':
        cave = randint(5, 10)
        request.session['gold_earn'] += cave
        temp_list.append("<p class='text-success'>Earned " + str(cave) + " goals from the cave! (" + time_now + ")</p>")
    
    elif building == 'house':
        house = randint(2, 5)
        request.session['gold_earn'] += house
        temp_list.append("<p class='text-success'>Earned " + str(house) + " goals from the house! (" + time_now + ")</p>")

    else:
        casino = randint(-50, 50)
        
        if casino == 0:
            temp_list.append("<p class='text-warning'>Earned " + str(casino) + " goals from the casino! (" + time_now + ")</p>")
        # if random is negative
        elif casino < 0:
            temp = request.session['gold_earn']
            temp += casino
            casino = request.session['gold_earn'] - temp
            request.session['gold_earn'] = temp
            temp_list.append("<p class='text-danger'>Earned a casino and lost " + str(casino) + " goals... Ouch! (" + time_now + ")</p>")
        else:
            request.session['gold_earn'] += casino
            temp_list.append("<p class='text-success'>Earned " + str(casino) + " goals from the casino! (" + time_now + ")</p>")
    
    request.session['activities'] = temp_list
    return redirect(index)