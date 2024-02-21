# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsoplotrgui(RPackage):
	"""Web Interface to 'IsoplotR'

	Provides a graphical user interface to the 'IsoplotR' package for radiometric geochronology. The GUI runs in an internet browser and can either be used offline, or hosted on a server to provide online access to the 'IsoplotR' toolbox.
	"""
	
	homepage = "https://www.ucl.ac.uk/~ucfbpve/isoplotr/"
	cran = "IsoplotRgui" 

	version("6.0", md5="8d575405525cb612b18962c3b50896bb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-isoplotr@5.6:", type=("build", "run"))
	depends_on("r-shinylight@1.1.2:", type=("build", "run"))
