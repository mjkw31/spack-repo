# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdrstyle(RPackage):
	"""A package with style requirements for the gDR suite

	Package fills a helper package role for whole gDR suite. It helps to support good development practices by keeping style requirements and style tests for other packages. It also contains build helpers to make all package requirements met.
	"""
	
	bioc = "gDRstyle" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gDRstyle_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gDRstyle/gDRstyle_1.0.0.tar.gz"]

	version("1.0.0", md5="473f3c2e73e05f50ec3af2b72bb18a55")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-bioccheck", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-lintr@3:", type=("build", "run"))
	depends_on("r-rcmdcheck", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
