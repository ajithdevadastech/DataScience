#Step1: Import the required library
import matplotlib.pyplot as plt

#Step2: Enter the data
languages = 'Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

#Step3: Assign the colors
colors = ['#FA8F0A','#F0DA32','#61F527','#18DE9D','#3594FF','#8B5A8C']

#Step4: Plot the chart
plt.pie(popularity, labels=languages, colors=colors)
plt.title('Popularity of Programming Languages in 2019')
plt.show()

#Let's look at a few more parameters of matplotlib.pyplot.pie:

#Step5: autopct parameter
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%')
plt.show()

#<b>autopct</b> is a string or function used to label the wedges with their numeric value.
# The label is placed inside the wedge.

#Step6: explode parameter
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode)
plt.show()

#<b>explode</b> is a len(x) array which specifies the fraction of the radius with which to offset each wedge.

#Step7: shadow parameter
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True)
plt.show()

#<b>shadow</b> parameter draws a shadow beneath the pie.

#Step8: startangle parameter
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140)
plt.show()

#<b>startangle</b> rotates the start of the pie chart by angle degrees counterclockwise from the x-axis.

#Step9: frame parameter
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140,
        frame=True)
plt.show()

#<b>frame</b> parameter plots axes frame with the chart if true.

#Step10: rotatelabels parameter
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140,
        frame=True, rotatelabels=True)
plt.show()

#<b>rotatelabels</b> parameter rotates each label to the angle of the corresponding slice if true.

#Step11: wedgeprops parameter
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140,
        frame=True, rotatelabels=True, wedgeprops = {'linewidth': 10})
plt.show()

#<b>wedgeprops</b> parameter sets the width of the wedge border lines.

#Step12: radius parameter
plt.pie(popularity, labels=languages, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140,
        frame=True, rotatelabels=True, wedgeprops = {'linewidth': 3}, radius=2)
plt.show()

#The <b>radius</b> of the pie, if radius is None it will be set to 1.





