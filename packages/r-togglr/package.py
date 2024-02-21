# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTogglr(RPackage):
	"""'Toggl.com' Api for 'Rstudio'

	Use the <https://toggl.com> time tracker api through R.
	"""
	
	homepage = "https://github.com/ThinkR-open/togglr"
	cran = "togglr" 

	version("0.1.99", md5="b3e0b376ab11a203cc19bb26e391c8ad")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
