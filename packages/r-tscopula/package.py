# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTscopula(RPackage):
	"""Time Series Copula Models

	Functions for the analysis of time series using copula models.  
    The package is based on methodology described in the following references.
    McNeil, A.J. (2021) <doi:10.3390/risks9010014>,
    Bladt, M., & McNeil, A.J. (2021) <doi:10.1016/j.ecosta.2021.07.004>,
    Bladt, M., & McNeil, A.J. (2021) <arXiv:2107.00960>.
	"""
	
	cran = "tscopula" 

	version("0.3.1", md5="9a514c598afeb572b590af1c167a7f77")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-fkf", type=("build", "run"))
	depends_on("r-ltsa", type=("build", "run"))
	depends_on("r-rvinecopulib", type=("build", "run"))
	depends_on("r-arfima", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-kdensity", type=("build", "run"))
