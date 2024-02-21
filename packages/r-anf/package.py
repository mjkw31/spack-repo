# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnf(RPackage):
	"""Affinity Network Fusion for Complex Patient Clustering

	This package is used for complex patient clustering by integrating multi-omic data through affinity network fusion.
	"""
	
	bioc = "ANF" 

	version("1.24.0", commit="656760dc158ce7f4ecb2ea54cf18cf0b66fe8767")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
