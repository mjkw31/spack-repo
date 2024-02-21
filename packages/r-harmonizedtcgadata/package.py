# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmonizedtcgadata(RPackage):
	"""Processed Harmonized TCGA Data of Five Selected Cancer Types

	This package contains the processed harmonized TCGA data of five cancer types used in "Tianle Ma and Aidong Zhang, Integrate Multi-omic Data Using Affinity Network Fusion (ANF) for Cancer Patient Clustering".
	"""
	
	bioc = "HarmonizedTCGAData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/HarmonizedTCGAData_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/HarmonizedTCGAData/HarmonizedTCGAData_1.24.0.tar.gz"]

	version("1.24.0", md5="f6e8f685a67152c6f382089c0e6aae01")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment