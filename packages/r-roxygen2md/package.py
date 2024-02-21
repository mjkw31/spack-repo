# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoxygen2md(RPackage):
	"""'Roxygen' to 'Markdown'

	Converts elements of 'roxygen' documentation to
    'markdown'.
	"""
	
	homepage = "https://roxygen2md.r-lib.org"
	cran = "roxygen2md" 

	version("1.0.0", md5="36a03ba61171d21f9170e30a7b102e71")

	depends_on("r-desc", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-enc", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
