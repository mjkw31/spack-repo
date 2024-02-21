# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusrank(RPackage):
	"""Wilcoxon Rank Tests for Clustered Data

	Non-parametric tests (Wilcoxon rank sum test and Wilcoxon signed rank test)
       for clustered data documented in
       Jiang et. al (2020) <doi:10.18637/jss.v096.i06>.
	"""
	
	homepage = "https://github.com/wenjie2wang/clusrank"
	cran = "clusrank" 

	version("1.0-3", md5="4a553c35adc14218ce637c8731b17527")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
