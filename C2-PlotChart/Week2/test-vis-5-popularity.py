import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

languages = ["Python", "SQL", "Java", "C++", "Javascript"]
popularity = [56, 39, 34, 34, 29]
pos = np.arange(len(languages))

plt.figure()

bars = plt.bar(pos, popularity, align="center", linewidth=0, color='lightslategrey')
bars[0].set_color("#1F77B4")
plt.xticks(pos, languages, alpha=0.8)
# plt.ylabel("% Popularity", alpha=0.8)
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

for spine in plt.gca().spines.values():
    spine.set_visible(False)

for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', ha='center', color='w', fontsize=11)

plt.show()
