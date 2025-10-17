import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig, axes = plt.subplots(1, 2, figsize=(85,5))

sns.stripolt('class',
              y='age',
              data=titanic,
              ax=axes[0])

sns.swarmplot('class',
              y='age',
              data=titanic,
              ax=axes[1],
              hue='class',
              size=4)

axes[0].set_title('Strip Plot')
axes[0].set_title('Swarm Plot')

plt.show()