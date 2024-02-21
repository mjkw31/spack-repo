# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardinalworkflows(RPackage):
	"""Datasets and workflows for the Cardinal mass spectrometry imaging package

	Datasets and workflows for Cardinal: DESI and MALDI examples including pig fetus, cardinal painting, and human RCC.
	"""
	
	bioc = "CardinalWorkflows" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/CardinalWorkflows_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/CardinalWorkflows/CardinalWorkflows_1.34.0.tar.gz"]

	version("1.34.0", md5="54c51a2ec2f20f96ad9e60c16eeb2ccb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cardinal", type=("build", "run"))

	# experiment