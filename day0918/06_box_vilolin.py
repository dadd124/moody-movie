import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

