# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClidamonger(RPackage):
	"""Monthly Climate Data for Germany, Usable for Heating and Cooling
Calculations

	This data package contains monthly climate data for Germany, it can be used for heating and 
    cooling calculations (external temperature, heating / cooling days, solar radiation).
	"""
	
	homepage = "https://github.com/IWUGERMANY/clidamonger"
	cran = "clidamonger" 

	version("1.0.0", md5="3db77f2ccf6ca4ab20e3ee159cb27a5c")

	depends_on("r@3.5:", type=("build", "run"))
