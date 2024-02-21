# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfvis(RPackage):
	"""Interactive visualizations for profiling R code."""

	cran = "profvis"

	version("0.3.8", md5="2c363c19fb6cb898dd3061d9a7035def")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.3.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.4.9:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
