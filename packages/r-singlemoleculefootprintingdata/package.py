# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglemoleculefootprintingdata(RPackage):
	"""Data supporting the SingleMoleculeFootprinting pkg

	This Data package contains data objcets relevanat for the SingleMoleculeFootprinting package. More specifically, it contains one example of aligned sequencing data (.bam & .bai) necessary to run the SingleMoleculeFootprinting vignette. Additionally, we provide data that are essential for some functions to work correctly such as BaitCapture() and SampleCorrelation().
	"""
	
	bioc = "SingleMoleculeFootprintingData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/SingleMoleculeFootprintingData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/SingleMoleculeFootprintingData/SingleMoleculeFootprintingData_1.10.0.tar.gz"]

	version("1.10.0", md5="451ecbdbb964607afbbe3b778b290246")

	depends_on("r-experimenthub", type=("build", "run"))

	# experiment