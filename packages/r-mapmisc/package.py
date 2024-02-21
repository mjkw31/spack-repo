# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapmisc(RPackage):
	"""Utilities for Producing Maps

	Provides a minimal, light-weight set of tools for producing nice looking maps in R, with support for map projections.  See Brown (2016) <doi:10.32614/RJ-2016-005>.
	"""
	
	cran = "mapmisc" 

	version("2.0.6", md5="f1c83cd041e58a743ae22663c35d79d6")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
