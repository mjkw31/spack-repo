# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleanupdtseq(RPackage):
	"""cleanUpdTSeq cleans up artifacts from polyadenylation sites from oligo(dT)-mediated 3' end RNA sequending data

	This package implements a Naive Bayes classifier for accurately differentiating true polyadenylation sites (pA sites) from oligo(dT)-mediated 3' end sequencing such as PAS-Seq, PolyA-Seq and RNA-Seq by filtering out false polyadenylation sites, mainly due to oligo(dT)-mediated internal priming during reverse transcription. The classifer is highly accurate and outperforms other heuristic methods.
	"""
	
	bioc = "cleanUpdTSeq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cleanUpdTSeq_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cleanUpdTSeq/cleanUpdTSeq_1.40.0.tar.gz"]

	version("1.40.0", md5="52f27e948758be1db9d6b003d69a84b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome-drerio-ucsc-danrer7", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
