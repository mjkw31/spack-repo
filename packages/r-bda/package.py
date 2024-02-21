# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBda(RPackage):
	"""Binned Data Analysis

	Algorithms developed for binned data analysis,
  gene expression data analysis and
  measurement error models for ordinal data analysis. 
	"""
	
	cran = "bda" 

	version("17.1.2", md5="8ee95a97ffd7ed318c6a299e6ac69049")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
