# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorregp(RPackage):
	"""Functions and Methods for Correspondence Regression

	A collection of tools for correspondence regression, i.e. the
    correspondence analysis of the crosstabulation of a categorical variable Y
    in function of another one X, where X can in turn be made up of the
    combination of various categorical variables. Consequently, correspondence
    regression can be used to analyze the effects for a polytomous or
    multinomial outcome variable.
	"""
	
	cran = "corregp" 

	version("2.0.2", md5="7c1fede9794bdd725aef71f807663857")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
