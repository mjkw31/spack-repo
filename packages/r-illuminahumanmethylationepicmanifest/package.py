# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylationepicmanifest(RPackage):
	"""Manifest for Illumina's EPIC methylation arrays."""

	bioc = "IlluminaHumanMethylationEPICmanifest"
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/IlluminaHumanMethylationEPICmanifest_0.3.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/IlluminaHumanMethylationEPICmanifest/IlluminaHumanMethylationEPICmanifest_0.3.0.tar.gz"]

	version("0.3.0", md5="c6b0268de177badfe0b8184002da7e16")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))

	# annotation