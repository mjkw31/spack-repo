# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTartare(RPackage):
	"""Raw ground spectra recorded on Thermo Fisher Scientific mass spectrometers

	Provides raw files recorded on different Liquid Chromatography Mass Spectrometry (LC-MS) instruments. All included MS instruments are manufactured by Thermo Fisher Scientific and belong to the Orbitrap Tribrid or Q Exactive Orbitrap family of instruments. Despite their common origin and shared hardware components, e.g., Orbitrap mass analyser, the above instruments tend to write data in different "dialects" in a shared binary file format (.raw). The intention behind tartare is to provide complex but slim real-world files that can be used to make code robust with respect to this diversity. In other words, it is intended for enhanced unit testing. The package is considered to be used with the rawrr package and the Spectra MsBackends.
	"""
	
	homepage = "https://github.com/cpanse/tartare"
	bioc = "tartare" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/tartare_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/tartare/tartare_1.16.0.tar.gz"]

	version("1.16.0", md5="869743e16f05bc962de518ca925750d8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub@2.16:", type=("build", "run"))
	depends_on("r-experimenthub@1:", type=("build", "run"))

	# experiment