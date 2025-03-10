# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikein(RPackage):
	"""Affymetrix Spike-In Experiment Data

	Contains the HGU133 and HGU95 spikein experiment data.
	"""
	
	homepage = "https://bioconductor.org/packages/SpikeIn"
	bioc = "SpikeIn" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/SpikeIn_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/SpikeIn/SpikeIn_1.44.0.tar.gz"]

	version("1.44.0", md5="439f9d2eda54024edb7c1c81862d74c8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

	# experiment