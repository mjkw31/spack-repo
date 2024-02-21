# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYorkr(RPackage):
	"""Analyze Cricket Performances Based on Data from Cricsheet

	Analyzing performances of cricketers and cricket teams
             based on 'yaml' match data from Cricsheet <https://cricsheet.org/>.
	"""
	
	homepage = "https://github.com/tvganesh/yorkr/"
	cran = "yorkr" 

	version("0.0.41", md5="31fa531eb424975adf7edc22d31bf159")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
