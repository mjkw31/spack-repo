# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiergwas(RPackage):
	"""Asessing statistical significance in predictive GWA studies

	Testing individual SNPs, as well as arbitrarily large groups of SNPs in GWA studies, using a joint model of all SNPs. The method controls the FWER, and provides an automatic, data-driven refinement of the SNP clusters to smaller groups or single markers.
	"""
	
	bioc = "hierGWAS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/hierGWAS_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/hierGWAS/hierGWAS_1.32.0.tar.gz"]

	version("1.32.0", md5="9f15cfa27c8d57b818fc7913d8a9093b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
