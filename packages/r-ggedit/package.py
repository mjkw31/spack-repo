# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgedit(RPackage):
	"""Interactive 'ggplot2' Layer and Theme Aesthetic Editor

	Interactively edit 'ggplot2' layer and theme aesthetics definitions.
	"""
	
	homepage = "https://github.com/yonicd/ggedit"
	cran = "ggedit" 

	version("0.3.1", md5="75ccee113781e4f9cb538db308806b6c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-colourpicker@0.2:", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
