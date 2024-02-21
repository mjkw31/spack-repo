# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLair(RPackage):
	"""Converting NDVI to LAI of Field, Proximal and Satellite Data

	Convert Leaf Area Index (LAI) from the Normalized Difference Vegetation Index (NDVI) using available equations from literature. 
    Detailed description of conversion equations in Bajocco et al. 2022 <doi:10.3390/rs14153554>.
	"""
	
	cran = "LAIr" 

	version("0.2.0", md5="d127cedcc1e6512405bc4fea9c872e53")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
