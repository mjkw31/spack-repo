# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgparallel(RPackage):
	"""Variations of Parallel Coordinate Plots for Categorical Data

	Create hammock plots, parallel sets, and common angle plots
    with 'ggplot2'.
	"""
	
	homepage = "https://github.com/heike/ggparallel/"
	cran = "ggparallel" 

	version("0.3.0", md5="098d67cd21ff7e748b8ae1d6cccbe93b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-plyr@1.8.9:", type=("build", "run"))
