# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeSscrofaUcscSusscr3(RPackage):
	"""Full genome sequences for Sus scrofa (UCSC version susScr3)

	Full genome sequences for Sus scrofa (Pig) as provided by UCSC (susScr3, Aug. 2011) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Sscrofa.UCSC.susScr3" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Sscrofa.UCSC.susScr3_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Sscrofa.UCSC.susScr3/BSgenome.Sscrofa.UCSC.susScr3_1.4.0.tar.gz"]

	version("1.4.0", md5="0457ca52a81c9d7ceadad5830169e6cf", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Sscrofa.UCSC.susScr3_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation