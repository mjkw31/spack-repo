# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycomm(RPackage):
	"""Data Modification and Analysis for Communication Research

	Provides convenience functions for common data
    modification and analysis tasks in communication research. This
    includes functions for univariate and bivariate data analysis, index
    generation and reliability computation, and intercoder reliability
    tests. All functions follow the style and syntax of the tidyverse, and
    are construed to perform their computations on multiple variables at
    once. Functions for univariate and bivariate data analysis comprise
    summary statistics for continuous and categorical variables, as well
    as several tests of bivariate association including effect sizes.
    Functions for data modification comprise index generation and
    automated reliability analysis of index variables. Functions for
    intercoder reliability comprise tests of several intercoder
    reliability estimates, including simple and mean pairwise percent
    agreement, Krippendorff's Alpha (Krippendorff 2004, ISBN:
    9780761915454), and various Kappa coefficients (Brennan & Prediger
    1981 <doi: 10.1177/001316448104100307>; Cohen 1960 <doi:
    10.1177/001316446002000104>; Fleiss 1971 <doi: 10.1037/h0031619>).
	"""
	
	homepage = "https://joon-e.github.io/tidycomm/"
	cran = "tidycomm" 

	version("0.2.1", md5="6435c87734c55851eebb0f440d2d7418")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
