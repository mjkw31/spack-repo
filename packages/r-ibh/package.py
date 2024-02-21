# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbh(RPackage):
	"""Interaction Based Homogeneity for Evaluating Gene Lists

	This package contains methods for calculating Interaction Based Homogeneity to evaluate fitness of gene lists to an interaction network which is useful for evaluation of clustering results and gene list analysis. BioGRID interactions are used in the calculation. The user can also provide their own interactions.
	"""
	
	bioc = "ibh" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ibh_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ibh/ibh_1.50.0.tar.gz"]

	version("1.50.0", md5="3c87bb1083990548eb09c4e43459ba1f")

	depends_on("r-simpintlists", type=("build", "run"))
