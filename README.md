# Zero-Carbon-Fly Decision-making Website




----
<div align="center"><img src="doc/assets/logo_colorful.png" alt="carbon emission" width="70%" />

<div align="center"><img src="doc/assets/cover_image_carbon project.png" alt="carbon emission" width="70%" />



<p><div align="center">Source: Mackincey, 2021</div></p>



---

### Mission

Zero-Carbon-Fly **aims to influence individuals’ travel behaviors and commit to climate actions through providing a net-zero-carbon-oriented travel pattern decision platform. How to internalize environmental externality by presenting carbon costs and guide users to decide on low carbon travel patterns**

Climate change has become a crucial issue in contemporary society. The US has pledged to achieve carbon neutrality by 2050, with a 2030 emissions target to be announced shortly. To meet the 2015 Paris Agreement, global greenhouse gas emissions need to be cut by 25– 50% over the next decade.

According to the U.S. Greenhouse Gas Emissions and Sinks report by EPA, the primary source of greenhouse gas emissions in the United States is Transportation, which composed 29 percent of 2019 greenhouse gas emissions.

Among all the travel patterns, air travel is the fastest-growing source of carbon emissions and emits the largest greenhouse gas. If the costs of environmental damage were reflected in flight ticket prices through effective carbon pricing, it would make other travel patterns, such as buses and trains, look a whole lot more attractive (Deutsche Welle, 2021). Additionally, **air travelers said they are willing to pay more for carbon-neutral tickets** with fliers aged 18 to 34 willing to pay the most, according to Mckinsey & Company’s research.

----
### Repo Organization

The repository is organized as follows:
```
+-- ZeroCarbonFly
|   +-- App.py
|   +-- Kayak.py
|   +-- Tests.py
+-- doc
|   +-- Design Specification.md
|   +-- Software Design.md
|   +-- Tech Review.pptx
|   +-- Final Presentation.pptx
+-- example
|   +-- ZeroCarbonFly_example.py
|   +-- Demo.mp4
|   +-- Example 1.jpeg
|   +-- Example 2.jpeg
+-- LICENSE
+-- README.md
```
----

### Dataset

This website will crawl data from flight ticket platform, KAYAK (www.kayak.com), and 
visualize the zero-carbon potentials and benefits for travellers.

----

### Software requirment (need confirm after finish all modules)

**All the required software is open source.**  The implementation was done using the following language and packages.  

**Programming language:**   
Python version 2.7  ([https://www.python.org/](https://www.python.org/))

**Python packages needed:**
- NumPy 1.10.4
- pandas 0.18.0
- matplotlib 1.5.1
- ipywidgets 4.1.1
- Jupyter 1.0.0
- Streamlit 1.2.0

----


### License information

Zero-Carbon-fly website is licensed under the MIT License, a short and simple permissive license with conditions only requiring preservation of copyright and license notices. The objective behind this choice of licensing is to make the content reproducible and make it useful for as many people as possible. 
[License](https://github.com/Zero-Carbon-Travel-Project/project/blob/c2f8a03c0ff3464a089fcf982638e5acd5e0d7c1/LICENSE)

----

### Set Up Locally
For the quickest introduction to ZeroCarbonFly, close the repository to your local computer. Navigate to the corresponding directory where the repo is saved, then navigate to the ZeroCarbonFly folder, then run the following command in your Windows Terminal.

```python
pip install --upgrade streamlit
streamlit run App.py
```
----

### Folder Contents and Repository structure

There are three main folders in this platform:

**[doc](https://github.com/Zero-Carbon-Travel-Project/project/tree/main/doc)** - 
Contains the project documentation files and references that are used to build this platform.

**[ZeroCarbonFly](https://github.com/Zero-Carbon-Travel-Project/project/tree/main/ZeroCarbonFly)** - 
Contains the main python modules for data crawling, unit tests, and website.

INTRODUCE all details file
-  `ZeroCarbonFly.py`: A functions that can be used to crawl data from flight ticket platfrom and calcuate carbon emission and pricing for visualizing in website.
-  `Website.py`: A python module for our ZeroCarbonFly website. 

**[ZeroCarbonFly/tests](website link)** -  Contains unit tests for each of the modules.

**[ZeroCarbonFly/sample_website](website link)** - Contains sample website from an demo data input for demonstrating the website features.

**[example](https://github.com/Zero-Carbon-Travel-Project/project/tree/main/example)** - 
Contains instruction to use our website.


### Acknowledgements
Thanks to Dr. David Beck and Anant Mittal at the University of Washington for their guidance and feedback in the development of this website.
