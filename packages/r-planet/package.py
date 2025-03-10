# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanet(RPackage):
	"""Placental DNA methylation analysis tools

	This package contains R functions to predict biological variables to from placnetal DNA methylation data generated from infinium arrays. This includes inferring ethnicity/ancestry, gestational age, and cell composition from placental DNA methylation array (450k/850k) data.
	"""
	
	homepage = "https://victor.rbind.io/planet"
	bioc = "planet" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/planet_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/planet/planet_1.10.0.tar.gz"]

	version("1.10.0", md5="dbd74bc4dd3583d6ebbd871b251ecd6d")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
