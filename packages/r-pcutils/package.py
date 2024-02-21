# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcutils(RPackage):
	"""Some Useful Functions for Statistics and Visualization

	
    Offers a range of utilities and functions for everyday programming tasks. 
    1.Data Manipulation. Such as grouping and merging, column splitting, and character expansion.
    2.File Handling. Read and convert files in popular formats, including "blast", "diamond", "fasta", "gff", "gtf", and various image formats like "jpg", "png", "pdf", and "svg". 
    3.Plotting Assistance. Helpful utilities for generating color palettes, validating color formats, and adding transparency. 
    4.Statistical Analysis. Includes functions for pairwise comparisons and multiple testing corrections, 
    enabling perform statistical analyses with ease.
    5.Graph Plotting, Provides efficient tools for creating doughnut plot and multi-layered doughnut plot;
    Venn diagrams, including traditional Venn diagrams, upset plots, and flower plots; 
    Simplified functions for creating stacked bar plots, or a box plot with alphabets group for multiple comparison group.
	"""
	
	homepage = "https://github.com/Asa12138/pcutils"
	cran = "pcutils" 

	version("0.2.1", md5="8c9bbebaf2e0e7ee5eb05208f1dc43cd")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
