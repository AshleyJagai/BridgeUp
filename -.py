#so python can graph scatter plot
import matplotlib.pyplot as plt

#so python can read the image
import matplotlib.image as img

#clear all previous graphs
plt.clf()

#open file
QuakeData = open("currentQuakes.txt")

#read and skip the line 
QuakeData.readline()

#make lists of coordinates
LAT = []
LONG = []

for line in QuakeData:
    line = line.split(',') #splits the list with commas
    LAT.append(float(line[1])) # add values to the list 
    LONG.append(float(line[2])) # add values to the list

# put the points in graph as magenta Xes 
plt.scatter(LONG, LAT, marker = "x", color = "magenta")

#graph title
plt.suptitle("Latitude and Longitude of Earthquakes in 2017", y = .8)

# label the y-axis
plt.ylabel("Latitude")

#label the X-axis
plt.xlabel("Longitude")

#read image
image = img.imread("world-map.gif")

#show the image 
plt.imshow(image, extent = [-197.962, 197.701, -63.8313, 87.9263])

#show the plot
plt.show()
