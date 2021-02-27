#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


## read csv file 
import io
import requests
url="https://raw.githubusercontent.com/LukeAFullard/Data-Analysis-Codes/main/Python-Codes/PythonBasics/pokemon_data.csv"
s=requests.get(url).content
df_Data =pd.read_csv(io.StringIO(s.decode('utf-8')))



##Scatterplots
# create a figure and axis
fig, ax = plt.subplots()
# scatter the Attack against the Defense
ax.scatter(df_Data['Attack'], df_Data['Defense'])
# set a title and labels
ax.set_title('Pokemon stuff')
ax.set_xlabel('Attack')
ax.set_ylabel('Defense')


##Scatterplot of multiple groups using multiple markers and marker sizes
# create color dictionary
colors = {'Fire':'r', 'Water':'g', 'Bug':'b'}
marks = {'Fire':'o', 'Water':'v', 'Bug':'x'}
sizes_marks = {'Fire':5, 'Water':40, 'Bug':80}
# create a figure and axis
fig, ax = plt.subplots()
# plot each data-point
for i in range(len(df_Data['Type 1'])):
    if df_Data['Type 1'][i] in colors.keys():
        ax.scatter(df_Data['Attack'][i], df_Data['Defense'][i],color=colors[df_Data['Type 1'][i]],marker=marks[df_Data['Type 1'][i]],s=sizes_marks[df_Data['Type 1'][i]])
# set a title and labels
ax.set_title('Pokemon')
ax.set_xlabel('Attack')
ax.set_ylabel('Defence')




## Lineplot
# get columns to plot
columns = df_Data.columns[4:9]
# create x data
x_data = range(0, df_Data.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, df_Data[column], label=column)
# set title and legend
ax.set_title('Pokemon stuff')
ax.legend()



##Histogram

# create figure and axis
fig, ax = plt.subplots()
# plot histogram
ax.hist(df_Data['Attack'])
# set title and labels
ax.set_title('Pokemon attack')
ax.set_xlabel('Attack Points')
ax.set_ylabel('Frequency')



## bar chart
# create a figure and axis 
fig, ax = plt.subplots() 
# count the occurrence of each class 
data = df_Data['Defense'].value_counts() 
# get x and y data 
points = data.index 
frequency = data.values 
# create bar chart 
ax.bar(points, frequency) 
# set title and labels 
ax.set_title('Pokemon defense') 
ax.set_xlabel('Defense Points') 
ax.set_ylabel('Frequency')


## Bar chart multiple groups


labels = df_Data["Type 1"].unique()
labels = np.sort(labels)
DDD=df_Data.groupby(["Type 1"]).mean()
DDD_attack = DDD["Attack"]
DDD_defense = DDD["Defense"]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, DDD_attack, width, label='Attack')
rects2 = ax.bar(x + width/2, DDD_defense, width, label='Defense')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores attack and defense')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation='vertical')
ax.legend()
#def autolabel(rects):
#    """Attach a text label above each bar in *rects*, displaying its height."""
#    for rect in rects:
#        height = rect.get_height()
        #ax.annotate('{}'.format(height),
                    #xy=(rect.get_x() + rect.get_width() / 2, height),
                    #xytext=(0, 3),  # 3 points vertical offset
                    #textcoords="offset points",
                    #ha='center', va='bottom')
#autolabel(rects1)
#autolabel(rects2)
fig.tight_layout()
plt.show()





## Box plots


fig, ax = plt.subplots()

# basic boxplot
ax.boxplot(df_Data["Attack"])
ax.set_title('Pokemon attack')



## Multiple box plots, violin plots

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

data = [df_Data["Attack"], df_Data["Defense"], df_Data["HP"]]



# plot violin plot
axs[0].violinplot(data,
                  showmeans=False,
                  showmedians=True)
axs[0].set_title('Violin plot') 
axs[0].set_xticks([1,2, 3])
axs[0].set_xticklabels(["Attack", "Defense", "HP"])
 
# plot box plot
axs[1].boxplot(data,labels = ["Attack", "Defense", "HP"])
axs[1].set_title('Box plot')

for ax in axs:
    ax.yaxis.grid(True)
    ax.set_ylabel('Observed values')

plt.show() 





## correlation matrix
fig, axs = plt.subplots()
corr = df_Data.corr() # Calculates correlation matrix
cax=axs.matshow(corr)
axs.set_xticks(np.arange(len(corr.columns)))
axs.set_yticks(np.arange(len(corr.columns)))
axs.set_xticklabels(corr.columns,rotation=90, fontsize=10)
axs.set_yticklabels(corr.columns,fontsize=10)
fig.colorbar(cax)



## plot multiple sub-figures

plot_counter = 0
fig, axs = plt.subplots(3, 6, sharey=True, tight_layout=False, figsize=(20, 10))
axs = axs.flatten()

for iii in (df_Data["Type 1"].value_counts().index):
  print(iii)
  marker = []
  marker = df_Data[df_Data["Type 1"] == iii]
  axs[plot_counter].hist(marker["Attack"])
  #axs[plot_counter].set_title('Attack by type')
  axs[plot_counter].set_xlabel(iii)
  axs[plot_counter].set_ylabel("Count")
  plot_counter += 1


## Save figures

plt.savefig('test.png')
plt.savefig('test2.pdf')
plt.savefig('test3.svg')    
plt.savefig('test4.png', dpi=600)  