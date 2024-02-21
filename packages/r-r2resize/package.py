# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2resize(RPackage):
	"""In-Text Resizer for Images, Tables and Fancy Resizable
Containers in 'Shiny', 'Rmarkdown' and 'Quarto' Documents

	Automatic resizing toolbar for containers, images and tables. Most suitable to include resize functionality in 'Markdown', 'Rmarkdown' and 'Quarto' documents.
	"""
	
	homepage = "https://r2resize.obi.obianom.com"
	cran = "r2resize" 

	version("1.8", md5="5372b1e2f39d80dc67a80049de66d61c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-nextgenshinyapps", type=("build", "run"))
