# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmusculusUcscMm9(RPackage):
	"""Full genome sequences for Mus musculus (UCSC version mm9)

	Full genome sequences for Mus musculus (Mouse) as provided by UCSC (mm9, Jul. 2007) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mmusculus.UCSC.mm9" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm9_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Mmusculus.UCSC.mm9/BSgenome.Mmusculus.UCSC.mm9_1.4.0.tar.gz"]

	version("1.4.0", md5="5a30ba2b4481a17e8e6979eb69eabf78", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Mmusculus.UCSC.mm9_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation