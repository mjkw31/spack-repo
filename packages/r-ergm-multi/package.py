# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmMulti(RPackage):
	"""Fit, Simulate and Diagnose Exponential-Family Models for
Multiple or Multilayer Networks

	A set of extensions for the 'ergm' package to fit multilayer/multiplex/multirelational networks and samples of multiple networks. 'ergm.multi' is a part of the Statnet suite of packages for network analysis. See Krivitsky, Koehly, and Marcum (2020) <doi:10.1007/s11336-020-09720-7> and Krivitsky, Coletti, and Hens (2022) <doi:10.48550/arXiv.2202.03685>.
	"""
	
	homepage = "https://statnet.org"
	cran = "ergm.multi" 

	version("0.2.0", md5="75c58e9b30ee971092cb7d36d94e8c4a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-network@1.18:", type=("build", "run"))
	depends_on("r-statnet-common@4.9:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-purrr@0.3.5:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-rle@0.9.2:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
