# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeor(RPackage):
	"""Analysis of Geostatistical Data.

	Geostatistical analysis including variogram-based, likelihood-based and
	Bayesian methods. Software companion for Diggle and Ribeiro (2007)
	<doi:10.1007/978-0-387-48536-2>."""

	cran = "geoR"

	version("1.9-3", md5="e23847959f76f0987970bf11c47661d1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
