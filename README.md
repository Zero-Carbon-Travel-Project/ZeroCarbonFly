# Carbon Neutral Flying Decision-Making Website


----
<img align="center" src="doc/assets/logo_colorful.png" alt="carbon emission" width="100%">

<img align="center" src="doc/assets/cover_image_carbon project.png" alt="carbon emission" width="100%">



Source: Mackincey, 2021

---

### Mission

Carbon Neutral Flying **aims to influence individuals’ travel behaviors and commit to climate actions through providing a net-zero-carbon-oriented travel pattern decision platform. How to internalize environmental externality by presenting carbon costs and guide users to decide on low carbon travel patterns**

Climate change has become a crucial issue in contemporary society. The US has pledged to achieve carbon neutrality by 2050, with a 2030 emissions target to be announced shortly. To meet the 2015 Paris Agreement, global greenhouse gas emissions need to be cut by 25– 50% over the next decade.

According to the U.S. Greenhouse Gas Emissions and Sinks report by EPA, the primary source of greenhouse gas emissions in the United States is Transportation, which composed 29 percent of 2019 greenhouse gas emissions.

Among all the travel patterns, air travel is the fastest-growing source of carbon emissions and emits the largest greenhouse gas. If the costs of environmental damage were reflected in flight ticket prices through effective carbon pricing, it would make other travel patterns, such as buses and trains, look a whole lot more attractive (Deutsche Welle, 2021). Additionally, **air travelers said they are willing to pay more for carbon-neutral tickets** with fliers aged 18 to 34 willing to pay the most, according to Mckinsey & Company’s research.

----
### Repo Organization

The repository is organized as follows:
```
├── environment.yml
├── LICENSE
├── README.md
├── doc
│   ├── Proposal.md
│   ├── Software Design.md
│   ├── Tech Review.pdf
│   ├── Final Presentation.pdf
│   ├── Carbon Calculation.ipynb
│   └── assets
├── example
│   ├── ZeroCarbonFly_Demo.mp4
│   └── User Guidance .ipynb
└── zerocarbonfly
    ├── Website.py
    ├── kayak.py
    └── assets
```
----

### Dataset

This website will crawl data from flight ticket platform, KAYAK (www.kayak.com), and visualize the zero-carbon potentials and benefits for travelers.

----

### Software requirement 

The website can only work on Linux system. If your use Windows Linux Subsystem (WSL), you need use Windows 11 or upper version of Windows. At the same time, you need follow the instruction from Microsoft to install the Google Chrome on your WSL. https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps       

**System and Software**

- Linux 
- Google Chrome for Linux 9.6

**Programming language:**

- Python version 3.8.8  ([https://www.python.org/](https://www.python.org/))

**Python packages needed**

- pandas 1.3.3
- numpy 1.20
- streamlit 1.2.0
- selenium 4.0.0 
- bs4 0.01
- pydeck 0.7.1
- altair 4.1.0

----


### License information

Zero-Carbon-fly website is licensed under the MIT License, a short and simple permissive license with conditions only requiring preservation of copyright and license notices. The objective behind this choice of licensing is to make the content reproducible and make it useful for as many people as possible. 
[License](https://github.com/Zero-Carbon-Travel-Project/project/blob/c2f8a03c0ff3464a089fcf982638e5acd5e0d7c1/LICENSE)

----

### Set Up Locally
For the quickest introduction to ZeroCarbonFly, clone the repository to your local computer. Navigate to the corresponding directory where the repo is saved, then navigate to the zerocarbonfly folder, then run the following command on your Linux.

```python
pip install --upgrade streamlit
streamlit run Website.py
```
----

### Folder Contents and Repository structure

There are three main folders in this platform:

**[doc](https://github.com/Zero-Carbon-Travel-Project/project/tree/main/doc)** - Contains the project documentation files and references that are used to build this platform.

**[zerocarbonfly](https://github.com/Zero-Carbon-Travel-Project/project/tree/main/ZeroCarbonFly)** - Contains the main python modules for data crawling and website.

INTRODUCE all details file
-  `ZeroCarbonFly.py`: A functions that can be used to crawl data from flight ticket platfrom and calcuate carbon emission and pricing for visualizing in website.
-  `Website.py`: A python module for our ZeroCarbonFly website. 

**[example](https://github.com/Zero-Carbon-Travel-Project/project/tree/main/example)** - Contains demo video and instruction to use our website.


### Acknowledgements
Thanks to Dr. David Beck and Anant Mittal at the University of Washington for their guidance and feedback in the development of this website.
