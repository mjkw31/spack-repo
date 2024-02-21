# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGangenerativedata(RPackage):
	"""Generate Generative Data for a Data Source

	Generative Adversarial Networks are applied to generate generative data for a data source. A generative model consisting of a generator and a discriminator network is trained. In iterated training steps the distribution of generated data is converging to that of the data source. Direct applications of generative data are the created functions for data classifying and missing data completion. Reference: Goodfellow et al. (2014) <arXiv:1406.2661v1>.
	"""
	
	cran = "ganGenerativeData"

	version("1.5.6", md5="78c9cb94ac49e9a0180d6ac0e795d33b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tensorflow@2:", type=("build", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
