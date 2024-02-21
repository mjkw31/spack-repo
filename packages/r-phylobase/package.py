# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylobase(RPackage):
	"""Base Package for Phylogenetic Structures and Comparative Data.

	Provides a base S4 class for comparative methods, incorporating one or more
	trees and trait data."""

	cran = "phylobase"

	version("0.8.12", md5="f2177d31af1389129d811d032bdf707a")

	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-ape@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rncl@0.6:", type=("build", "run"))
	depends_on("r-rnexml", type=("build", "run"))
