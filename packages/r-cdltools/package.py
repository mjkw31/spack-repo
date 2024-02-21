# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdltools(RPackage):
	"""Tools to Download and Work with USDA Cropscape Data

	Downloads USDA National Agricultural Statistics Service (NASS) 
    cropscape data for a specified state. Utilities for fips, abbreviation, 
    and name conversion are also provided. Full functionality requires an 
    internet connection, but data sets can be cached for later off-line use.
	"""
	
	homepage = "https://www.github.com/jlisic/cdlTools"
	cran = "cdlTools" 

	version("0.15", md5="2075006087e4d353a036275e3ff7c2bd")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
