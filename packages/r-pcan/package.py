# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcan(RPackage):
	"""Phenotype Consensus ANalysis (PCAN)

	Phenotypes comparison based on a pathway consensus approach. Assess the relationship between candidate genes and a set of phenotypes based on additional genes related to the candidate (e.g. Pathways or network neighbors).
	"""
	
	bioc = "PCAN" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PCAN_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PCAN/PCAN_1.30.0.tar.gz"]

	version("1.30.0", md5="94596d43854d98aee2e6da198147772b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
