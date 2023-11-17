import matplotlib.pyplot as plt
import seaborn as sns
def create_banner(df):
    lPlot = sns.lineplot(df, x='Week Ending Date', y=df.columns[2])
    # Rotate x-axis labels vertically
    lPlot.set_xticklabels(lPlot.get_xticklabels(), rotation=90, fontsize=7)
    plt.show()