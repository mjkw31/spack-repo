# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperdesign(RPackage):
	"""Design Experiments for Batches

	Distributes samples in batches while making batches
    homogeneous according to their description. Allows for an arbitrary
    number of variables, both numeric and categorical. For quality control
    it provides functions to subset a representative sample.
	"""
	
	homepage = "https://experdesign.llrs.dev"
	cran = "experDesign" 

	version("0.2.0", md5="87df9eeb3f8f547db0d084871d9f6d8b")

	depends_on("r@3.5:", type=("build", "run"))
