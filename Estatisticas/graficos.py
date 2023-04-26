import matplotlib as plt
import seaborn as sns

y = [2, 6, 2, 5, 9, 1]
x = ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6']

sns.barplot(x,y)
plt.barh(x,y)

