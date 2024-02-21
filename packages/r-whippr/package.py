# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhippr(RPackage):
	"""Tools for Manipulating Gas Exchange Data

	Set of tools for manipulating gas exchange data from cardiopulmonary exercise testing.
	"""
	
	homepage = "https://github.com/fmmattioni/whippr"
	cran = "whippr" 

	version("0.1.2", md5="1d6d892f13c095e2d238a286d99b4ea7")

	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
	depends_on("r-broom@0.7:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-patchwork@1.0.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-nlstools", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
