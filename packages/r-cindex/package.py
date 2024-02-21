# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCindex(RPackage):
	"""Chromosome Instability Index

	The CINdex package addresses important area of high-throughput genomic analysis. It allows the automated processing and analysis of the experimental DNA copy number data generated by Affymetrix SNP 6.0 arrays or similar high throughput technologies. It calculates the chromosome instability (CIN) index that allows to quantitatively characterize genome-wide DNA copy number alterations as a measure of chromosomal instability. This package calculates not only overall genomic instability, but also instability in terms of copy number gains and losses separately at the chromosome and cytoband level.
	"""
	
	bioc = "CINdex" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CINdex_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CINdex/CINdex_1.30.0.tar.gz"]

	version("1.30.0", md5="2616a2a02791d966dbf54a54f2ad5f42")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-som", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
