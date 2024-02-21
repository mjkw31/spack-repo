# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDropout(RPackage):
	"""Handling Incomplete Responses in Survey Data Analysis

	Offers robust tools to identify and manage incomplete responses in survey datasets, thereby enhancing the quality and reliability of research findings.
	"""
	
	homepage = "https://github.com/hendr1km/dropout"
	cran = "dropout" 

	version("2.1.0", md5="0ef2937ced7298fdb2daba09352f8c8d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
