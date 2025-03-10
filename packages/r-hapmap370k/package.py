# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmap370k(RPackage):
	"""Example Illumina 370k HapMap Data

	Example HapMap data from Illumina 370k BeadChips
	"""
	
	bioc = "hapmap370k" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hapmap370k_1.0.1.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hapmap370k/hapmap370k_1.0.1.tar.gz"]

	version("1.0.1", md5="569556341a45da799372aaf1012be72e")


	# annotation