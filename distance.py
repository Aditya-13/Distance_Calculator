import math
import requests
from tkinter import *
api_key = '' # Get your API key from http://api.positionstack.com and paste here...
bg="#653D3D"

def distance_between_cities():
    print('Distance calculator By Aditya')
    place1 = textEntry1.get()
    place2 = textEntry2.get()
    
    url1 = "http://api.positionstack.com/v1/forward?access_key={}&query={}".format(api_key, place1)
    url2 = "http://api.positionstack.com/v1/forward?access_key={}&query={}".format(api_key, place2)
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)

    output.delete

    data1 = response1.json()
    lat1 = data1['data'][0]['latitude']
    long1 = data1['data'][0]['longitude']

    data2 = response2.json()
    lat2 = data2['data'][0]['latitude']
    long2 = data2['data'][0]['longitude']

    first_ele = float(math.sin((lat2*(math.pi / 180) - lat1*(math.pi / 180)) / 2)**2)
    middle_ele = float(math.cos(lat1*(math.pi / 180)) * math.cos(lat2*(math.pi / 180)))
    last_ele = float(math.sin((long2*(math.pi / 180) - long1*(math.pi / 180)) / 2)**2)

    distance = 2 * 6371000 * math.asin(math.sqrt(first_ele + (middle_ele)*(last_ele)))
    
    resultString = '  Distance between {} and {} is: \n\t\t{} Km \n\t\t{} Miles'.format(place1.capitalize(), place2.capitalize(), round(round(distance / 1000, 3), 2), round(round(distance / 1000, 3) / 1.6), 2)
    print(resultString)
    output.insert(END, resultString)
# distance_between_cities()

window = Tk()
window.title("Distance Finder")
window.geometry('400x500')
window.configure(background=bg)
logo = PhotoImage(file=" ") # Enter the path of the downloaded imsge here...

Label (window, image=logo, bg=bg, height=200, width=400).grid(row=0, column=1, sticky=E)

Label (window, text="Enter the starting place:", bg=bg, fg = "black", font="Montserrat 16").grid(row=4, column=1)

textEntry1 = Entry(window, width=30, bg=bg, fg="black", font="Montserrat 14", border=0.5)
textEntry1.grid(row=5, column=1)
Label (window, text="\nEnter the destination:", bg=bg, fg = "black", font="Montserrat 16").grid(row=7, column=1)

textEntry2 = Entry(window, width=30, bg=bg, fg="black", font="Montserrat 14", border=0.5)
textEntry2.grid(row=8, column=1)
Button (window, text="Calculate",border=3, font="Montserrat",width=7,command=distance_between_cities).grid(row=9, column=1)

output = Text(window,bg=bg, height=4, width= 40, wrap=WORD, font="Montserrat 12")
output.grid(row=10, column=1, columnspan=1)

window.mainloop()