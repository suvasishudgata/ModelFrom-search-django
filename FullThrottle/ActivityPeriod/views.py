from django.shortcuts import render
from ActivityPeriod.faker import UserFactory
from ActivityPeriod.models import User
from ActivityPeriod.forms import UserList
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


'''
#Used to create dummy user data
for _ in range(0, 200):
    UserFactory.create()
'''
activityPeriods =[
                [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			    ],
                [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:22PM"
				}
			    ]
            ]

#accessing the user model
names = User.objects.all()
nameList = []


count = User.objects.count()

i = 0
#Storing the User data into list
for name in names:
    if i%2 == 0:
        nameList.append({'name':str(name), 'userId':str(name.userId), 
        'timezone':str(name.userTimeZone), 'activityPeriods':activityPeriods[0]})
    else:
        nameList.append({'name':str(name), 'userId':str(name.userId), 
        'timezone':str(name.userTimeZone), 'activityPeriods':activityPeriods[1]})    
    i = i + 1

print(nameList)    
        

#Funtion to get the username from the form
def getName(request):
    if request.method == 'POST':
        form = UserList(request.POST)
    else:
        form = UserList()
    return render(request, r'ActivityPeriod\home.html', {'form':form})

#Funtion to display the user details
@csrf_exempt
def Users(request):
    name = request.GET.get('name')
    return render(request, r'ActivityPeriod\base.html', {'name':str(name), 
                'nameList':nameList})
