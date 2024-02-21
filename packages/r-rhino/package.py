# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhino(RPackage):
	"""A Framework for Enterprise Shiny Applications

	A framework that supports creating and extending enterprise Shiny applications using best practices.
	"""
	
	homepage = "https://appsilon.github.io/rhino/"
	cran = "rhino" 

	version("1.6.0", md5="28d0baf3fcdf32e55b726300cd40e6e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-box@1.1.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lintr@3:", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-sass", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-styler", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
