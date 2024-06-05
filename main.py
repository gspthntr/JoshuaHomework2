import matplotlib.pyplot as plt
import pandas as pd
results = {num: [] for num in range(1, 7)}
df = pd.read_csv('mechanical_analysis_Dataset_B.csv')
letters = ["vo", "vv", "ao", "av", "io", "iv"]
for num in range(1, 7):
    for letter in letters:
        klass = df[(df["class"] == num) & (df["dir"] == letter)]
        dir_count = len(klass)
        results[num].append( {letter: dir_count})
print(results)

classes = list(results.keys())
labels = ['vo', 'vv', 'ao', 'av', 'io', 'iv']
values = {label: [] for label in labels}

for cls in classes:
    for item in results[cls]:
        for key in item:
            values[key].append(item[key])

fig, ax = plt.subplots(figsize=(15, 6))

bar_width = 0.135

r = range(len(classes))
positions = {label: [x + i * bar_width for x in r] for i, label in enumerate(labels)}

for label in labels:
    bars = ax.bar(positions[label], values[label], width=bar_width, label=label)
    for bar, value in zip(bars, values[label]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5, str(value),
                ha='center', va='bottom', fontsize=9)


ax.set_xlabel("Type of defect")
ax.set_ylabel("Count")
ax.set_title("Joshua's Histogram")
ax.set_xticks([r + bar_width * (len(labels) / 2) for r in range(len(classes))])
ax.set_xticklabels([f'Class {cls}' for cls in classes])
ax.legend()

plt.show()

