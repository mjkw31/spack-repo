# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCobiclust(RPackage):
	"""Biclustering via Latent Block Model Adapted to Overdispersed
Count Data

	Implementation of a probabilistic method for biclustering
    adapted to overdispersed count data. It is a Gamma-Poisson Latent Block Model.
    It also implements two selection criteria in order to select the number of
    biclusters.
	"""
	
	cran = "cobiclust" 

	version("0.1.0", md5="7a3dd8dbb5bfe44204272698d3631714")

	depends_on("r-cluster", type=("build", "run"))
