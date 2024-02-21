# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInformeasure(RPackage):
	"""R implementation of Information measures

	This package compiles most of the information measures currently available: mutual information, conditional mutual information, interaction information, partial information decomposition and part mutual information. All of these estimators can be used to quantify nonlinear dependence between variables in (biological regulatory) network inference. The first estimator is used to infer bivariate networks while the last four estimators are dedicated to analysis of trivariate networks.
	"""
	
	homepage = "https://github.com/chupan1218/Informeasure"
	bioc = "Informeasure" 

	version("1.12.0", commit="1dc962ff30937e83b0429b8a2085b0a8152ae0fd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
