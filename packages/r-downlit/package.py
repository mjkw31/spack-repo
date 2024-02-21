# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDownlit(RPackage):
	"""Syntax Highlighting and Automatic Linking.

	Syntax highlighting of R code, specifically designed for the needs of
	'RMarkdown' packages like 'pkgdown', 'hugodown', and 'bookdown'. It
	includes linking of function calls to their documentation on the web, and
	automatic translation of ANSI escapes in output to the equivalent HTML."""

	cran = "downlit"

	version("0.4.3", md5="58fbf827a761ff8705006a1b4421975c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-brio", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
