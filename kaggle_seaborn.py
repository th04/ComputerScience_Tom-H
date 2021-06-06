import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

fifa_filepath = "input/fifa.csv"
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

fifa_data.head()

plt.figure(figsize=(16,6))
sns.lineplot(data=fifa_data)