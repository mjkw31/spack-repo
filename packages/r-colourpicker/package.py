# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColourpicker(RPackage):
	"""A Colour Picker Tool for Shiny and for Selecting Colours in Plots.

	A colour picker that can be used as an input in 'Shiny' apps or Rmarkdown
	documents. The colour picker supports alpha opacity, custom colour
	palettes, and many more options. A Plot Colour Helper tool is available as
	an 'RStudio' Addin, which helps you pick colours to use in your plots. A
	more generic Colour Picker 'RStudio' Addin is also provided to let you
	select colours to use in your R code."""

	cran = "colourpicker"

	version("1.3.0", md5="e8d6b8cb5a3316250a6edba9f1d7025b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets@0.7:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-shiny@0.11.1:", type=("build", "run"))
	depends_on("r-shinyjs@2:", type=("build", "run"))
