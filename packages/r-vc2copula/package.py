# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVc2copula(RPackage):
	"""Extend the 'copula' Package with Families and Models from
'VineCopula'

	Provides new classes for (rotated) BB1, BB6, BB7, BB8, and 
  Tawn copulas, extends the existing Gumbel and Clayton families with 
  rotations, and allows to set up a vine copula model using the 'copula' API.
  Corresponding objects from the 'VineCopula' API can easily be converted.
	"""
	
	homepage = "https://github.com/tnagler/VC2copula"
	cran = "VC2copula" 

	version("0.1.4", md5="8e1dd1b6e784089e79009b74794cb86e")

	depends_on("r-copula@1.1.2:", type=("build", "run"))
	depends_on("r-vinecopula", type=("build", "run"))
