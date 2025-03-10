# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomartr(RPackage):
	"""Genomic Data Retrieval.

	Perform large scale genomic data retrieval and functional annotation
	retrieval. This package aims to provide users with a standardized way to
	automate genome, proteome, 'RNA', coding sequence ('CDS'), 'GFF', and
	metagenome retrieval from 'NCBI RefSeq', 'NCBI Genbank', 'ENSEMBL',
	'ENSEMBLGENOMES', and 'UniProt' databases. Furthermore, an interface to the
	'BioMart' database (Smedley et al. (2009) <doi:10.1186/1471-2164-10-22>)
	allows users to retrieve functional annotation for genomic loci. In
	addition, users can download entire databases such as 'NCBI RefSeq' (Pruitt
	et al. (2007) <doi:10.1093/nar/gkl842>), 'NCBI nr', 'NCBI nt', 'NCBI
	Genbank' (Benson et al. (2013) <doi:10.1093/nar/gks1195>), etc. as well as
	'ENSEMBL' and 'ENSEMBLGENOMES' with only one command."""

	cran = "biomartr"

	version("1.0.7", md5="d7405c52f1076202a4f6188dc9d5c78b")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table@1.9.4:", type=("build", "run"))
	depends_on("r-dplyr@0.3:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-downloader@0.3:", type=("build", "run"))
	depends_on("r-rcurl@1.95.4.5:", type=("build", "run"))
	depends_on("r-xml@3.98.1.1:", type=("build", "run"))
	depends_on("r-httr@0.6.1:", type=("build", "run"))
	depends_on("r-stringr@0.6.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
