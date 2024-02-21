# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpa(RPackage):
	"""An Implementation of Ordinal Pattern Analysis

	Quantifies hypothesis to data fit for repeated measures 
	and longitudinal data, as described by Thorngate (1987) 
	<doi:10.1016/S0166-4115(08)60083-7> and Grice et al., (2015) 
	<doi:10.1177/2158244015604192>. Hypothesis and data are encoded as
	pairwise relative orderings which are then compared to determine the
	percentage of orderings in the data that are matched by the hypothesis.
	"""
	
	homepage = "https://github.com/timbeechey/opa"
	cran = "opa"

	version("0.8.1", md5="377f70a6fa4f3721afe4cd440c40abad")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
