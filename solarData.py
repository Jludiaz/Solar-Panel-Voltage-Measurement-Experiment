import numpy as np
import matplotlib.pyplot as plt

#We open our txt. files
f1 = open("/Users/jeremyludiaz/Documents/brightConditions.txt", "r") #bright
f2 = open("/Users/jeremyludiaz/Documents/flashlight6inches.txt", "r") #6 inches
f3 = open("/Users/jeremyludiaz/Documents/flashlight12inches.txt", "r") #12 inches
f4 = open ("/Users/jeremyludiaz/Documents/darkconditions.txt", "r") #dark conditions

#we read our contents and set them to a variable
contents = f1.read()
contents2 = f2.read()
contents3 = f3.read()
contents4 = f4.read()

#we split each of our data numbers with ,
splitContents = contents.split(",")
splitContents2 = contents2.split(",")
splitContents3 = contents3.split(",")
splitContents4 = contents4.split(",")

for i in range (len(splitContents)):
    splitContents[i] = float(splitContents[i])
    
for i in range (len(splitContents2)):
    splitContents2[i] = float(splitContents2[i])

for i in range (len(splitContents3)):
    splitContents3[i] = float(splitContents3[i])
    
for i in range (len(splitContents4)):
    splitContents4[i] = float(splitContents4[i])
   
#We print our contnts that we open in our txt.fil  
print (splitContents)
print (splitContents2)
print (splitContents3)
print (splitContents4)

#add points to plot
fig, (ax1, ax2) = plt.subplots(2, 1)
#define data
x=range(0,10)
# y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#We plot our ontents in our graph and we plot out points
ax1.plot(splitContents)
ax1.plot(splitContents2)
ax1.plot(splitContents3)
ax1.plot(splitContents4)

#find line of best fit
a, b = np.polyfit(x, splitContents, 1)
a1, b1 = np.polyfit(x, splitContents2, 1)
a2, b2 = np.polyfit(x, splitContents3, 1)
a3, b3 = np.polyfit(x, splitContents4, 1)

#add line of best fit to plot
#We use colors to tell the difference between our graphs 
ax1.plot(x, a*x+b, color='steelblue', linestyle='--', linewidth=2)
ax1.plot(x, a1*x+b1, color='orange', linestyle='--', linewidth=2) 
ax1.plot(x, a2*x+b2, color='red', linestyle='--', linewidth=2)
ax1.plot(x, a3*x+b3, color='green', linestyle='--', linewidth=2)

#Set my labels for the top graph
ax1.set_ylabel('Voltage')
ax1.set_xlabel('Readings')
ax1.set_title('Data from Solar Panel')

#Set our legend's labels, location. (outside the graph)
ax1.legend(['Bright', 'Flash 6 Inches', 'Flash 12 Inches', 'Dark'], loc='best', bbox_to_anchor=(1.0, 1.0)) 


#Bottom graph
light = ['Bright', '6 Inches', '12 Inches', 'Dark'] #X values
counts = [3.8798, 2.2902, 1.2324, 0.6208] #Highest Y Values
bar_labels = ['Bright', '6 Inches', '12 Inches', 'Dark'] #Legend
bar_colors = ['tab:blue', 'tab:orange', 'tab:red', 'tab:green'] #Bar Colors

ax2.bar(light, counts, label=bar_labels, color=bar_colors)

#print labels for my graphs
ax2.set_ylabel('Voltage')
ax2.set_title('Average Voltage Reading')
# ax2.legend(title='Conditions')


#add fitted regression equation to plot
#plt.text(1, 4, 'y = ' + '{:.2f}'.format(b) + ' + {:.2f}'.format(a) + 'x', size=14)


plt.show()

