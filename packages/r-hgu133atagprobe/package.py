# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133atagprobe(RPackage):
	"""Probe sequence data for microarrays of type hgu133atag

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U133A_tag_probe_tab.
	"""
	
	bioc = "hgu133atagprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hgu133atagprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hgu133atagprobe/hgu133atagprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="97aeaf9ac9450369cf030581b8ec5a53")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation