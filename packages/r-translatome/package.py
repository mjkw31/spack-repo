# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTranslatome(RPackage):
	"""Comparison between multiple levels of gene expression

	Detection of differentially expressed genes (DEGs) from the comparison of two biological conditions (treated vs. untreated, diseased vs. normal, mutant vs. wild-type) among different levels of gene expression (transcriptome ,translatome, proteome), using several statistical methods: Rank Product, Translational Efficiency, t-test, Limma, ANOTA, DESeq, edgeR. Possibility to plot the results with scatterplots, histograms, MA plots, standard deviation (SD) plots, coefficient of variation (CV) plots. Detection of significantly enriched post-transcriptional regulatory factors (RBPs, miRNAs, etc) and Gene Ontology terms in the lists of DEGs previously identified for the two expression levels. Comparison of GO terms enriched only in one of the levels or in both. Calculation of the semantic similarity score between the lists of enriched GO terms coming from the two expression levels. Visual examination and comparison of the enriched terms with heatmaps, radar plots and barplots.
	"""
	
	bioc = "tRanslatome" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/tRanslatome_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/tRanslatome/tRanslatome_1.40.0.tar.gz"]

	version("1.40.0", md5="6dabe57675cc4250a3b38f9d309a6816")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-anota", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-rankprod", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-gosemsim", type=("build", "run"))
	depends_on("r-heatplus", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
