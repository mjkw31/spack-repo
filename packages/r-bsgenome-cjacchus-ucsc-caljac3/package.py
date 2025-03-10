# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCjacchusUcscCaljac3(RPackage):
	"""Full genome sequences for Callithrix jacchus (UCSC version calJac3)

	Full genome sequences for Callithrix jacchus (Marmoset) as provided by UCSC (calJac3, Mar. 2009) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Cjacchus.UCSC.calJac3" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Cjacchus.UCSC.calJac3_1.4.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Cjacchus.UCSC.calJac3/BSgenome.Cjacchus.UCSC.calJac3_1.4.2.tar.gz"]

	version("1.4.2", md5="41f927aa0d6ffbdaa6ad93c9135409e6", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Cjacchus.UCSC.calJac3_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation