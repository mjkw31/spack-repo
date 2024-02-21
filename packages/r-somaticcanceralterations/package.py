# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomaticcanceralterations(RPackage):
	"""Somatic Cancer Alterations

	Collection of somatic cancer alteration datasets
	"""
	
	bioc = "SomaticCancerAlterations" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/SomaticCancerAlterations_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/SomaticCancerAlterations/SomaticCancerAlterations_1.38.0.tar.gz"]

	version("1.38.0", md5="77b2b0312705c2a9581cdf7aab591db8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

	# experiment