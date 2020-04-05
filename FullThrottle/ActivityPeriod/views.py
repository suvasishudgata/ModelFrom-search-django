from django.shortcuts import render
from ActivityPeriod.faker import UserFactory
from ActivityPeriod.models import User
from ActivityPeriod.forms import UserList
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


'''
#Creating Dummy users via Faker
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

#Creating Dummy Users Manually
nameList.append({'name': "Egon Spengler", 'userId': "W012A3CDE",
				'timezone': "America/Los_Angeles", 'activityPeriods':activityPeriods[0]})
nameList.append({'name': "Glinda Southgood", 'userId': "W07QCRPA4",
				'timezone': "Asia/Kolkata", 'activityPeriods':activityPeriods[1]})

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

#Saving the data from database into a file
with open('list_of_names.txt', "w") as output:
	for element in range (0, len(nameList)):
		output.write('%s\n' % str(nameList[element]))

#Funtion to get the username from the form
def getName(request):
    if request.method == 'POST':
        form = UserList(request.POST)
    else:
        form = UserList()
    return render(request, r'ActivityPeriod\home.html', {'form':form})

#Funtion to display the user details
def Users(request):
	name =  request.GET.get('name')
	return render(request, r'ActivityPeriod\base.html', {'name':str(name), 'nameList':nameList})