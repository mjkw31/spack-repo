# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRilostat(RPackage):
	"""ILO Open Data via Ilostat Bulk Download Facility or SDMX Web
Service

	Tools to download data from the ilostat database
    <https://ilostat.ilo.org> together with search and
    manipulation utilities.
	"""
	
	homepage = "https://ilostat.github.io/Rilostat/"
	cran = "Rilostat" 

	version("1.1.8", md5="16498c5ef400a5eb9fb8cede4ed0a0ba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr@1.0.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.6:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
