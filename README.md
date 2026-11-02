# Style guide for coding

This style guide is meant to support clear, consistent, and reproducible code in statistical projects. The goal is to make scripts easy to read, easy to maintain, and easy to share with colleagues.

The style is designed for work in R and Python, with an emphasis on transparency, structure, and good documentation of analytical steps.

Further references:
- Python style guide: https://peps.python.org/pep-0008/
- R style guide: https://google.github.io/styleguide/Rguide.html
- Tidyverse style guide: https://style.tidyverse.org/

# 1. General principles

Good code should be:
- clear and readable
- consistent across projects
- transparent about assumptions and decisions
- easy to reproduce and review
- concise without being cryptic

When in doubt, choose the option that makes the code easier for a colleague to understand quickly.

# 2. File structure and naming

## 2.1 File names

File names should be:
- lowercase
- descriptive
- separated by underscores
- machine-readable and human-readable

Use numbering for sequential steps when relevant.

Good examples:
- 01_load_data.py
- 02_clean_population_data.R
- 03_create_descriptive_tables.py

Bad examples:
- data.py
- final_version.R
- analysis_final_final.R

## 2.2 Project folder structure

Projects should use a simple and consistent folder layout.

Example:
- raw/
- code/
- data/
- text/
- documentation/
- results/

This structure makes it easier to separate inputs, scripts, outputs, and documentation.

# 3. Code layout

## 3.1 Sectioning and readability

Use commented section headers to split files into logical parts. Keep sections short and meaningful.

Example:

```python
# 1. Load data ---------------------------------------------------

# 2. Clean and transform data -----------------------------------

# 3. Create output tables ----------------------------------------
```

```r
# 1. Load data =====================================================

# 2. Clean and transform data ------------------------------------

# 3. Create output tables -----------------------------------------
```

Use consistent comment markers such as `-` and `=` to separate blocks visually.

## 3.2 Line length

Aim for a maximum of 79 characters per line when practical. This improves readability and reduces horizontal scrolling.

## 3.3 Indentation

Use one indentation level per block.

For Python, use 4 spaces.
For R, use 2 spaces or a consistent indentation style, but avoid mixing styles within the same project.

## 3.4 Blank lines

Use blank lines between logical blocks of code, but not too many. Keep the structure readable without creating visual clutter.

# 4. Naming conventions

## 4.1 Functions

Use verbs when naming functions. The name should describe the action performed.

Examples:
- load_data()
- clean_population()
- calculate_rate()
- plot_time_series()

Suggested prefixes:
- load_: read input data
- clean_: remove or standardise data issues
- transform_: reshape or recode variables
- calculate_: compute a summary or statistic
- plot_: produce a figure
- save_: write an output file

## 4.2 Objects

Use nouns or noun-like names for objects.

Examples:
- pop_data
- birth_counts
- region_codes
- result_table

For statistical work, naming should be explicit and domain-aware.

Examples:
- pop_2010
- births_total
- emigrants_2023
- moves_by_region

## 4.3 Avoid ambiguous names

Avoid names such as:
- data
- stuff
- temp
- values
- result

These are too vague and become difficult to interpret later.

# 5. Comments and documentation

Comments should explain why something is done, not simply restate what the code already says.

Good comments:
- explain a decision
- describe the purpose of a section
- document assumptions or exclusions

Avoid comments that merely repeat the code.

Example:

```python
# Exclude 2020 because the data collection was disrupted by the COVID-19 pandemic
```

This is useful because it explains context.

# 6. Python conventions

## 6.1 Assignment

Use `=` for assignment.

```python
population = 1000
```

## 6.2 Function and variable naming

Use snake_case for variables and functions.

Examples:
- clean_population_data()
- region_name
- birth_rate

## 6.3 Data structures

Prefer clear and readable structures over clever compact code.

Use list comprehensions only when they remain easy to understand. For more complex logic, prefer a regular loop.

## 6.4 Style consistency

Follow the core rules of PEP 8, especially for:
- naming
- spacing
- line length
- blank lines
- readable function definitions

# 7. R conventions

## 7.1 Assignment

Use `<-` for assignment in R.

```r
population <- 1000
```

## 7.2 Naming

Use snake_case and keep names descriptive.

Examples:
- population_data
- birth_counts
- region_codes

## 7.3 Tidyverse style

Prefer readable, pipe-based workflows when they improve clarity.

```r
population_data <- read.csv("data/population.csv") |>
  filter(year >= 2010) |>
  mutate(region = tolower(region))
```

This makes the analytical steps easier to follow.

# 8. Reproducibility and transparency

All scripts should be written to be reproducible.

This means:
- using clear paths or project-relative file locations
- documenting assumptions
- avoiding hidden dependencies
- making the workflow easy to rerun

If a script depends on a special definition, assumption, or manual correction, say so explicitly.

# 9. Output and results

Outputs should be:
- well-labelled
- easy to interpret
- saved in a consistent location
- documented in a way that makes the result understandable to others

Use consistent names for tables, plots, and reports. For example:
- 01_population_summary.csv
- plot_population_trend.png
- table_region_summary.xlsx

# 10. Practical rules to remember

- Keep code readable before clever.
- Prefer explicit names over compact ones.
- Section files into logical blocks.
- Comment the reason, not the obvious.
- Write code as if another analyst will read it next month.
- Keep outputs reproducible and transparent.

# 11. Summary

The main goal of this style guide is not perfection, but consistency. Good code should be easy to read, easy to review, and easy to reuse. By following these conventions, statistical analysis becomes more transparent, durable, and collaborative.

This guide should be used as a practical baseline for all future coding work at Statistics Norway.
