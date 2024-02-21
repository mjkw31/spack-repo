# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntact(RPackage):
	"""Integrate TWAS and Colocalization Analysis for Gene Set Enrichment Analysis

	This package integrates colocalization probabilities from colocalization analysis with transcriptome-wide association study (TWAS) scan summary statistics to implicate genes that may be biologically relevant to a complex trait. The probabilistic framework implemented in this package constrains the TWAS scan z-score-based likelihood using a gene-level colocalization probability. Given gene set annotations, this package can estimate gene set enrichment using posterior probabilities from the TWAS-colocalization integration step.
	"""
	
	homepage = "https://github.com/jokamoto97/INTACT"
	bioc = "INTACT" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/INTACT_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/INTACT/INTACT_1.2.0.tar.gz"]

	version("1.2.0", md5="d8646f4acb0cbb31ccf53a672818be40")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
