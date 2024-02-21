# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatexdiffr(RPackage):
	"""Diff 'rmarkdown' Files Using the 'latexdiff' Utility

	Produces a PDF diff of two 'rmarkdown', Sweave or TeX files,  using
	the external 'latexdiff' utility.
	"""
	
	cran = "latexdiffr"

	version("0.1.0", md5="ed5909f0edba220def3ba41c18f095ba")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
