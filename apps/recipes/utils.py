from io import BytesIO 
import base64
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MaxNLocator

matplotlib.use('Agg')

custom_colors = ['#074343', '#e25d46', '#e2ab46', 'skyblue']

def generate_charts(recipe_names, cooking_times, difficulty_counts, ingredient_counts):
    charts = {}

    # 1. Bar chart for Recipe Name vs Cooking Time
    plt.figure(figsize=(10, 6))
    plt.bar(recipe_names, cooking_times, color='skyblue')
    plt.xlabel('Recipe Name', fontweight=700, labelpad=10)
    plt.ylabel('Cooking Time (mins)', fontweight=700, labelpad=10)
    plt.xticks(rotation=30, ha='center')
    max_time = max(cooking_times) if cooking_times else 0  
    plt.yticks(range(0, max_time + 5, 5))
    plt.tight_layout()
    charts['bar_chart'] = get_chart()

    # 2. Pie chart for Recipe Difficulty Distribution
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
       difficulty_counts.values(), 
       labels=difficulty_counts.keys(), 
       autopct='%1.1f%%', 
       startangle=140, 
       colors=custom_colors,
       wedgeprops={'edgecolor': 'black'},
    )
    for autotext in autotexts:
      autotext.set_color('white')

    plt.legend(
    wedges,
    difficulty_counts.keys(),
    title="Recipe Difficulty",
    loc="center left",
    bbox_to_anchor=(1, 1)
    )
    plt.tight_layout()
    charts['pie_chart'] = get_chart()

    # 3. Line chart for Recipes by Number of Ingredients
    plt.figure(figsize=(10, 6))
    plt.plot(recipe_names, ingredient_counts, marker='o', linestyle='-', color='orange')
    plt.xlabel('Recipe Name', fontweight=700, labelpad=10)
    plt.ylabel('Number of Ingredients', fontweight=700, labelpad=10)
    plt.xticks(ticks=range(len(recipe_names)), labels=recipe_names, rotation=30)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.tight_layout()
    charts['line_chart_ingredients'] = get_chart()

    return charts


def get_chart():
  buffer = BytesIO()         
   #create a plot with a bytesIO object as a file-like object. Set format to png
  plt.savefig(buffer, format='png')
   #set cursor to the beginning of the stream
  buffer.seek(0)
   #retrieve the content of the file
  image_png=buffer.getvalue()
   #encode the bytes-like object
  chart=base64.b64encode(image_png)
   #decode to get the string as output
  chart=chart.decode('utf-8')
   #free up the memory of buffer
  buffer.close()
  plt.close()

   #return the image/graph
  return chart