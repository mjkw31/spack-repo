# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcfr(RPackage):
	"""Manipulate and Visualize VCF Data.

	Facilitates easy manipulation of variant call format (VCF) data. Functions
	are provided to rapidly read from and write to VCF files. Once VCF data is
	read into R a parser function extracts matrices of data. This information
	can then be used for quality control or other purposes. Additional
	functions provide visualization of genomic data. Once processing is
	complete data may be written to a VCF file (*.vcf.gz). It also may be
	converted into other popular R objects (e.g., genlight, DNAbin). VcfR
	provides a link between VCF data and familiar R software."""

	cran = "vcfR"

	maintainers("dorton21")

	version("1.15.0", md5="ef023d52f85da793b1c26689d051f100")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memuse", type=("build", "run"))
	depends_on("r-pinfsc50", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
