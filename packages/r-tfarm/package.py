# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfarm(RPackage):
	"""Transcription Factors Association Rules Miner

	It searches for relevant associations of transcription factors with a transcription factor target, in specific genomic regions. It also allows to evaluate the Importance Index distribution of transcription factors (and combinations of transcription factors) in association rules.
	"""
	
	bioc = "TFARM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TFARM_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TFARM/TFARM_1.24.0.tar.gz"]

	version("1.24.0", md5="bf2876d47da6baa42642dc5492ef7a94")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
