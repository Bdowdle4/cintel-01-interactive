# These are necessary to create your visual
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# This will add a sidebar with an interactive slider
# The slider should include the following: string id, string label, interger min, integer max, and integer for the initial value
with ui.sidebar():
    ui.input_slider("how_many_bins", "Number of Bins", 0, 400, 40)

# This will add a unique title for your visual
ui.page_opts(title="First Time Using PyShiny App with Plot", fillable=True)

# This will give you a reactive output chart
# The chart should include the following: numpy data array, number of bins, and density set to True to normalize the total area
@render.plot(alt="A histogram that displays random data distribution")
def draw_histogram():
    # If you want a specific number of points generated. 
    count_of_points: int = 245
    # This will ensure reproducibility 
    np.random.seed(444)
    # To generate random data you need np.random.randn(), since we specififed number of points generated, include that as well
    random_data_array = np.random.randn(count_of_points)
    # Using matplotlib's hist() function, create a histogram including 2 arguments and 1 parameter
    plt.hist(random_data_array, input.how_many_bins(), density=True, color= 'green')
    # IF you would like your visual to be a different color, add it after your parameter

    # IF you would like to change the font on your histogram you need to set the font dictionaries
    title_font = {'fontname': 'Comic Sans MS', 'size': '16', 'color': 'green', 'weight': 'normal',
              'verticalalignment': 'bottom'}
    axis_font = {'fontname': 'Comic Sans MS', 'size': '16', 'color' : 'green'}
    # Choose the labels for your fonts
    plt.title('Histogram of Random Data', **title_font)
    plt.xlabel('Value', **axis_font)
    plt.ylabel('Frequency', **axis_font)
