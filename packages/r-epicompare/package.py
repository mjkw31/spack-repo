# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpicompare(RPackage):
	"""Comparison, Benchmarking & QC of Epigenomic Datasets

	EpiCompare is used to compare and analyse epigenetic datasets for quality control and benchmarking purposes. The package outputs an HTML report consisting of three sections: (1. General metrics) Metrics on peaks (percentage of blacklisted and non-standard peaks, and peak widths) and fragments (duplication rate) of samples, (2. Peak overlap) Percentage and statistical significance of overlapping and non-overlapping peaks. Also includes upset plot and (3. Functional annotation) functional annotation (ChromHMM, ChIPseeker and enrichment analysis) of peaks. Also includes peak enrichment around TSS.
	"""
	
	homepage = "https://github.com/neurogenomics/EpiCompare"
	bioc = "EpiCompare" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/EpiCompare_1.6.4.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/EpiCompare/EpiCompare_1.6.4.tar.gz"]

	version("1.6.4", md5="29fcf20f00f1a8ab67b6c2a280834aac")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-brgenomics", type=("build", "run"))
	depends_on("r-chipseeker", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomation", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-downloadthis", type=("build", "run"))
