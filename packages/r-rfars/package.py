# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfars(RPackage):
	"""Download and Analyze Fatal Crash Data

	Download raw data from the Fatality Analysis Reporting System and prepare it for research.
	"""
	
	homepage = "https://github.com/s87jackson/rfars"
	cran = "rfars" 

	version("0.3.0", md5="f40a41d73ff8d0e7d4a12f9bbff1c2fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sas7bdat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
