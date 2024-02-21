# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuncharts(RPackage):
	"""Functional Control Charts

	Provides functional control charts 
    for statistical process monitoring of functional data, 
    using the methods of Capezza et al. (2020) <doi:10.1002/asmb.2507> and 
    Centofanti et al. (2021) <doi:10.1080/00401706.2020.1753581>.
    The package is thoroughly illustrated in the paper of 
    Capezza et al (2023) <doi:10.1080/00224065.2023.2219012>.
	"""
	
	homepage = "https://github.com/unina-sfere/funcharts"
	cran = "funcharts" 

	version("1.3.2", md5="36a56daab4eee7c67fea417c3f9e908d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-roahd", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
