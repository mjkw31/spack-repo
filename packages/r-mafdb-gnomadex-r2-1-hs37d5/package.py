# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMafdbGnomadexR21Hs37d5(RPackage):
	"""Minor allele frequency data from gnomAD exomes release 2.1 for hs37d5

	Store minor allele frequency data from the Genome Aggregation Database (gnomAD exomes release 2.1) for the human genome version hs37d5.
	"""
	
	bioc = "MafDb.gnomADex.r2.1.hs37d5" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/MafDb.gnomADex.r2.1.hs37d5_3.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/MafDb.gnomADex.r2.1.hs37d5/MafDb.gnomADex.r2.1.hs37d5_3.10.0.tar.gz"]

	version("3.10.0", md5="6ca4d742571687a13906d99cea2dbf1f", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/MafDb.gnomADex.r2.1.hs37d5_3.10.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicscores@1.9.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

	# annotation