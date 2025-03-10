# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylation27kDb(RPackage):
	"""Illumina Illumina Human Methylation 27k annotation data (chip IlluminaHumanMethylation27k)

	Illumina Illumina Human Methylation 27k annotation data (chip IlluminaHumanMethylation27k) assembled using data from public repositories
	"""
	
	bioc = "IlluminaHumanMethylation27k.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/IlluminaHumanMethylation27k.db_1.4.8.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/IlluminaHumanMethylation27k.db/IlluminaHumanMethylation27k.db_1.4.8.tar.gz"]

	version("1.4.8", md5="70586bda9db01d598723bb439c315367")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@2.4.5:", type=("build", "run"))

	# annotation