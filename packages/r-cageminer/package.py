# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCageminer(RPackage):
	"""Candidate Gene Miner

	This package aims to integrate GWAS-derived SNPs and coexpression networks to mine candidate genes associated with a particular phenotype. For that, users must define a set of guide genes, which are known genes involved in the studied phenotype. Additionally, the mined candidates can be given a score that favor candidates that are hubs and/or transcription factors. The scores can then be used to rank and select the top n most promising genes for downstream experiments.
	"""
	
	homepage = "https://github.com/almeidasilvaf/cageminer"
	bioc = "cageminer" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cageminer_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cageminer/cageminer_1.8.0.tar.gz"]

	version("1.8.0", md5="02b96b12bfe145c4c9deefff49cd1015")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-bionero", type=("build", "run"))
