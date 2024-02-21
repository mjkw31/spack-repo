# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeacarb(RPackage):
	"""Seawater Carbonate Chemistry

	Calculates parameters of the seawater carbonate system and assists the design of ocean acidification perturbation experiments.
	"""
	
	homepage = "https://CRAN.R-project.org/package=seacarb"
	cran = "seacarb" 

	version("3.3.2", md5="51a63201d8e07bdf07781a723f224010")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-oce", type=("build", "run"))
	depends_on("r-gsw", type=("build", "run"))
	depends_on("r-solvesaphe", type=("build", "run"))
