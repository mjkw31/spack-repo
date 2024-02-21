# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeScerevisiaeUcscSaccer3(RPackage):
	"""Saccharomyces cerevisiae (Yeast) full genome (UCSC version sacCer3)

	Saccharomyces cerevisiae (Yeast) full genome as provided by UCSC (sacCer3, April 2011) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Scerevisiae.UCSC.sacCer3" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Scerevisiae.UCSC.sacCer3_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Scerevisiae.UCSC.sacCer3/BSgenome.Scerevisiae.UCSC.sacCer3_1.4.0.tar.gz"]

	version("1.4.0", md5="7f2d8bba69c3dcebf426d9b19a6bed30", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Scerevisiae.UCSC.sacCer3_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation