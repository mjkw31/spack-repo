# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFirst(RPackage):
	"""Factor Importance Ranking and Selection using Total Indices

	A model-independent factor importance ranking and selection procedure that is based on total Sobol' indices. Please see Huang and Joseph (2024) <arXiv:2401.00800>. This research is supported by U.S. National Science Foundation grants DMS-2310637 and DMREF-1921873.
	"""
	
	cran = "first" 

	version("1.0", md5="44f3a69778e7b51dcce0fbab1a00495a")

	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-twinning", type=("build", "run"))
