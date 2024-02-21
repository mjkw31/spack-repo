# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpir(RPackage):
	"""Tools for the Analysis of Epidemiological Data

	Tools for the analysis of epidemiological and surveillance data. Contains functions for directly and indirectly adjusting measures of disease frequency, quantifying measures of association on the basis of single or multiple strata of count data presented in a contingency table, computation of confidence intervals around incidence risk and incidence rate estimates and sample size calculations for cross-sectional, case-control and cohort studies. Surveillance tools include functions to calculate an appropriate sample size for 1- and 2-stage representative freedom surveys, functions to estimate surveillance system sensitivity and functions to support scenario tree modelling analyses.   
	"""
	
	homepage = "https://mvs.unimelb.edu.au/research/groups/veterinary-epidemiology-melbourne"
	cran = "epiR" 

	version("2.0.67", md5="4351b6186ed0150cf4e7daef835a7e0b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
