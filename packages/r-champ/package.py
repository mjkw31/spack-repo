# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChamp(RPackage):
	"""Chip Analysis Methylation Pipeline for Illumina HumanMethylation450 and
	EPIC.

	The package includes quality control metrics, a selection of
	normalization methods and novel methods to identify differentially
	methylated regions and to highlight copy number alterations."""

	bioc = "ChAMP"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ChAMP_2.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ChAMP/ChAMP_2.32.0.tar.gz"]

	version("2.32.0", md5="cba5699dfd4af0625152f73d2e8e3af5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-champdata@2.6:", type=("build", "run"))
	depends_on("r-dmrcate", type=("build", "run"))
	depends_on("r-illumina450probevariants-db", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicmanifest", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rpmm", type=("build", "run"))
	depends_on("r-prettydoc", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-globaltest", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicanno-ilm10b4-hg19", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-watermelon", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-goseq", type=("build", "run"))
	depends_on("r-missmethyl", type=("build", "run"))
	depends_on("r-kpmt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-isva", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-plotly@4.5.6:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
