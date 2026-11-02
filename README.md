# Style Guide for Coding
This style is meant to provide the rules and conventions that I use in my coding practice. I aim for consistency as well as transparency. There will be language specifics for **R** and **Python**.

Further references can be found under [Python]([Python](https://peps.python.org/pep-0008/)), [Google-R](https://google.github.io/styleguide/Rguide.html),  [Tidyverse](https://style.tidyverse.org/)

# Files
File names use lower-case characters and underscores as seperators, so that they are machine readable. Sequential files can be numbered either with 1_..., 2_..., or if there are many files expexted 01_..., 02_..., 03_....

File names should be desciptive, e.g. human readable. 

```
# Good
01_load_data.py

# Bad
data.py
```


# Code lay-out

## Internal file structure
use commented lines of ```-``` and ```=``` to break up your file into easily readable chunks. Ideally, combine with numbering and number of comments to indicate the leel


```R
# 1. Load data ============================

## 1.1. Load population data -------------


## 1.2. Load birth counts ----------------

## 2. Combine population and birht data ===

```

## Indentation
I will use 1 tab per indentation level.


## Maximum Line length
I aim for 79 characters per line.

## Blank Lines


## Whitespace in Expression and Statements


## Naming convention

- *Functions:* usually start with a verb that describes the activity that the function executes:
    - trans_...: transform a variable into another
    - calc_...: calculate a composite measure
    - plot_...: any plotting function
    - pivot_...: reshape a data structure into another format
- *Objects*: usually use nouns to illustrate the object type
    - pop_...: population countrs, subgroups are indicated through the paranthetes (pop_2010), (pop_f), (pop_oslo)
    - births_..., deaths_..., moves_..., emigr_, immigr_...: event counts of birth, deaths, emigrations, immigrations
    - 


## R
The assignment operator ```<-``` should be used in R to assign objects.

## Python 
The assignement operator ```=``` shoudl be used to assign objects.
