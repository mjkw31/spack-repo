# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimstatespace(RPackage):
	"""Simulate Data from State Space Models

	Provides a streamlined and user-friendly framework
    for simulating data in state space models,
    particularly when the number of subjects/units (n) exceeds one,
    a scenario commonly encountered in social and behavioral sciences.
    For an introduction to state space models in social and behavioral sciences,
    refer to Chow, Ho, Hamaker, and Dolan (2010) <doi:10.1080/10705511003661553>.
	"""
	
	homepage = "https://github.com/jeksterslab/simStateSpace"
	cran = "simStateSpace" 

	version("1.1.0", md5="32dc70cfb9bb140f19da4d77d7c7b269")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
