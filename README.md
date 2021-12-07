# Zero-Carbon Travel Patterns Decision-making Platform


----
<img src="doc/cover image_carbon project.png" height="250" width="250" align=center>

source: Mackincey, 2021

---

### Mission

This project **aims to influence individuals’ travel behaviors and commit to climate actions through providing a net-zero-carbon-oriented travel pattern decision platform. How to internalize environmental externality by presenting carbon costs and guide users to decide on low carbon travel patterns**


Climate change has become a crucial issue in contemporary society. The US has pledged to achieve carbon neutrality by 2050, with a 2030 emissions target to be announced shortly. To meet the 2015 Paris Agreement, global greenhouse gas emissions need to be cut by 25– 50% over the next decade.

According to the U.S. Greenhouse Gas Emissions and Sinks report by EPA, the primary source of greenhouse gas emissions in the United States is Transportation, which composed 29 percent of 2019 greenhouse gas emissions.

Among all the travel patterns, air travel is the fastest-growing source of carbon emissions and emits the largest greenhouse gas. If the costs of environmental damage were reflected in flight ticket prices through effective carbon pricing, it would make other travel patterns, such as buses and trains, look a whole lot more attractive (Deutsche Welle, 2021). Additionally, **air travelers said they are willing to pay more for carbon-neutral tickets** with fliers aged 18 to 34 willing to pay the most, according to Mckinsey & Company’s research.

----

### Dataset

This platform has two main steps to collect data.

1. CRAWLING DATA PROCESS

We could start from crawling data we need from flight ticket platforms. Here, we will focus on the KAYAK (www.kayak.com). For example, when a user requests the two adult tickets from Seattle (SEA) to Los Angeles (LAX), a round trip (2021-12-03 & 2021-12-13), business class, the link for the request will be :

https://www.kayak.com/flights/SEA-LAX/2021-12-03/2021-12-13/business/2adults

We could send the link and receive data from the KAYAK, which includes almost all the data we need (figure X). Then we generate the result dataframe and do data preprocessing, including data cleaning, filtering, renaming, etc.

2. CARBON


### Software and License information

INPUT Repository Structure after finish this project

LegTextScraper primarily uses a Python-based web browser automation tool, [Selenium](https://www.selenium.dev), to conduct webscraping. This requires a specific browser and browser driver to work properly. The package is built using Google Chrome.

- Python = 3.7
- [Google Chrome](https://www.google.com/chrome/)  
- [Chrome Driver](https://chromedriver.chromium.org/downloads)

To check your installed Chrome version and to download the appropriate Chrome Driver, follow these instructions:
1. Open Google Chrome
2. At the top right corner of the browser, click the settings tab (three vertical dots ⋮)
3. Navigate down to Help > About Google Chrome
4. Your Google Chrome version is listed on the top of the page. For example:

<img src="doc/readme_chrome.png">

5. Find the [Chrome Driver](https://chromedriver.chromium.org/downloads) that corresponds to your version and save it to your local drive



### Quick Start
For the quickest introduction to savvy, run the file [`savvy_driver.ipynb`](http://nbviewer.jupyter.org/github/houghb/savvy/blob/master/savvy_driver.ipynb) in a Jupyter notebook.

Alternatively, install savvy using setup.py (see the documentation for details), then run the following in a Jupyter notebook.  The Jupyter notebook is required for interactive widgets to work, but the core plotting functionality can also be run from the command line and Bokeh will generate html figures if preferred (see the Bokeh documentation for instructions).
```python
import copy

from bokeh.plotting import show, output_notebook
import os.path as op

import savvy
import savvy.data_processing as dp
import savvy.interactive_plots as ip
from savvy.plotting import make_plot, make_second_order_heatmap
import savvy.network_tools as nt

output_notebook()

# path to sample data files
path = op.join(savvy.__path__[0], 'sample_data_files/')

# process the data files and store their pandas dataframes in a dictionary
sa_dict = dp.get_sa_data(path)

# create interactive radial plots (or bar charts if few features) for ST and S1
ip.interact_with_plot_all_outputs(sa_dict)

# Plot heat maps of S2 indices for all your analysis files
ip.plot_all_second_order(sa_dict, top=5, mirror=True)

# Display a network plot of the second order interactions
# with first or total order sensitivity indices
# (set inline to false for an interactive window)
sa_dict_net = copy.deepcopy(sa_dict)
g = nt.build_graph(sa_dict_net['sample-output1'], sens='ST', top=40,
                   min_sens=0.01, edge_cutoff=0.0)
nt.plot_network_circle(g, inline=True)
```


LegTextScraper is installed using the command line and is best used with a virtual environment due to its dependencies.

1. Open your choice of terminal (e.g., Terminal (MacOS) or [Ubuntu 20.04 LTS](https://www.microsoft.com/en-us/p/ubuntu-2004-lts/9n6svws3rx71?activetab=pivot:overviewtab) (Windows))
2. Clone the repoistory using `git clone https://github.com/ka-chang/LegTextScraper.git`
3. Change to the LegTextScraper repository using `cd LegTextScraper`
4. Set up a new virtual environment using `conda create –n legtextscraper python=3.7`
5. Activate the legtextscraper virtual environment with `conda activate legtextscraper`
6. Install package requirements using `pip3 install –r requirements.txt`


----

### Summary of Folder Contents

**[savvy_driver.ipynb](https://github.com/houghb/savvy/blob/master/savvy_driver.ipynb)** - This is a Jupyter Notebook that is the driver for this package and can be used to create the interactive plots.

**[doc](https://github.com/houghb/savvy/tree/master/doc)** - Contains the project documentation files that are used to build the documentation at readthedocs.org.

**[doc/images](https://github.com/houghb/savvy/tree/master/doc/images)** - Contains images of sample plots and the package structure.

**[savvy](https://github.com/houghb/savvy/tree/master/savvy)** - Contains modules to visualize and generate the sensitivity analysis results.

-  `sensitivity_tools.py`: A wrapper of some SALib functions that can be used to generate sensitivity analysis results on your own models for visualizing in savvy.
- `data_processing.py`: Reads, cleans, and reformats the results.
- `plotting.py`: Plots 1st and total order sensitivity data as a radial plot and 2nd order data as a heat map.
- `interactive_plots.py`: Allows for user interaction with the plots created in `plotting.py`.
- `network_tools.py`: Creates a graph of the sensitivity data and displays it, but requires graph-tool which may not be available to all users.

**[savvy/tests](https://github.com/houghb/savvy/tree/master/savvy/tests)** -  Contains unit tests for each of the modules.

**[savvy/sample_data_files](https://github.com/houghb/savvy/tree/master/savvy/sample_data_files)** - Contains sample sensitivity analysis results from a Sobol sensitivity analysis using SALib that are used for unit testing and for demonstrating the package features.

----
### Repository structure

INPUT Repository Structure after finish this project

The package is organized as follows:





The `ZeroCarbonFly` directory includes a `states` module, unit tests in `test`, and a `dashboard_helper` function script. Data relevant to dashboard and the states module are included in `data` directory. The `examples` directory provides example Jupyter notebooks that can help new users learn the ways LegTextScraper organizes scraping and processing. A Plotly Dash dashboard can run locally through the `app.py` file (see [Dashboard](https://github.com/ka-chang/LegTextScraper/blob/main/README.md#dashboard) section below for details.




### Acknowledgements
Thanks to Dr. David Beck and Anant Mittal at the University of Washington for their guidance and feedback in the development of this platform.