# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplus2r(RPackage):
	"""Supplemental S-PLUS Functionality in R

	Currently there are many functions in S-PLUS that are
  missing in R. To facilitate the conversion of S-PLUS packages to R packages,
  this package provides some missing S-PLUS functionality in R.
	"""
	
	homepage = "https://github.com/spkaluzny/splus2r"
	cran = "splus2R" 

	version("1.3-4", md5="fd76b15d234696e010c1dce71911ae69")

	depends_on("r@2.7.2:", type=("build", "run"))
