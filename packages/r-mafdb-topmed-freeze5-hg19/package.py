# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMafdbTopmedFreeze5Hg19(RPackage):
	"""Minor allele frequency data from TOPMed for hg19

	Store minor allele frequency data from NHLBI TOPMed for the human genome version hg19.
	"""
	
	bioc = "MafDb.TOPMed.freeze5.hg19" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/MafDb.TOPMed.freeze5.hg19_3.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/MafDb.TOPMed.freeze5.hg19/MafDb.TOPMed.freeze5.hg19_3.10.0.tar.gz"]

	version("3.10.0", md5="7fdb58eb69187ade189689da58ca6266", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/MafDb.TOPMed.freeze5.hg19_3.10.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicscores@1.9.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

	# annotation