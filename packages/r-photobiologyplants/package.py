# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologyplants(RPackage):
	"""Plant Photobiology Related Functions and Data

	Provides functions for quantifying visible (VIS) and ultraviolet
    (UV) radiation in relation to the photoreceptors Phytochromes,
    Cryptochromes, and UVR8 which are present in plants. It also includes data 
    sets on the optical properties of plants. Part of the 'r4photobiology' 
    suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://docs.r4photobiology.info/photobiologyPlants/"
	cran = "photobiologyPlants" 

	version("0.4.3", md5="99d38e90390fe5e1e924beae59ab08fa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-photobiology@0.10.15:", type=("build", "run"))
	depends_on("r-photobiologywavebands@0.5.1:", type=("build", "run"))
