# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScientific(RPackage):
	"""Elegant Scientific Themed Reporting for 'Markdown'

	Offers 'markdown' output formats designed with various scientific styles, allowing users to generate PDF and HTML outputs. The output has a contemporary appearance with vibrant visuals, providing numerous styles for effective highlighting. The package also includes additional features specifically tailored for front-page slides, enhancing the overall presentation and customization options. The package was created using the 'tufte' R package code as a starting point.
	"""
	
	homepage = "https://scientific.obi.obianom.com"
	cran = "scientific" 

	version("2024.0", md5="ca5b15b7cc497fc83a51b3257df2f163")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
