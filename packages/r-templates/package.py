# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTemplates(RPackage):
	"""A System for Working with Templates

	Provides tools to work with template code and text in R. It aims to
    provide a simple substitution mechanism for R-expressions inside these
    templates. Templates can be written in other languages like 'SQL', can
    simply be represented by characters in R, or can themselves be R-expressions
    or functions.
	"""
	
	cran = "templates" 

	version("0.3.0", md5="435075c225cbfbb285a557342906b656")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
