# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgiraph(RPackage):
	"""Make 'ggplot2' Graphics Interactive

	Create interactive 'ggplot2' graphics using 'htmlwidgets'.
	"""
	
	homepage = "https://davidgohel.github.io/ggiraph/"
	cran = "ggiraph"

	version("0.8.8", md5="14792a74b258d0c4fa7674fb15dcac27")

	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("libpng", type=("build", "link", "run"))
