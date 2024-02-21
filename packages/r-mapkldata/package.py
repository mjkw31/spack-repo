# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapkldata(RPackage):
	"""Gene expression data for testing of the package mAPKL.

	Gene expression data from a breast cancer study published by Turashvili et al. in 2007, provided as an eSet.
	"""
	
	bioc = "mAPKLData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/mAPKLData_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/mAPKLData/mAPKLData_1.34.0.tar.gz"]

	version("1.34.0", md5="ce6399a1c853cb4e78de226347c3dc5d")

	depends_on("r@3.2:", type=("build", "run"))

	# experiment