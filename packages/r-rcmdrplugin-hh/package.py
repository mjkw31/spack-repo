# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginHh(RPackage):
	"""Rcmdr Support for the HH Package

	Rcmdr menu support for many of the functions in the HH package.
        The focus is on menu items for functions we use in our introductory
        courses.
	"""
	
	cran = "RcmdrPlugin.HH" 

	version("1.1-47", md5="53e0efb1d4b68507b1fb4ca1dc4ec5ca")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-hh", type=("build", "run"))
	depends_on("r-rcmdr@2.0.0:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
