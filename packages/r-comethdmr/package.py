# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComethdmr(RPackage):
	"""Accurate identification of co-methylated and differentially methylated regions in epigenome-wide association studies

	coMethDMR identifies genomic regions associated with continuous phenotypes by optimally leverages covariations among CpGs within predefined genomic regions. Instead of testing all CpGs within a genomic region, coMethDMR carries out an additional step that selects co-methylated sub-regions first without using any outcome information. Next, coMethDMR tests association between methylation within the sub-region and continuous phenotype using a random coefficient mixed effects model, which models both variations between CpG sites within the region and differential methylation simultaneously.
	"""
	
	homepage = "https://github.com/TransBioInfoLab/coMethDMR"
	bioc = "coMethDMR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/coMethDMR_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/coMethDMR/coMethDMR_1.6.0.tar.gz"]

	version("1.6.0", md5="0a6229d90868a4a60eb0f72c4499d1fc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
